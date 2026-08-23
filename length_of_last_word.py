class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()

        length = 0

        for i in xrange(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break

            length += 1

        return length
