class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        s = 0
        n = 0
        for i in nums:
            s += i
            if s == k:
                n += 1
            if (s - k) in d:
                n += d[s - k]
            d[s] += 1
      
        return n
   
