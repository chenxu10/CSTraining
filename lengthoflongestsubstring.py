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

    # 我是怎么想到的：昨天学了hash，后来看了Java的双指针版本，后来就开始想到了python的
    # 这个解法，但是在max这里卡住了，卡主是因为丧失了对问题本身的attention,忘记了答案每次
    # 都要迭代