import heapq

Inf = float("inf")
class Solution:
    def secondMinimum(self, n: int, edges, time: int, change: int) -> int:
        visited = [[Inf for _ in range(2)] for _ in range(n + 1)]
        edges_dict = {}
        for a, b in edges:
            if a in edges_dict:
                edges_dict[a].append(b)
            else:
                edges_dict[a] = [b]
            if b in edges_dict:
                edges_dict[b].append(a)
            else:
                edges_dict[b] = [a]
        
        q = []
        q.append((1, 0))
        answer = 0
        while q:
            here, prev_time = heapq.heappop(q)
            if here == n and visited[n][0] < prev_time:
                answer = prev_time
                break
            prev_time = self._stop_time(prev_time, change)
            
            if visited[here][0] > prev_time:
                visited[here][0] = prev_time
            elif visited[here][1] > prev_time:
                visited[here][1] = prev_time
            else:
                continue
            next_time = time + prev_time
            
            for there in edges_dict[here]:
                heapq.heappush(q, (there, next_time))
        return answer
    def _stop_time(self, time, change):
        cycle = time // change
        if (cycle) % 2 == 0:
            return time
        remain_time = time % change
        rest_time = change - remain_time
        return time + rest_time
print(Solution().secondMinimum(5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5))
print(Solution().secondMinimum(2,
[[1,2]],
3,
2))
print(Solution()._stop_time(3,5))
print(Solution()._stop_time(6,5))
print(Solution()._stop_time(946,183))
print(Solution()._stop_time(2044,183))
print(Solution()._stop_time(7672,172))