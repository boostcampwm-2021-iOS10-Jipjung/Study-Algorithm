from collections import deque

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        q = deque(word)
        stack = []
        while q:
            char = q.popleft()
            stack.append(char)
            if ch == char:
                stack.reverse()
                break
        
        return "".join(stack) + "".join(q)