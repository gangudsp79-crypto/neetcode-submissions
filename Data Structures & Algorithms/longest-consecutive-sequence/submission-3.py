class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        for i in range(len(nums)):
            if nums[i]-1 not in s:
                current=nums[i]
                count=0

                while current in s:
                    current+=1
                    count+=1
                longest=max(longest,count)
        return longest
            

                    

        

        
        