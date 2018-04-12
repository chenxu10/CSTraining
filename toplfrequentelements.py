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


