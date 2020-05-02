class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        a=nums
        cs=0
        ml=0
        d={}
        n=len(a)
        a= [ (-1) if i==0 else i for i in a ]
        
        for i in range(len(a)):
            cs+=a[i]
        
            if cs ==0:
                ml=i+1
                
            if cs in d:
                
                if ml<i-d[cs]:
                    ml=i-d[cs]
                    
            else:
                d[cs]=i
                
        return ml
