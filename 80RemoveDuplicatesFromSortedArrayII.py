class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        ind = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
                nums[ind] =  nums[i]
                ind += 1
                c += 1
            elif d[nums[i]] <= 1:
                d[nums[i]] += 1
                nums[ind] = nums[i]
                ind += 1
                c += 1
        return c