class Solution(object):
    def minimumOperations(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] % 3 == 0:
                i += 1
            elif nums[i] > 3:
                nums[i] = nums[i] - 1
                count += 1
            else:
                nums[i] = nums[i] + 1
                count += 1
        return count                   
        