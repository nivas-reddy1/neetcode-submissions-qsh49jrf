class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMaP = {} # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMaP:
                return [prevMaP[diff], i]
            prevMaP[n] = i