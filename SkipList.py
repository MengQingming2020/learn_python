#一开始阅读和实现起来比较坑的跳表

import random

class Node(object):
    def __init__(self, value, max_hight = 0):
        self.data = value
        self.next = [None] * max_hight  #申请长度为max_high的数组来存放节点的指针

class SkipList(object):
    def __init__(self):
        self.MAXLEVEL = 16  #跳表的最大层数限制
        self.PERCENT = 0.5  #用于__random_high函数中，确定索引的疏密，0.5相当于上层索引个数约为下层的一半
        self.high = 1
        self.head = Node(None, self.MAXLEVEL)   #这是一个带头链表；另外，self.MAXLEVEL不能用self.high代替，头节点的指针个数一经确定，不会更新,因为已申请用于存储指针的数组长度不能随意变化
        """
        不要被课程中的示意图误导，跳表实际上是长这样的：

                    head.next[15] ----> None
                    ... ...
                    head.next[2] -----> None

                    head.next[1] --------------------------------------------        node2.next[1] -----> None
                                                                            ↓
        head.data|  head.next[0] -----> node1.data| node1.next[0] -----> node2.data| node2.next[0] -----> None

        从上图可以看出： 1.头节点出生自带16个指针，存储在一个长度为16的数组（list)中，所以可以直接根据下标访问各个指针
                        2.每个节点至少有一个指针，指向第0层链表中的下一个节点，node1就是这样只有一个指针的非酋
                        3.可以根据第1层的指针head.next[1]找到node2.data2,自然也能根据node2的两个指针访问其各自所指的节点
        """

    def find(self, value):
        p = self.head
        for i in range(self.high-1, -1, -1):
            while p.next[i] != None and p.next[i].data < value:
                p = p.next[i]
        if p.next[0] != None and p.next[0].data == value:
            return p.next[0]
        else:
            return None

    def insert(self, value):
        high = self.__random_high()

        if self.high < high:    
            self.high = high

        new_node = Node(value, high)

        updata = [None] * high    #申请一个长度为high的数组，用于存储游标 p 的查找路线
        p = self.head
        for i in range(high - 1, -1, -1):
            while p.next[i] != None and p.next[i].data < value:
                p = p.next[i]
            updata[i] = p

        for i in range(high):   #在node节点之后插入new_node: new_node.next = node.next    node.next = new_node
            new_node.next[i] = updata[i].next[i]    
            updata[i].next[i] = new_node

    def delete(self, value):
        updata = [None] * self.high

        p = self.head
        for i in range(self.high-1, -1, -1):
            while p.next[i] != None and p.next[0].data < value:
                p = p.next[i]
            updata[i] = p

        if p.next[0] != None and p.next[0].data == value:
            for i in range(self.high-1, -1, -1):
                if updata[i].next[i] != None and updata[i].next[i].data == value:
                    updata[i].next[i] = updata[i].next[i].next[i]

        while self.high > 1 and self.head.next[self.high] == None:
            self.high -= 1

    def __random_high(self):
        high = 1
        while random.random() < self.PERCENT and high < self.MAXLEVEL:
            high += 1
        return high

    def __repr__(self):
        vals = []
        p = self.head
        while p.next[0] != None:
            vals.append(str(p.next[0].data)) #我也想不申请数组，直接像链表那样打印，奈何总是报错 (ง •_•)ง
            p = p.next[0] 
        return '->'.join(vals)


if __name__ == '__main__':
    sl = SkipList()
    print(sl.head.next)
    for i in range(10):
        sl.insert(i)
    print(sl)
    p = sl.find(7)
    print(p.data)
    sl.delete(7)
    print(sl)
    sl.delete(4.5)
    print(sl)