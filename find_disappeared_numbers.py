class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        for num in nums:
            index = abs(num) - 1

            if nums[index] > 0:
                nums[index] = -nums[index]

        result = []

        for i in xrange(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result
