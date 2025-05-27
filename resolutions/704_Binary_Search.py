class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        answer = 0
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                right = middle - 1
            if nums[middle] < target:
                left = middle + 1
        return -1