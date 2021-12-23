from collections import deque

Inf = float("inf")
class Solution:
    def secondMinimum(self, n: int, edges, time: int, change: int) -> int:
        visited = [[False for _ in range(2)] for _ in range(n + 1)]
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

        visited[1][0] = True       
        
        q = deque()
        q.append((1, 0))
        answer = []
        while q:
            here, prev_time = q.popleft()
            if here == n:
                answer.append(prev_time)
            prev_time = self._stop_time(prev_time, change)
            next_time = time + prev_time
            for there in edges_dict[here]:
                if not visited[there][0]:
                    visited[there][0] = True
                    q.append((there, next_time))
                    continue
                if not visited[there][1]:
                    visited[there][1] = True
                    q.append((there, next_time))
                    continue
        # print(here)
        print(answer)
        print(visited)
        return sorted(answer)[1]
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