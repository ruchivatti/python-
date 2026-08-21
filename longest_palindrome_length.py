class Solution(object):
    def longestPalindrome(self, s):
        count = {}
        answer = 0
        has_odd = False

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for value in count.values():
            answer += (value // 2) * 2

            if value % 2 == 1:
                has_odd = True

        if has_odd:
            answer += 1

        return answer
