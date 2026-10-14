class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)

        max_heap = [-c for c in Counter(tasks).values()]
        heapq.heapify(max_heap)
        cooldown_queue = deque()
        time = 0
        
        while max_heap or cooldown_queue:
            time += 1

            if max_heap:
                count = abs(heapq.heappop(max_heap)) - 1
                if count > 0:
                    cooldown_queue.append((count, time + n))
            
            if cooldown_queue and cooldown_queue[0][1] == time:
                heapq.heappush(max_heap, -cooldown_queue.popleft()[0])

        return time
                
