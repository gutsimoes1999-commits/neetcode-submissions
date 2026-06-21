class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if self.getCount(s) == self.getCount(t):
            return True
        return False
    


    def getCount(self, word: str):
        counter = {}
        for i in word:
            counter[i] = counter.get(i, 0) + 1
        
        return counter;


