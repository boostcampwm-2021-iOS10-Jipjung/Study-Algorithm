import heapq

DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))
INF = float("inf")

def is_blocked(board, i, j):
    if board[i][j] == 1:
        return True
    return False

def solution(board):
    answer = 0
    q = []
    N, M = len(board), len(board[0])
    visited = [[[False for i in range(4)] for i in range(M)] for i in range(N)]
    for i in range(4):
        visited[0][0][i] = True
    q.append((0, 0, 0, 0))
    q.append((0, 0, 0, 1))
    while q:
        price, i, j, d = heapq.heappop(q)
        if (i == (N - 1)) and (j == (M - 1)):
            answer = price
            break
            
        reverse_d = (d + 2) % 4
        for dd, (di, dj) in enumerate(DIRECTION):
            nd, ni, nj = dd, i + di, j + dj
            dprice = 100
            if dd == reverse_d:
                continue
            elif dd != d:
                dprice += 500
            nprice = price + dprice
            
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj][nd] and not is_blocked(board, ni, nj):
                visited[i][j][d] = True
                heapq.heappush(q, (nprice, ni, nj, nd))
            
    return answer