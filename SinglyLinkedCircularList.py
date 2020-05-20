#单向循环链表的基本查找、插入、删除操作

class Node(object):
	"""链表结构的Node节点"""

	def __init__(self,data,next_node = None):
		"""Node节点的初始化方法.
        参数:
            data:存储的数据
            next:下一个Node节点的引用地址
        """
		self.data = data
		self.next = next_node

class SinglyLinkedCircularList(object):
	"""单向循环链表"""
	
	def __init__(self):
		"""单向列表的初始化方法."""
		self.tail = None	#在这个循环链表中，尾节点与实际的头节点重合了，因此取名tail更容易阅读
	
	def is_empty(self):
		"""检验列表是否为空"""
		return self.tail is None

	def create_node(self,value):
		"""创建一个存储value值的Node节点.
        参数:
            value:将要存储在Node节点中的数据
        返回:
            一个新的Node节点
        """
		return Node(value)
	
	def find_by_value(self,value):
		"""按照数据值在链表中查找.
        参数:
            value:查找的数据
        返回:
            Node
        """
		if self.tail is None:
			return
		node = self.tail.next
		not_found = False
		while node.data is not value:
			if node is self.tail:
				not_found = True
				break
			else:
				node = node.next
		if not not_found:
			return node

	def find_by_index(self,index):
		"""按照索引值在链表中查找.
        参数:
            index:索引值
        返回:
            Node
        """
		node = self.tail.next
		pos = 0
		while pos is not index and node is not self.tail:
			node = node.next
			pos += 1
		return node

	def add_value(self,value):
		"""在链表的头部插入一个存储value数值的Node节点.
        参数:
            value:将要存储的数据
        """
		new_node = Node(value)
		if self.tail is None:
			new_node.next = new_node
			self.tail = new_node
		else:
			new_node.next = self.tail.next
			self.tail.next = new_node
	
	def add(self,node):
		"""在链表的头部插入一个Node节点.
        参数:
            node:将要插入的节点
        """
		if self.tail is None:
			node.next = node
			self.tail = node
		else:
			node.next = self.tail.next
			self.tail.next = node
	
	def append_value(self,value):
		"""从链表尾部插入一个指定值Value的节点
		参数:
        	value:将要存储的数据
		"""
		self.add_value(value)	#循环链表中，在头部插入一个节点，即在尾节点之后插入一个节点
		self.tail = self.tail.next	#将新插入的节点定义为尾节点
		
	def append(self,node):
		"""在链表的头部插入一个Node节点.
        参数:
            node:将要插入的节点
        """
		self.add(node)
		self.tail = self.tail.next

	def insert_after(self,node,value):
		"""在链表的某个指定Node节点之后插入一个存储value数据的Node节点.
        参数:
            node:指定的一个Node节点
            value:将要存储在新Node节点中的数据
        """
		if node is None or self.tail is None:
			return
		new_node = Node(value)
		new_node.next = node.next
		node.next = new_node

	def insert_before(self, node, value):
		"""在链表的某个指定Node节点之前插入一个存储value数据的Node节点.
        参数:
            node:指定的一个Node节点
            value:将要存储在新的Node节点中的数据
        """
		if node is None or self.tail is None:  
			return
		else:
			new_node = Node(value)
			cur = self.tail.next
			not_found = False
			while cur.next is not node:
				if cur is self.tail:
					not_found = True
					break
				else:
					cur = cur.next
			if not not_found:
				cur.next = new_node
				new_node.next = node
		
	def delete_first(self):
		"""删除头节点
		返回：
			data:头节点的值
        """
		if self.tail is None:
			return
		else:
			data = self.tail.next.data
			self.tail.next = self.tail.next.next
			return data

	def delete_last(self):
		"""删除尾节点
		返回：
			data:尾节点的值
        """
		if self.tail is None:
			return
		else:
			cur = self.tail.next
			if cur is self.tail:
				self.tail = None
				return cur.data
			else:
				while cur.next is not self.tail:
					cur = cur.next
				data = cur.next.data
				cur.next = cur.next.next
				self.tail = cur
				return data

	def delete_by_node(self, node):
		"""在链表中删除指定Node的节点.
        参数:
            node:指定的Node节点
        """
		if node is None or self.tail is None:  
			return
		else:
			cur = self.tail.next
			not_found = False
			while cur.next is not node:
				if cur is self.tail:
					not_found = True
					break
				else:
					cur = cur.next
			if not not_found:
				cur.next = cur.next.next

	def delete_by_value(self, value):
		"""在链表中删除指定存储数据的Node节点.
        参数:
            value:指定的存储数据
        """
		if self.tail is None:
			return
		else:
			cur = self.tail.next
			not_found = False
			while cur.next.data is not value:
				if cur is self.tail:
					not_found = True
					break
				else:
					cur = cur.next
			if not not_found:
				cur.next = cur.next.next

	def reverse_self(self):
		"""翻转链表的指针"""
		pre = self.tail
		node=self.tail.next
		head = self.tail.next
		while node is not self.tail:
			next_node = node.next
			node.next = pre
			pre = node
			node = next_node
		node.next = pre
		self.tail = head


	def print_all(self):
		"""打印当前链表所有节点的数据"""
		if self.tail is None:
			print("当前链表为空")
		else:
			node = self.tail.next
			while node is not self.tail:
				print(str(node.data)+"-->",end = " ")
				node = node.next
			print(str(node.data))
			
if __name__ == "__main__":
	l = SinglyLinkedCircularList()
	for i in range(10):
		l.add_value(i)
	l.print_all()
	print(l.is_empty())
	l.append_value(10)
	l.print_all()
	print(l.delete_first())
	l.print_all()
	l.add_value(9)
	l.print_all()
	print(l.delete_last())
	l.print_all()
	node7 = l.find_by_value(7)
	print(node7)
	l.insert_before(node7,100)
	l.print_all()
	l.delete_by_value(100)
	l.print_all()
	l.insert_after(node7,99)
	l.print_all()
	l.delete_by_node(node7.next)
	l.print_all()
	node3th = l.find_by_index(3)
	print(node3th)

	l.reverse_self()
	l.print_all()
