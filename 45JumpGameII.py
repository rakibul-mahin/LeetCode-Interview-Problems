class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        furthest = 0
        curr = 0

        for i in range(len(nums)-1):
            furthest = max(furthest, nums[i]+i)
            if i == curr:
                curr = furthest
                jumps += 1
        
        return jumps