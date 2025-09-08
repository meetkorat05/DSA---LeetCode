class Solution(object):
    def firstBadVersion(self, n):
        low = 1
        high = n
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
        