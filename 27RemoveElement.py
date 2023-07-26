class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        c = 0
        for j in nums:
            if j != val:
                nums[i] = j
                i += 1
                c+=1
            
        return c