class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for idx, v in enumerate(nums):
            d[v] = idx
        for idx, v in enumerate(nums):
            sF = target - v
            if sF in d and idx != d[sF]:
                return [idx, d[sF]]
