class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        a = {}
        b = {}

        for x, y in zip(s, t):
            if x in a and a[x] != y:
                return False
            if y in b and b[y] != x:
                return False

            a[x] = y
            b[y] = x

        return True
