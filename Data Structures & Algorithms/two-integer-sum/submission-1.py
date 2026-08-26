class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in set:
                return [set[diff], i]
            set[n] = i
        