"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum_vals = set()
        nums.sort()
        target = 0
        new_k = []


        for i in range(len(nums) - 1):
            left = 0
            right = len(nums) - 1
            while left < i and i < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if  current_sum == target:
                    if (nums[left], nums[i], nums[right]) not in sum_vals:
                         sum_vals.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                  # print(sum_vals)
                elif current_sum < target: 
                    left += 1
                elif current_sum > target: 
                    right -= 1
                    

        for elem in sum_vals:
            if elem not in new_k:
                new_k.append(elem)
        sum_vals = new_k
        return sum_vals