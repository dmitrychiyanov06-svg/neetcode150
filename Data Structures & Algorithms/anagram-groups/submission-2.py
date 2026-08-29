class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for x in strs:
            count = [0] * 26
            for ch in x:
                count[ord(ch) - ord('a')] += 1
            ans[tuple(count)].append(x)
        return list(ans.values())