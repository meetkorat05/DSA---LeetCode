class Solution(object):
    def findWordsContaining(self, words, x):
        ans = []
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
        return ans        