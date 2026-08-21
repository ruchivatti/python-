class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        product = 1
        for i in xrange(n):
            result[i] = product
            product *= nums[i]

        product = 1
        for i in xrange(n - 1, -1, -1):
            result[i] *= product
            product *= nums[i]

        return result
