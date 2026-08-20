class Solution(object):
    def reverseBits(self, n):
        result = 0

        for i in xrange(32):
            result = (result << 1) | (n & 1)
            n >>= 1

        return result
