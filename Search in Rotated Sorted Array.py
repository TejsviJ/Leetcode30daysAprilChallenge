class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        if target not in nums or not nums:
            return -1
        elif len(nums)==1:
            return 0
        elif nums[0]==target:
            return 0
        elif nums[len(nums)-1]== target:
            return (len(nums)-1)
        pivotNo=nums[0]
        nums.sort()
        pivotIndex=nums.index(pivotNo)
        
        b=0
        e=len(nums)-1
        m=int((b+e)/2)
      
        
             
        while True:
            if target == nums[m]:
            
                l=m
                break
            elif target>nums[m]:
                b=m+1
                m=int((b+e)/2)
            else:
                e=m-1
                m=int((b+e)/2)
        print (l, pivotIndex)
        
        if l<pivotIndex:
            l=len(nums)-(pivotIndex-l)
            return l
        else:
            l=l-pivotIndex
            return l
        
