"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def split(self, word): 
        return [char for char in word]


    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeenDict = {}
        longest = [0, 1]
        start = 0 
        
        for i, char in enumerate(s):
            if char in lastSeenDict:
                start = max(start, lastSeenDict[char] + 1)
            if longest[1] - longest[0] < i + 1 - start:
                longest = [start, i + 1]
            lastSeenDict[char] = i
        return len(s[longest[0]:longest[1]])

        
# This example works, but if fails to find the substring,
# it thinks the substring is a subsequence 
# def split(word): 
#     return [char for char in word]
  
# def lengthOfLongestSubstring(s: str) -> int:
#   dict = {}
#   new_string = split(s)
  
#   if len(s) < 1:
#     return 0
  
#   for i in new_string:
#     value = i
#     if value in dict:
#       dict[value] += 1
    
#     else:
#       count = 1
#       dict[value] = count
      
#   final_value = len(dict)
#   return final_value

