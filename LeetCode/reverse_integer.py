"""
Given a 32-bit signed integer, reverse digits of an integer.
Example:
    Input: 123
    Output: 321

Assume we are dealing with an environment which could only 
store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 
when the reversed integer overflows.
"""

# class Solution:
#     def reverse(self, x: int) -> int:
#         reverse_int = 0 
#         while x > 0:
#             reverse_int = (10*reverse_int) + x%10
#             x //= 10
#         return  reverse_int

class Solution:
    def reverse(self, x: int) -> int:
        # If element is greater then 0
        if x > 0:
            value = 1
        # Check if element is less then 0
        elif x < 0:
            value = -1
            x = -x
        # otherwise element is 0
        else:
            value = 0
        # Convert element to a string, and then revert the string, and convert the string to 
        # integer again
        result = (int(repr(x)[::-1])) * value

        # Check if result is the max 32-bit 
        if result < 2**31 and result > -2**31:
            return result
        # If result overflow 32-bit return 0
        else:
            return 0
