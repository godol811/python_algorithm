class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def twoSum(nums: list[int], i: int, res: list[list[int]]):
            lo, hi = i + 1, len(nums) - 1

            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]

                if sum < 0:
                    lo += 1
                elif sum > 0:
                    hi -= 1
                else:
                    res.append(nums[i], nums[lo], nums[hi])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(nums, i, res)
        return res
