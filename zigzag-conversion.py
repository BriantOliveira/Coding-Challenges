"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
       # In case the input string is empty
        if  len(s) == 0:
            return ""
        # In case the input string only contain one element
        if len(s) == 1:
            return s
        # In case there is only one row
        if numRows == 1:
            return s

        length = len(s)
        new_array = []
        cycle = 2*numRows - 2
        
        row_n = 0 

        for i in range(numRows):    
            for j in range(i, length, cycle):
                new_array.append(s[j])
                if i != numRows-1 and i != 0 and j+cycle-2*i < length:
                    new_array.append(s[j+cycle-2*i])
        newstr = ''.join(new_array)
        return newstr
          