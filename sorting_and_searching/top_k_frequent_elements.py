import heapq
import itertools
from collections import Counter
from typing import List


class SolutionHeap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


class SolutionBucketSort:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        flat_list = list(itertools.chain(*buckets))
        return flat_list[::-1][:k]
