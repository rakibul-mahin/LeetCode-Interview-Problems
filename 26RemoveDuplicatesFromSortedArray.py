class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        u = []
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                u.append(nums[i])
                
        u.append(nums[len(nums)-1])
        
        for i in range(len(u)):
            nums[i] = u[i]
            
        return len(u)