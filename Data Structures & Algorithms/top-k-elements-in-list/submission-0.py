class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        freq=[]
        for i in range(len(nums)+1):
            freq.append([])
        
        for num in nums:
            dict[num]=1+dict.get(num,0)
        for n,c in dict.items():
            freq[c].append(n)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res