class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1] * len(nums), [1] * len(nums)
        pref, suff = 1, 1
        output = []
        for i in range(len(nums)):
            if i != 0:
                pref *= nums[i - 1]
            prefix[i] = pref
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                suff *= nums[i + 1]
            suffix[i] = suff
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])

        return output