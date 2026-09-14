class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        if len(nums)%2==0:
            x = (nums[mid]+nums[mid+1])/2
            return x
        else:
            return nums[mid]