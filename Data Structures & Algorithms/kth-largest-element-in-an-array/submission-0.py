class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            elif min_heap[0] < n:
                heapq.heappushpop(min_heap, n)
        return min_heap[0]