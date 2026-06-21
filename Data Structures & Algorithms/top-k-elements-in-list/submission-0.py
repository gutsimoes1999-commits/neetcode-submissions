class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for i in nums:
            freqMap[i] +=1
        freqList = sorted(freqMap.items(), key=lambda item: item[1], reverse = True)
   
        res = []
        for i in range(k):
            res.append(freqList[i][0])
    
        return res

    
