class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        return self.helperSearch(nums, target, 0, len(nums)-1)


    def helperSearch(self, nums, target, left, right):
        if left > right:
            return -1
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return self.helperSearch(nums, target, left, middle - 1)
        else:
            return self.helperSearch(nums, target, middle + 1, right)