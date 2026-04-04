class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(len(nums)):
            values[nums[i]] = i
        
        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in values and values[curr] != i: 
                return [i, values[curr]]
        
        return [] 