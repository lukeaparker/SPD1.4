# Write a function that takes two lists of numbers and combines them into a single list.

He asked specific questions about the examples. 
The structure of the numbers. The sorting state of the numbers. 
Solving with binary search but it was too slow. 
They used a hashset. They explained that it was the faster solution over a log n solution. 
Making it faster. 
He did a really good job of communicating and talking his way through the problem. 



list1 = [23, 32, 22, 45, 67, 3]
list2 = [2, 3, 4, 6, 7, 7]

def list_union(list1, list2):
    new_list = list1 + list2
    print(new_list)
    return new_list

list_union(list1, list2)
