class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[]] * len(nums)
        counter = defaultdict(0)
        for v in nums:
            counter[v] += 1
        for k,v in couter.items():
            counts[v].append(v)
        result = []
        for l in counts[::-1]:
            