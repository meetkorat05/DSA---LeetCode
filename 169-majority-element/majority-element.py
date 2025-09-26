class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for key in freq.keys():
            if freq[key] > n//2:
                return key