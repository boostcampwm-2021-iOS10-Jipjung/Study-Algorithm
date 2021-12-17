# from collections import Counter
# def solution(N, stages):
#     answer = [0] * (N+1)
#     user = len(stages)
#     counter = Counter(stages)
#     for i in range(1, N+1):
#         if user == 0:
#             break
#         answer[i] = counter[i] / user
#         user -= counter[i]

#     answer = sorted(range(1,N+1), key=lambda x:answer[x], reverse=True)
#     return answer

def solution(N, stages):
    # [확률]
    answer = [0 for _ in range(N)]
    stages = sorted(stages)

    i = 0
    for n in range(1, N + 1):
        count = 0
        while i < len(stages) and stages[i] <= n:
            i += 1
            count += 1
        if len(stages) - (i - count) == 0:
            answer[n - 1] = 0
        else:
            answer[n - 1] = count / (len(stages) - (i - count))

    return list(map(lambda x: x[0] + 1, sorted(enumerate(answer), key = lambda x: (- x[1], x[0]))))