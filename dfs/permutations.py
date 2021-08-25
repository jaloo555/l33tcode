class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums or len(nums) == 0:
            return []
        
        res = []
        
        # For each idx, loop through all possible places to add
        def helper(nums, idx, curr):
            if len(curr) == len(nums):
                res.append(list(curr))
                return
            
            for i in range(idx, len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    helper(nums, idx + 1, curr)
                    curr.pop()
            return
        
        # Swapping method (at each idx, swap curr with an index > idx)
        def helper2(nums, idx):
            if idx == len(nums):
                res.append(list(nums))
                return
            
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                helper2(nums, idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]
        
        helper2(nums, 0)
        return res
    