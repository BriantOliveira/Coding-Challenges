"""
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.

Exemple: 
    Input: 121
    Output: true

    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, 
    it becomes 121-. Therefore it is not a palindrome.

    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if int is negative return False
        if x < 0:
            return False
        # Check if int is greater or equal to 0
        if x >= 0: 
            # Convert int to string and revert the string
            toString = str(x)[::-1]
            # Loop through the string
            for i in toString:
                # join all the elements on the string. Ex: '1, 2, 1' to '121'
                new = "".join(toString)
                # Convert string back to integer
                new_value = int(new)
                # Check if new string is equal to inputed string 
                # If is equal return True
                if new_value == x:
                    return True
            # If not true, always return false
            return False