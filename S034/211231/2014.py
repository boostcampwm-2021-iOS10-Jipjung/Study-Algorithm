from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # cands = list("".join(char * (count // k) for char, count in Counter(s).items()))
        cands = [char for char, count in Counter(s).items() if count >= k]
        cands.sort()
        
        def is_repeated(seq):
            count = 0
            i = 0
            n = len(seq)
            for char in s:
                if seq[i] == char:
                    i += 1
                if i == n:
                    count += 1
                    i = 0
                if count == k:
                    return True
            return False
        
        q = deque([""])
        answer = ""
        while q:
            sub_seq = q.popleft()
            for cand in cands:
                new_sub_seq = sub_seq + cand
                if is_repeated(new_sub_seq):
                    q.append(new_sub_seq)
                    answer = new_sub_seq
        return answer