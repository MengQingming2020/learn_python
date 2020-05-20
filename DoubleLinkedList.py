#带头节点和尾节点两个哨兵的双向链表
#基本的插入、查找、删除操作

class Node(object):
    """双向链表结构的Node节点"""
    def __init__(self,data,pre_node=None,next_node=None):
        """Node节点的初始化方法
        参数：
            data：存储的数据
            pre_node：前一个节点的引用地址
            next_node：后一个节点的引用地址
        """
        self.data = data
        self.pre =pre_node
        self.next = next_node

class DoubleLinkedList(object):
    """带头节点和尾节点两个哨兵的双向链表"""
    def __init__(self):
        """带头节点和尾节点两个哨兵的双向链表初始化方法
            两个哨兵都是不存储数据的节点
        """
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def is_empty(self):
        """检查链表是否为空
        返回：
            True：链表为空
            False：链表不为空
        """
        if self.head.next is self.tail:
            return True
        else:
            return False

    def add(self,node):
        """在头节点之后添加一个节点
        参数：
            node:待添加节点
        """
        node.pre = self.head
        self.head.next.pre = node
        node.next = self.head.next
        self.head.next = node

    def add_value(self,value):
        """在头节点之后添加一个数据
        参数：
            value：待添加数据"""
        new_node = Node(value)
        self.add(new_node)

    def append(self,node):
        """在尾节点之前添加一个节点
        参数：
            node：待添加节点
        """
        node.next = self.tail
        self.tail.pre.next = node
        node.pre = self.tail.pre
        self.tail.pre = node

    def append_value(self,value):
        """在尾节点之前添加一个数据
        参数：
            value：带添加数据
        """
        new_node = Node(value)
        self.append(new_node)

    def insert_after(self,node,value):
        """在指定节点之后插入一个数据
        参数：
            node：指定节点
            value：待插入数据
        """
        new_node = Node(value)
        new_node.pre = node
        node.next.pre = new_node
        new_node.next = node.next
        node.next = new_node
    
    def insert_before(self,node,value):
        """在指定节点之前插入一个数据
        参数：
            node：指定节点
            value：待插入数据"""
        new_node = Node(value)
        new_node.next = node
        node.pre.next = new_node
        new_node.pre = node.pre
        node.pre = new_node

    def find_by_value(self,value):
        """按照数据值在查找
        参数：
            value：要查找的数据
        返回：
            node：找到的第一个节点；若未找到，返回False
        """
        if self.head.next is self.tail:
            return
        node = self.head.next
        while node is not self.tail:
            if node.data == value:
                return node
            node = node.next
        else:
            return

    def find_by_index(self,index):
        """按照索引值查找
        参数：
            index：索引值
        返回：
            node：找到的第一个节点；若未找到，返回False
        """
        node = self.head
        count = 0
        while node is not None and count is index:
            node = node.next
            count += 1
        return node

    def delete_first(self):
        """删除头节点之后的第一个节点
        返回：
            data：已删除节点中存储的数据
        """
        if self.head.next is self.tail:
            return
        data = self.head.next.data
        self.head.next.next.pre = self.head
        self.head.next = self.head.next.next
        return data

    def delete_last(self):
        """删除尾节点之前的第一个节点
        返回：
            data：已删除节点中存储的数据
        """
        if self.head.next is self.tail:
            return
        data = self.tail.pre.data
        self.tail.pre.pre.next = self.tail
        self.tail.pre = self.tail.pre.pre
        return data

    def delete_node(self,node):
        """删除指定节点
        参数：
            node：待删除节点
        返回：
            若未找到返回False
        """
        if self.head.next is self.tail:
            return
        cur = self.head.next
        not_found = False
        while cur is not node:
            if cur is self.tail:
                not_found = True
                return
            else:
                cur = cur.next
        if not not_found:
            cur.pre.next = cur.next
            cur.next.pre = cur.pre
    
    def delete_value(self,value):
        """删除第一个存储指定数据的节点
        参数：
            value：待删除数据
        返回：
            若未找到返回False
        """
        if self.head.next is self.tail:
            return
        cur = self.head.next
        not_found = False
        while cur.data is not value:
            if cur is self.tail:
                not_found = True
                return
            else:
                cur = cur.next
        if not not_found:
            cur.pre.next = cur.next
            cur.next.pre = cur.pre

    def clear(self):
        """清空链表"""
        self.head.next = self.tail
        self.tail.pre = self.head

    def print_all(self):
        """按照顺序打印链表中的所有数据"""
        if self.head.next is self.tail:
            print("这个链表是空的。")
            return
        node = self.head.next
        while node.next is not self.tail:
            print(str(node.data)+"-->",end=" ")
            node = node.next
        print(str(node.data))

    def print_reverse(self):
        """按照逆序打印链表中的所有元素"""
        if self.head.next is self.tail:
            print("这个链表是空的。")
            return
        node = self.tail.pre
        while node.pre is not self.head:
            print(str(node.data)+"-->",end=" ")
            node = node.pre
        print(str(node.data))



if __name__ == '__main__':
    l = DoubleLinkedList()
    for i in range(10):
        l.add_value(i)
    l.print_all()

    l.append_value(100)
    l.print_reverse()

    node0 = l.find_by_value(0)
    l.insert_after(node0,99)
    l.insert_before(node0,98)
    l.print_all()

    l.delete_first()
    l.delete_last()
    l.print_all()

    l.delete_node(node0)
    l.delete_value(5)
    l.print_all()

    l.clear()
    l.print_reverse()
        

