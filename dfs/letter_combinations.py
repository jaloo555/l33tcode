class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        res = []
        
        if not digits or len(digits) == 0:
            return []
        
        def helper(digits,idx, curr):
            nonlocal res, letters
            
            # Base case
            if idx == len(digits):
                res.append(curr)
                return 
            
            # Traverse
            for ch in letters[digits[idx]]:
                curr += ch
                helper(digits,idx+1,curr)
                curr = curr[:-1]
        
        helper(digits, 0, "")
        
        return res