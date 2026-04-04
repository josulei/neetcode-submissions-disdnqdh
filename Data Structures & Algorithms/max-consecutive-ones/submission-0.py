class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currMax = 0
        maxOnes = 0
        for i in nums: 
            if i != 1: 
                maxOnes = max(maxOnes, currMax)
                currMax = 0
            else: 
                currMax +=1 

        return max(maxOnes, currMax)
        