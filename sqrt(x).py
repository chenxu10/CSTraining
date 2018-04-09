# Method1: Brute Force Method
class Solution:
    def mySqrt(self, x):
        if x <= 1: return x
        s = 1
        while True:
            if s*s > x: return s - 1
            s += 1
        return -1