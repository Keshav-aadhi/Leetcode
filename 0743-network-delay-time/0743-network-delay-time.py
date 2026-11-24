class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges = {i: [] for i in range(1, n+1)}
        for i in times:
            edges[i[0]].append((i[1], i[2]))
        heap = [(0,k)]
        visited = set()
        delays = 0
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            delays = max(time, delays)
            for nei in edges[node]:
                if nei not in visited:
                    heapq.heappush(heap, (time+nei[1], nei[0]))
        return delays if len(visited) == n else -1