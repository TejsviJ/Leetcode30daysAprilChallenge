#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return s.pop()
                
