class Solution:
    def is_palindrom(self, collection):
        i = 0
        j = len(collection) - 1
        while i < j:
            if collection[i] != collection[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def find_subseqs(self, s):
        n = len(s)
        subseqs = []
        for i in range(1, 1 << n):
            temp = ""
            for j in range(n):
                if (i >> j) & 1 == 0:
                    continue
                temp += s[j]
            if self.is_palindrom(temp):
                subseqs.append(i)
        return subseqs
    
    def count_one(self, s):
        one = 0
        while s > 0:
            if s & 1:
                one += 1
            s = (s >> 1)
        return one
    
    def maxProduct(self, s: str) -> int:
        subseqs = self.find_subseqs(s)
        answer = 0
        for seq1 in subseqs:
            for seq2 in subseqs:
                if seq1 & seq2:
                    continue
                answer = max(answer, self.count_one(seq1) * self.count_one(seq2))
        return answer