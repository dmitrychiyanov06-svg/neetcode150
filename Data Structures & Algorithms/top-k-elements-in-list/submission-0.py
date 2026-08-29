class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        res = []
        for x in nums:
            ans[x] = ans.get(x, 0) + 1
        freq = sorted(list(ans.items()), key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(freq[i][0])
            
        return res