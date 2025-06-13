class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [ [] for _ in range(len(nums)) ]
        counter = defaultdict(int)
        for v in nums:
            counter[v] += 1
        for key,value in counter.items():
            counts[value -1].append(key)
        result = []
        for l in counts[::-1]:
            result.extend(l)
        return result[:k]