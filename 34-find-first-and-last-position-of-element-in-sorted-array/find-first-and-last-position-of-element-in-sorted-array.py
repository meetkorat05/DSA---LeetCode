class Solution(object):
    def searchRange(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                left = mid
                right = mid
                while left > 0 and nums[left-1] == target:
                    left = left - 1
                while right < len(nums) - 1 and nums[right+1] == target:
                    right = right + 1
                return [left,right]           
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1        
        return [-1,-1]