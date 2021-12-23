# 7분 짜리 - 쉬움 int() 안해줘서 런타임 에러 1

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split()
        temp_token = 0
        for token in tokens:
            if token.isnumeric():
                if temp_token < int(token):
                    temp_token = int(token)
                else:
                    return False
        return True

print(Solution().areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
