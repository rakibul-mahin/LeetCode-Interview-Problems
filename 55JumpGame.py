class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = 0
        for i in range(0, len(nums)):
            if i > r:
                return False
            r = max(r, nums[i]+i)
        return True