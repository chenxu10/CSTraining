# Method1: Brute Force Method
class Solution:
    def mySqrt(self, x):
        if x <= 1: return x
        s = 1
        while True:
            if s*s > x: return s - 1
            s += 1
        return -1



# Method2: Binary Search Method
class Solution:
    def mySqrt(self, x):
        left=1
        right=x
        while left<=right:
            middle=left+(right-left)//2
            if middle*middle>x:
                right=middle-1
            else:
                left=middle+1
        return right


# Method3: Newton Method
class Solution:
    def mySqrt(self, x):
        a=x
        while a*a>x:
            a=(a+x//a)//2
        return a

