class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)

        for length in xrange(1, n // 2 + 1):
            if n % length != 0:
                continue

            pattern = s[:length]

            if pattern * (n // length) == s:
                return True

        return False
