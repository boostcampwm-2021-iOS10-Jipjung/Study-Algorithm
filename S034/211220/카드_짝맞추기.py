from itertools import permutations
from collections import deque

DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))

def get_card_orders(cards):
    card_count = len(cards)
    permutation_cards = list(permutations(cards, card_count))
    card_orders = []
    temp = []
    def dfs(permutation_card, i):
        if i == card_count:
            card_orders.append(temp[:])
            return
        for j in range(2):
            temp.append((permutation_card[i], j))
            temp.append((permutation_card[i], (j + 1) % 2))
            dfs(permutation_card, i + 1)
            temp.pop()
            temp.pop()
    for permutation_card in permutation_cards:
        dfs(permutation_card, 0)
    return card_orders

def bfs_card_order(card_dict, card_order, board, r, c, N):
    # print((card_dict, card_order, board, r, c, N))
    q = deque()
    q.append((r, c, 0, 1))
    answer = 0
    visited = [[[[False for i in range(4)] for i in range(len(card_order) + 1)] for i in range(N)] for i in range(N)]
    # visited = [[[False for i in range(4)] for i in range(N)] for i in range(N)]
    
    for index, (card_id, card_number) in enumerate(card_order):
        i, j = card_dict[card_id][card_number]
        board[i][j] = index + 1
    # print(board)
    # print(card_dict, card_order)
    while q:
        # print(q)
        i, j, depth, current_card_idx = q.popleft()
        if board[i][j] == current_card_idx:
            current_card_idx += 1
            depth += 1
        if current_card_idx > len(card_order):
            answer = depth
            break
            
        for dd, (di, dj) in enumerate(DIRECTION):
            ni, nj = i + di, j + dj
            
            # index over
            if (0 > ni) or (ni >= N) or (0 > nj) or (nj >= N):
                continue
            # visited
            if visited[ni][nj][current_card_idx][dd]:
                continue
            visited[ni][nj][current_card_idx][dd] = True
            q.append((ni, nj, depth + 1, current_card_idx))
            while True:
                # index over
                ni, nj = ni + di, nj + dj
                if (0 > ni) or (ni >= N) or (0 > nj) or (nj >= N):
                    ni -= di
                    nj -= dj
                    if (ni != i + di) or (nj != j + dj): 
                        q.append((ni, nj, depth + 1, current_card_idx))
                    break
                # visited
                if board[ni][nj] >= current_card_idx:
                    if (ni != i + di) or (nj != j + dj): 
                        q.append((ni, nj, depth + 1, current_card_idx))
                    break 
            
    return answer        
def solution(board, r, c):
    answer = 2
    N = len(board)
    card_dict = {}
    for i in range(N):
        for j in range(N):
            card = board[i][j]
            if card == 0:
                continue
            if card in card_dict:
                card_dict[card].append((i, j))
            else:
                card_dict[card] = [(i, j)]
    cards, card_count = list(card_dict), len(card_dict)

    answer = 100000000
    for card_order in get_card_orders(cards):
        
        result = bfs_card_order(card_dict, card_order, board, r, c, N)
        answer = min(answer, result)
    return answer