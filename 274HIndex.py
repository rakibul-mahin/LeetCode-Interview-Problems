class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        n = len(citations)
        hi = 0

        for i in range(n):
            if citations[i] < n - i:
                h = citations[i]
            else:
                hi = max(hi, n-i)
        return hi