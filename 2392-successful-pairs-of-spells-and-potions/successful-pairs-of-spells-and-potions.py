class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        ans = []
        m = len(potions)

        for spell in spells:
            min_needed = (success + spell - 1) // spell

            low = 0 
            high = m - 1
            idx = m
            while low <= high:
                mid = (low + high) // 2
                if potions[mid] >= min_needed:
                    idx = mid
                    high = mid - 1
                else:
                    low = mid + 1

            ans.append(m - idx)
        return ans

          
