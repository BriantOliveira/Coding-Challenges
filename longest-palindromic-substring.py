"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""   
        longest = ""
        for m in range(len(s)):
            # palindrome expands at the center m
            sub = self.palindrome(s, m, m)
            if len(sub) > len(longest):
                longest = sub
            # palindrome expands at the center between m and m + 1
            sub = self.palindrome(s, m, m + 1)
            if len(sub) > len(longest):
                longest = sub
        return longest  
    # palindrome function finds the longest palindrome in string s from center m or center m and m+1.
    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1 
        return s[l + 1:r]
