"""
Interview question: You are given a list of n-1 integers and these integers are in the range of 1 to n.
There are no duplicates in the list. One of the integers is missing in the list. 
Write an efficient code to find the missing integer.
"""


def find_n_number(list_of_numbers): 
    num = len(list_of_numbers)
    totalValue = (num + 1) * (num + 2)/2
    sum_of_list = sum(list_of_numbers)
    return totalValue - sum_of_list


list_of_num = [1, 2, 4, 5, 6, 7, 8, 9, 10] 
missing_number = find_n_number(list_of_num) 
print(missing_number) 

