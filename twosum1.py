# How you think of this problem
'''
复习完了Hash表以后突然想到新创一个Hash表，然后每判断完一次
就扔进HashTable中去
'''



# Brute Force Solution
# Two threads
class Solution(object):
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target-nums[j]= nums[i]:
                    return [i,j]

# Hash Table I
class Solution(object):
    def twoSum(self,nums,target):
        dict={}
         for i,num in enumerate(nums):
            dict[num]=i

         for i,num in enumerate(nums):
             if target-num in dict and dict[target-num]!=i:
                 return [i,dict[target-num]]


# Hash Table II
class Solution(object):
    def twoSum(self,nums,target):
         for i,num in enumerate(nums):
             if target-num in dict:
                 return [i,dict[target-num]]
             else:
                 dict[num]=i
# 反思
# 想清楚用哪个数据结构，为什么用？它有什么好处？
# Hash表要求的未知量