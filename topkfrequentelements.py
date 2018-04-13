# Solution1: sort by frequency+pick top k
# Time complexity: O(nlogn)
# Space complexity: O(n)

# 偷懒的调包方法
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        return [i[0] for i in collections.Counter(nums).most_common(k)]

# 从头开始实现
# use hash tap to store the elements frequency
# scan the array O(n)


# define a bucket, the key is frequency, the value is all the numbers with
# that specific frequency


# define ans
# scan the ans
# bucket insert elements into answer


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for item in nums:
            try:
                counts[item] += 1
            except KeyError:
                counts[item] = 1
        inv_map = {}
        for m, n in counts.items():
            inv_map[n] = inv_map.get(n, [])
            inv_map[n].append(m)
        a=[[s,t] for s,t in sorted(inv_map.items(),reverse = True)]
        ans=[]
        i=0
        while len(ans)<k:
            ans.extend(a[i][1])
            i+=1
        return ans