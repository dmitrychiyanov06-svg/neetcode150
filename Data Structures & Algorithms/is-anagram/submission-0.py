class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = set(s)
        ts = set(t)
        if ss == ts:
            sd = dict()
            td = dict()
            for x in ss:
                sd[x] = s.count(x)
            for y in ts:
                td[y] = t.count(y)
            return(sd == td)
        return False

