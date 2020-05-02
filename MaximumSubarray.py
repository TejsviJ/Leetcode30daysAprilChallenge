#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a=nums
        max_so_far=a[0] 
        curr_max = a[0] 
      
        for i in range(1,len(a)): 
            curr_max = max(a[i], curr_max + a[i]) 
            max_so_far = max(max_so_far,curr_max) 
          
        return max_so_far 
       
