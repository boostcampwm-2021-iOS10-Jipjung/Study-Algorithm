class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        remains = [[] for i in range(3)]
        for stone in stones:
            if stone % 3 == 0:
                remains[0].append(stone)
            elif stone % 3 == 1:
                remains[1].append(stone)
            else:
                remains[2].append(stone)
        turn = False
        left_count = len(stones)
        total_remain = 0
        while True:
            for i in range(3):
                if i + total_remain == 3:
                    continue
                if len(remains[i]) > 0:
                    remains[i].pop()
                    total_remain = (total_remain + i) % 3
                    left_count -= 1
                    if left_count == 0:
                        return False
                    break
            else:
                break
            turn = not turn
        print(remains)
        return turn
            