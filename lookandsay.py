"""
Look and Say
Implement a function that outputs the Look and Say sequence:
1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211
"""

from itertools import groupby

def look_and_say(number):
    return ''.join(str(len(list(g))) + k
        for k, g in groupby(number))

    numberstring = '1'
    for i in range(10):
        print(numberstring)
        numberstring = look_and_say(numberstring)
