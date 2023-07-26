class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        t = d[nums[0]]
        val = nums[0]
        for k, v in d.items():
            if v > t:
                t = v
                val = k
        return val