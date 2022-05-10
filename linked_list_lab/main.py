from LinkedList import LinkedList
from Node import Node

# Linked list testing
list1 = LinkedList()
list1.add_element_end(1)
list1.add_element_end(2)
list1.add_element_end(3)

list2 = LinkedList()
list2.add_element_end(4)
list2.add_element_end(5)
list2.add_element_end(6)

list1.extend(list2)
current = list1.get_front()
while list1.get_end() != current:
    print(current.data)
    current = current.next
print(current.data)

