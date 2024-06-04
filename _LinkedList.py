class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self) -> Node:
        if self.length == 0:
            return None
        temp, prev = self.head, self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        temp.next = None
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    

    def get(self, index):
        if index < 0 or index >=  self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp


    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1) 
        new_node.next = temp.next
        temp.next = new_node
        return True

my_ll = LinkedList(1)
my_ll.append(3)
my_ll.append(5)
# my_ll.print_list()
# print(my_ll.pop().value)
my_ll.prepend(0)
# my_ll.print_list()
# print('*'*30)
# print('pop')
# print(my_ll.pop_first())
# print('*'*30)
my_ll.print_list()

print('*'*30)
print(my_ll.set(2, 2))

print('*'*30)
my_ll.print_list()



