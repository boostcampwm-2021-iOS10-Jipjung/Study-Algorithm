# print(move_doll_to_basket(1, [1]))
def move_doll_to_basket(doll, basket):
    basket.append(doll)
    if len(basket) >= 2 and basket[-2] == basket[-1]:
        basket.pop()
        basket.pop()
        return 2
    return 0

def solution(board, moves):
    answer = 0
    moves = list(map(lambda x: x - 1, moves))
    N, M = len(board), len(board[0])
    basket = []
    for move in moves:
        for i in range(N):
            if board[i][move] == 0:
                continue
            doll = board[i][move]
            board[i][move] = 0
            removed_count = move_doll_to_basket(doll, basket)
            answer += removed_count
            break
    
    return answer