class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        positions = {}

        for i in xrange(len(nums)):
            if nums[i] in positions:
                if i - positions[nums[i]] <= k:
                    return True

            positions[nums[i]] = i

        return False
