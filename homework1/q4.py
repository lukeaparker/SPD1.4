# Given a large number of ints, return the largest possible product of 3 numbers.

num_list = [10, 2, 5, 20, 50]

def largest(num_list):
    ordered = num_list.sort()
    list_last = len(num_list) - 1
    list_second_last = list_last - 1
    list_third_last = list_second_last - 1
    sum = num_list[list_last] + num_list[list_second_last] + num_list[list_third_last]
    return sum

largest(num_list)