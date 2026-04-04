class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        return self.helperSearch(nums, target, 0, len(nums)-1)


    def helperSearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        middle = (right + left) // 2
        if left > right:
            return -1
        if nums[middle] == target:
            return middle
        if nums[middle] > target:
            return self.helperSearch(nums, target, left, middle-1)
        elif nums[middle] < target:
            return self.helperSearch(nums, target, middle+1, right)
            