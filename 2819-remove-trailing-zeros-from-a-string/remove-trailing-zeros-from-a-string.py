class Solution(object):
    def removeTrailingZeros(self, num):
        i = len(num) - 1
        while i>=0 and num[i]=='0':
            i = i - 1
        return num[:i+1]    

        