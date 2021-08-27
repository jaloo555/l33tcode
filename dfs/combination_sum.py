class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or len(candidates) == 0:
            return []
        
        res = []
        def helper(remain, first, curr):
            nonlocal res
            
            # Base case
            if remain == 0:
                res.append(curr[:])
                return
            elif remain < 0:
                return
            
            # Traverse - First limits the search to exclude precedent number, i to give repeat current selection
            for i in range(first, len(candidates)):
                curr.append(candidates[i])
                # Backtrack
                helper(remain - candidates[i], i, curr)
                curr.pop()
            return
        
        helper(target, 0, [])
        
        
        return res