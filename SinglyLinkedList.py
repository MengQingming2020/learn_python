# 1.单链表的插入、删除、查找操作；
# 2.链表中存储的数据类型是Int
"""
    singlyLinkedList中实现的方法声明：
    查找方法：
        find_by_value(self,value) 按照数值value查找
        find_by_index(self,index) 按照索引查找
        find_last_node(self) 查找尾节点
    插入方法：
        add_value(self,value) 从头部插入值
        add(self,node)在链表头部插入一个节点
        append_value(self,value)在链表尾部插入一个存储value数值的节点
        append(self,node)在链表尾部插入一个节点
        insert_value_after(self,node,value) 在指定节点之后插入值
        insert_after(self,node,insert_node)在链表的某个指定Node节点之后插入一个Node节点.
        insert_value_before(self,node,value) 在指定节点之前插入值
        insert_before(self, node, insert_node)在链表的某个指定Node节点之前插入一个Node节点

    删除方法：
        delete_by_node(self,node) 删除指定节点
        delete_by_value(self,value) 删除存储指定数据的节点
    其他方法：
        is_empty(self)判断链表是否为空
        length(self) 计算链表节点个数
        delete_last_n_node(self,n) 删除倒数第n个节点
        find_mid_node(self) 查找链表的中间节点
        creat_node(self,value) 创建一个存储指定值的节点
        print_all(self) 打印链表的所有节点数据
        revered_self(self) 翻转链表自身
        __reversed_with_two_nodes(self) 翻转两个相邻节点
        has_ring(self) 判断链表是否有环
        __iter__(self) 改写用for关键字遍历链表的方法
        __repr__(self) 改写用print关键字打印链表的方法
"""

class Node(object):
    """链表结构的Node节点"""

    #__init__是初始化的方法；注意前后各有两个下划线；
    # 一个初始化的节点不指向任何一个节点，所以next_node默认为None
    def __init__(self, data, next_node=None):   
        """Node节点的初始化方法.
        参数:
            data:存储的数据
            next_node:下一个Node节点的引用地址
        """
        self.data = data
        self.next = next_node

        
class SinglyLinkedList(object):
    """单向链表"""

    def __init__(self):
        """ 单向列表的初始化方法"""
        self.head = None

    def is_empty(self):
        """检查链表是否为空"""
        return self.head is None


    def find_by_value(self, value):
        """按照数据值在单向列表中查找，若有多个节点存储了value,只返回第一个存储value节点的位置
        参数:
            value:查找的数据
        返回:
            Node
        """
        node = self.head
        while node is not None and node.data is not value:  
            node = node.next
        return node #node实际上是这个节点的内存地址，如果没有找到，node == None；
        #可以用node.data,node.next分别读取这个节点存储的数据和下一节点的内存地址
        
    def find_by_index(self, index):
        """按照索引值在列表中查找.
        参数:
            index:索引值
        返回:
            Node
        """
        node = self.head
        pos = 0
        while node is not None and pos is not index:
            node = node.next
            pos += 1
        return node

        
    def add_value(self, value):
        """在链表的头部插入一个存储value数值的Node节点.
        参数:
            value:将要存储的数据
        """
        new_node = Node(value)
        new_node.next = self.head    #将待插入节点的指针指向头节点
        self.head = new_node  #将待插入节点定义为链表的头节点

    def add(self,node):
        """在链表头部插入一个节点"""
        node.next = self.head
        self.head = node

    def append_value(self,value):
        """在链表尾部插入一个存储value数值的节点
        参数：
            value：将要存储的数据
        """
        new_node = Node(value)
        if self.head is None:
            self.add(new_node)
        else:
            pre = self.head
            while pre.next is not None:
                pre = pre.next
            pre.next = new_node

    def append(self,node):
        """在链表尾部插入一个节点"""
        if self.head is None:
            self.add(node)
        else:
            pre = self.head
            while pre.next is not None:
                pre = pre.next
            pre.next = node
   
    def insert_value_after(self, node, value):
        """在链表的某个指定Node节点之后插入一个存储value数据的Node节点.
        参数:
            node:指定的一个Node节点
            value:将要存储在新Node节点中的数据
        """
        if node == None:    #如果这个节点不存在
            return  #return后面如果不带任何变量，默认为None
        else:
            new_node = Node(value)
            new_node.next = node.next #将待插入节点的指针指向指定节点的下一个节点
            node.next = new_node   #将指定节点的指针指向待插入节点

    def insert_after(self, node, insert_node):
        """在链表的某个指定Node节点之后插入一个Node节点.
        参数:
            node:指定的一个Node节点
            insert_node:将要插入的节点
        """
        if node == None:    #如果这个节点不存在
            return  #return后面如果不带任何变量，默认为None
        else:
            insert_node.next = node.next #将待插入节点的指针指向指定节点的下一个节点
            node.next = insert_node   #将指定节点的指针指向待插入节点

    def insert_value_before(self, node, value):
        """在链表的某个指定Node节点之前插入一个存储value数据的Node节点.
        参数:
            node:指定的一个Node节点
            value:将要存储在新的Node节点中的数据
        """
        if node == self.head: #如果指定节点是头节点，直接插入
            self.add_value(value)  #注意调用这个类自身的方法或属性，方法名或属性名前面要加上 self.
        elif node == None:  #如果指定节点是一个空节点，返回None
            return
        else:
            new_node = Node(value)
            pre = self.head
            not_found = False   #有时候逻辑太复杂理不清，可以考虑增加一个用作分类判断的变量
            while pre.next is not node:    #直到pre移动到指定节点的前一个节点的位置停止
                if pre.next == None:   #如果直到链表的结尾都没有找到指定节点
                    not_found = True
                    return False
                    break
                else:
                    pre = pre.next
            if not not_found:   #如果找到了指定节点，就在pre之后插入新节点，插入逻辑与insert_after相同
                new_node.next = pre.next
                pre.next = new_node
    
    def insert_before(self, node, insert_node):
        """在链表的某个指定Node节点之前插入一个Node节点.
        参数:
            node:指定的一个Node节点
            insert_node:将要插入的节点
        """
        if node == self.head: #如果指定节点是头节点，直接插入
            self.add_value(value)  #注意调用这个类自身的方法或属性，方法名或属性名前面要加上 self.
        elif node == None:  #如果指定节点是一个空节点，返回None
            return
        else:
            pre = self.head
            not_found = False   #有时候逻辑太复杂理不清，可以考虑增加一个用作分类判断的变量
            while pre.next is not node:    #直到pre移动到指定节点的前一个节点的位置停止
                if pre.next == None:   #如果直到链表的结尾都没有找到指定节点
                    not_found = True
                    return False
                    break
                else:
                    pre = pre.next
            if not not_found:   #如果找到了指定节点，就在pre之后插入新节点，插入逻辑与insert_after相同
                insert_node.next = pre.next
                pre.next = insert_node
    
    def delete_by_node(self, node):
        """在链表中删除指定Node的节点.
        参数:
            node:指定的Node节点
        """
        if self.head == None:  #如果链表为空
            return
        elif node == self.head:    #如果要删除的节点是头节点
            self.head = node.next    #把头节点的下一个节点指定为头节点，也可写成self.head = self.head.next
        else:
            pre = self.head
            not_found = True
            while pre.next is not node:
                if pre.next == None: #如果到链表的尾部都没有找到指定节点
                    not_found = True
                    break
                else:
                    pre = pre.next
            if not not_found:
                pre.next = node.next  #把node前一个节点的指针指向node的后一个节点,自然就把node删除了

    def delete_by_value(self, value):
        """在链表中删除指定存储数据的Node节点.
        参数:
            value:指定的存储数据
        """
        node = self.find_by_value(value)    #先找到这个节点
        self.delete_by_node(node)   #再直接删除
    
    def length(self):
        """计算链表节点的个数
        返回：
            count
        """
        node = self.head
        count = 0
        while node is not None:
            node = node.next
            count += 1
        return count

    def delete_last_n_node(self, n):
        """删除链表中倒数第N个节点.
        主体思路：
            设置快、慢两个指针，快指针先行，慢指针不动；
            当快指针跨了N步以后，快、慢指针同时往链表尾部移动，
            当快指针到达链表尾部的时候，慢指针所指向的下一个节点就是链表的倒数第N个节点
        参数:
            n:需要删除的倒数第N个序数
        """
        fast = self.head
        slow = self.head
        step = 0

        len = self.length()
        if n > len or n <= 0:   #如果n超出或小于链表的节点个数
            print("链表中不存在倒数第%d个节点"%n)
        elif n == len:  #如果实际要删除的是头节点
            self.head = fast.next
        else:
            while step < n :    #快指针先前进n步
                fast = fast.next
                step += 1
            while  fast.next is not None: #快指针抵达链表尾部时停止
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next #删除慢指针的下一个节点
              
    def find_mid_node(self):
        """查找链表中的中间节点.
        主体思想:
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，
            则当快指针到达链表尾部的时候，慢指针指向链表的中间节点
        返回:
            node:链表的中间节点
        """
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None: #不能交换这两个条件的位置，否则当链表节点数为偶数时，指针会越界
            fast = fast.next.next #快指针每次前进两步
            slow = slow.next
        return slow
        
    def reversed_self(self):
        """ 翻转链表自身 
            从头节点开始依次翻转指针的方向
        """
        if self.head == None or self.head.next == None:    #如果链表为空或只有一个节点
            return
        else:
            pre = self.head
            node = pre.next
            while node is not None:
                pre,node = self.__reversed_with_two_nodes(pre,node)
            self.head.next = None #翻转原来头节点的指针
            self.head = pre   #指针全部翻转后pre变成了链表的头节点

    def __reversed_with_two_nodes(self, pre, node):
        """翻转相邻两个节点之间的指针，注意如果单独翻转两个相邻节点的指针可能断开链表，并形成循环
        参数:
            pre:前一个节点
            node:当前节点
        返回:
            (pre,node):下一个相邻节点的元组
        """
        tmp = node.next    #存储node下一个节点的位置
        node.next = pre    #翻转pre和node之间的指针
        pre = node  #将pre移动到node的位置
        node = tmp  #将node移动到它下一个节点的位置
        return (pre,node)

    def has_ring(self):
        """检查链表中是否有环.
        主体思想：
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，
            如果快指针没有与慢指针相遇而是顺利到达链表尾部,
            说明没有环；否则，存在环
        返回:
            True:有环
            False:没有环
        """
        fast = self.head
        slow = self.head
        ring = False
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                ring = True
        return ring
    
    def create_node(self, value):
        """创建一个存储value值的Node节点.
        参数:
            value:将要存储在Node节点中的数据
        返回:
            一个新的Node节点
        """
        return Node(value)
        
    def print_all(self):
        """打印当前链表所有节点数据."""
        node = self.head
        if node == None:
            print("当前链表还没有数据")
            return
        while node.next is not None:
            print(str(node.data)+" -->",end = " ")
            node = node.next
        print(str(node.data))   #这个打印的时尾节点
    
    def __iter__(self): #如果不理解，可以查询python中迭代器与生成器的内容
        """重写__iter__方法，方便for关键字调用打印值"""
        node = self.head
        while node is not None:
            yield node.data #yield会暂停循环，存储当前数值，并作为下一次执行该程序的起始位置
            node = node.next

    def __repr__(self):
        """重写__repr__方法，可直接用print关键字打印链表内容"""
        nums = []
        current = self.head
        while current is not None:
            nums.append(current.data)
            current = current.next
        return " --> ".join(str(num) for num in nums)       

if __name__ == "__main__":
    l = SinglyLinkedList()
    for i in range(10):
        l.add_value(i)
    l.print_all()

    print(l.is_empty())

    node9 = l.find_by_value(9)
    print("按值查询",node9)
    l.insert_value_after(node9,100)
    l.append_value(77)
    l.print_all()

    node3th = l.find_by_index(3)
    print("按索引查询",node3th)
    l.insert_value_before(node3th,99)
    l.print_all()

    l.delete_by_node(node3th)
    l.print_all()

    l.insert_value_after(node9,88)
    l.delete_by_value(99)
    l.print_all()

    l.delete_last_n_node(9)
    print(l)

    print("链表的节点个数",l.length())

    nodenew = l.create_node(88)
    print("新节点的地址",nodenew)

    l.reversed_self()
    print("翻转链表",l)

    nodemid = l.find_mid_node()
    print("中间节点",nodemid)
    nodemid.data = 66
    print(l)
    
    print("是否有环",l.has_ring())

    for i in l:
        print(i)