class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        d=['U']*(len(nums)-1)
        d.append('G')
        if nums[0]>=len(nums)-1:
            return True
    
        for i in range(len(nums)-2,-1,-1):
            if nums[i]==0:
                d[i]='B'
                continue
                
            if i+nums[i]>=len(nums)-1 or 'G' in d[i:i+nums[i]+1] :
                d[i]='G'
            else: 
                d[i]='B'
      
        if d[0]=='G':
            return True
        else: 
            return False
