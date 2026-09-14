class Solution:
    def hasDuplicate(self, nums):
        s=set()
        nums.sort()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
        