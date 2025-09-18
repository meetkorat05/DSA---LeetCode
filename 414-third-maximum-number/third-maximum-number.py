class Solution(object):
    def thirdMax(self, nums):
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')

        for n in nums:
            if n in (first,second,third):
                continue 
            if n > first:
                first,second,third = n,first,second
            elif n > second:
                second,third = n,second
            elif n > third:
                third = n

        if third != float('-inf'):
            return third
        else:
            return first
        