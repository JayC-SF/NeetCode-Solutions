class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = dict()
        for idx, c in enumerate(s):
            if c in sd:
                sd[c] += 1
            else:
                sd[c] = 1
        for idx, c in enumerate(t):
            if c in sd:
                if sd[c] <= 1:
                    del sd[c]
                else:
                    sd[c] -= 1
            else:
                return False
        if len(sd) == 0:
            return True
        else:
            return False
