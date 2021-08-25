class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or len(candidates) == 0:
            return []
        
        res = []
        def helper(candidates, target, currSum, curr, start):
            nonlocal res
            
            if currSum == target:
                res.append(list(curr))
                return 
            elif currSum > target:
                return
                
            # Limiting to start -> len is to remove precedent numbers that have already been explored
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                helper(candidates, target, currSum + candidates[i], curr, i)
                curr.pop()
        
        helper(candidates, target, 0, [], 0)
        
        
        return res