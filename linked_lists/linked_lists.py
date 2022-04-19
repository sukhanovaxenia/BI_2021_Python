class LinkedListItem:
	def __init__(self, value):
		self.value = value
		self.__next = None

	def get_next(self):
		return self.__next

	def set_next(self, next_item):
		self.__next = next_item

	def has_next(self):
		return self.__next is not None

class LinkedList:
	def __init__(self):
		self.__head = None
		self.__tail = None
		self.__len = 0

	def __getitem__(self, index):
		current = self.__head
		for _ in range(index):
			current = current.get_next()
		return current.value

	def __contains__(self, value):
		current = self.__head
		found  = False
		while current:
			if current.value == value or value in current.value:
				found = True
				break
			current = current.get_next()
		return found

	def __len__(self):
		return self.__len

	def add(self, value, index=None):
		self.__len += 1
		new_item = LinkedListItem(value)
		if index is None:
			if not self.__head:
				self.__head = new_item
			else:
				self.__tail.set_next(new_item)
			self.__tail = new_item
		elif index < 0:
			raise IndexError('Index should not be negative!')
		elif index > self.__len:
			raise IndexError("Index out of range!")
		elif index == 0:
			new_item.set_next(self.__head)
			self.__head = new_item
		else:
			prev_item, current = None, self.__head
			i = 0
			while i < index and current.has_next():
				prev_item = current
				current = current.get_next()
				i += 1
			if i == index:
				prev_item.set_next(new_item)
				new_item.set_next(current)
		return self

	def extend(self, values, index=None):
		for value in values:
			self.add(value, index)
		return self

	def first(self):
		return self.__head.value

	def last(self):
		return self.__tail.value

	def pop(self, index=None):
		if self.__head is None:
			return
		if index is None:
			index = self.__len - 1
		if index < 1:
			raise ValueError("Index is not valid!")
		if index > self.__len:
			raise IndexError("Index out of range!")
		# convenient to operate by values
		current, prev = self.__head, None
		if current:
			i = 0
			while current.get_next() is not None:
				if i == index:
					break
				else:
					prev = current
					current = current.get_next()
					i += 1
			if prev is None:
				self.__head = current.get_next()
				if current.get_next() is None:
					self.__tail = current.get_next()
			else:
				prev.set_next(current.get_next())
		self.__len -= 1
		return self

	def remove_last_occurrence(self, value):
		regular_list = self.list_iterator()
		detect = 0
		for i, val in enumerate(regular_list):
			if val == value:
				detect = i
		return self.pop(index=detect)
		#if current.value == value:
		#	return current.get_next()
		#while current.get_next():
		#	if current.get_next().value == value:
		#		prev.set_next(current.get_next())
		#		break
		#	prev = current
		#	current = current.get_next()
		#return prev

	def list_iterator(self):
		current = self.__head
		if not current:
			return []
		l_list = []
		while current:
			l_list.append(current.value)
			current = current.get_next()
		return l_list

if __name__ == "__main__":
	items = LinkedList()
	items.add(10)
	items.add(11)
	items.add(12)
	items.add(13)
	items.add(20)
	print(items[1])
	print(items[2])
	print(items[100])
	print(items.first())
	print(items.last())
	print(len(items))