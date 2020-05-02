class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=0
        p=prices
        n=len(p)
        i=0
        if n==1:
            return 0
        while i<n-1 :
            while i<n-1 and p[i]>p[i+1]:
                i+=1
            if i==n-1:
                break
            buy = p[i] 
            i += 1
                        
            while ((i < n) and (p[i] >= p[i - 1])): 
                i += 1
            sell = p[i - 1]
            
            mp+=sell-buy
        return mp
            
