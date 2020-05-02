class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       
        
        while True:
            stones.sort()
            if len(stones)==1:
                return stones[0]
            elif len(stones)==2:
                return stones[1]-stones[0]
            else:
                weight=stones[-1]-stones[-2]
                stones.pop(-1) 
                stones.pop(-1) 
            
            if weight != 0:
                stones.append(weight)
