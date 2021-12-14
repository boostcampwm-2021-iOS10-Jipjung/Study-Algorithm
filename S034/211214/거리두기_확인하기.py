from collections import deque

DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))
PARTICIPANT, TABLE, PARTITION = "P", "O", "X"
N, M = 5, 5

def is_point_seperate(place, i, j):
    visited = [[False for _ in range(M)] for _ in range(N)]

    q = deque()
    depth = 0
    visited[i][j] = True
    q.append((i, j, depth))
    while q:
        i, j, depth = q.popleft()
        for di, dj in DIRECTION:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = True
                if place[ni][nj] == PARTICIPANT:
                    return False
                if place[ni][nj] == TABLE and depth == 0:
                    q.append((ni, nj, depth + 1))
    return True

def is_place_seperate(place):
    for i in range(N):
        for j in range(M):
            if place[i][j] == PARTICIPANT and not is_point_seperate(place, i, j):
                return False
    return True

def solution(places):
    answer = list(map(lambda place: 1 if is_place_seperate(place) else 0, places))
    return answer