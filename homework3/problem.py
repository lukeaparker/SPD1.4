from math import ceil
from linkedlist import LinkedList

ll = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])



def find_middle(ll):
    node = ll.head
    length = ll.length() 
    middle = length // 2
    i = 1

    while i < middle:
        node = node.next
        i += 1 
    print(node.data)
    return node.data

find_middle(ll)




    