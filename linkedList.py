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
            return
        elif self.length == 1:
            self.tail = None
            self.head = None
            self.length -= 1
        else:
            temp, prev = self.head, None
            # go to last node while keep last - 1 in variable
            while temp.next:
                prev = temp
                temp = temp.next

            self.tail = prev
            prev = temp
            temp = None
            self.length -= 1
        return prev        

my_ll = LinkedList(1)
my_ll.append(3)
print(my_ll.print_list())
