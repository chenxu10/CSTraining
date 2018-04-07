class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans=0
        left=0
        # 创建一个hashtable来记录{字符:出现的位置}
        dict={}
        for i in range(len(s)):
            if s[i] in dict and dict[s[i]]>=left:
                left=dict[s[i]]+1
        dict[s[i]]=i
        ans=max(ans,i-left+1)
        return ans

    # 反思：遇到substring问题的模板
    # 第一,一个hashmap或者hashtable储存每个字符的frequency多少
    # 第二,对字符串做遍历