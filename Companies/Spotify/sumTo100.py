"""
Given an array of integers, return indices of the two numbers such that 
they add up to a specific target. You may assume that each input would have 
exactly one solution, and you may not use the same element twice.
Exemple:
Given nums = [1, 2, 15, 98, 99,], target = 100,
Because nums[0] + nums[4] = 1 + 99 = 100,
return [0, 4].
"""

class Solution:
    def sumTo100(self, nums: List[int]) -> List[int]:
        target = 100
        dict = {}
        # Loop through the list of numbers
        for i in range(len(nums)):
            value = nums[i]
            # subtract the target value from current index. 9 - 2 = 7
            result = target - value
            # Check if result "7" exist in the dict
            if result in dict:
                # If the result value exist then you return the index which in this
                # case if the value in the dict and the current index
                return [dict[result], i]
            # If the value doesn't exist in the dictionary, add/append the value to the dict
            if value not in dict:
                dict[value] = i
        # In case the sum of two elements is not equal the target return an empty list
        return []