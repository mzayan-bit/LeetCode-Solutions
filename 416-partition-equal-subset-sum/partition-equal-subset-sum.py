from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        
        total = 0
        for i in range(length):
            total += nums[i]
        if total % 2 != 0:
            return False
        
        half = total // 2
        dp = [False] * (half + 1)
        dp[0] = True   
        
        for num in nums:
            for t in range(half, num - 1, -1):
                if dp[t - num]:
                    dp[t] = True
        
        return dp[half]