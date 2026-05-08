class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 1
        if len(nums) != 0: 
            num2 = sorted(nums)
            curr = 1
            for i in range(len(num2)-1):
                if num2[i]+1 == num2[i+1]:
                    curr+=1
                    output = max(output, curr)
                elif num2[i] == num2[i+1]:
                    continue
                else: 
                    output = max(output, curr)
                    curr = 1 
        if len(nums) == 0: 
            return 0
        else: 
            return output
        