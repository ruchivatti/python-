class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last = {}
        left = 0
        answer = 0

        for right in xrange(len(s)):
            ch = s[right]

            if ch in last and last[ch] >= left:
                left = last[ch] + 1

            last[ch] = right
            answer = max(answer, right - left + 1)

        return answer
