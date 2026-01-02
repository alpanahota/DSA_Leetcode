class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):  # Start j from i+1 to avoid duplicate pairs and checking same element
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No such pair found
        