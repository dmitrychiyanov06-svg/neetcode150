class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sd = dict()
            td = dict()
            for i in range(len(s)):
                sd[s[i]] = sd.get(s[i], 0) + 1
                td[t[i]] = td.get(t[i], 0) + 1
            return sd == td
        return False

