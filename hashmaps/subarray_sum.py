class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        count = 0
        running_sum = 0
        
        # Sum: # of occurrences
        occurence = {}
        occurence[0] = 1
        
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum - k in occurence:
                count += occurence[running_sum - k]
            
            if running_sum in occurence:
                occurence[running_sum] += 1
            else:
                occurence[running_sum] = 1
        
        return count
    
"""
Above is the specific problem that can be solved by two pinters. Now let's generalize the characteristics of the problems that can be solved by two pinters. The summary is simple:

If a wider scope of the sliding window is valid, the narrower scope of that wider scope is valid mush hold.
If a narrower scope of the sliding window is invalid, the wider scope of that narrower scope is invalid mush hold.
With 2 rules above hold, we are able to optimize the brute-force solution to two pointers solution.

I just show you what kind of question can be solved by two pointers by using some very simple Induction Reasoning. Now let me show you why this problem cannot be solved by two pointers. Like I said, If this problem doesn't meet the creteria that two pointer technique, it cannot be solved with two pointers.

In this specific problem, rule 1 doesn't hold, because I can find a specific case such that it doesn't hold, e.g., if K is 3, 1,1,1 sum is 3, so 1,1,1, is valid, but 1,1 sum is 2 which means 1,1 is invalid, so rule 1 breaks.

Rule2 doesn't hold, either, because I can find a specific case such that it doesn't hold, e.g., if K is 2, 1,1,1 sum is 3, so 1,1,1, is invalid, but 1,1,1,-1 sum is 2 which means 1,1,1,-1 is valid, so rule 2 breaks.
"""