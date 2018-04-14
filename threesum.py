# Build a hash table of all the integers

# Pairwise sums and if it's in the hash table


# sort the nums

# -nums[i] becomes the target

class Solution:
    def threeSum(self, nums):
        n=len(nums)
        # no duplicates
        ans=set()
        nums.sort()
         # edge cases
        if n<3:
            return []
        for i in range(n-2):
            # no duplicates
            if i==0 or nums[i]!=nums[i-1]:
                left=i+1
                right=n-1
                while left<right:
                    sum=nums[i]+nums[left]+nums[right]
                    if sum==0:
                        ans.add((nums[i],nums[left],nums[right]))
                        left+=1
                        right-=1
                    elif sum<0:
                        left+=1
                    else:
                        right-=1
        return list(ans)



