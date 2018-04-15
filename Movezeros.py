# The problem belongs to the category of "Array Transformation"

# Two problems are mutually exclusive

# Solve the individual sub problems

# Combine them for the final solution

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[zero]=nums[zero],nums[i]
                zero+=1