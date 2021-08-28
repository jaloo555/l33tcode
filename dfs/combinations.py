class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(first = 1, curr = []):
            nonlocal res
            
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(first, n+1): 
                curr.append(i)
                helper(i+1, curr)
                curr.pop()
                
        
        helper()
        return res