class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        left_letter_count = 0
        for char in s:
            if char == letter:
                left_letter_count += 1
        stack = []
        stack_letter_count = 0
        
        for i, char in enumerate(s):
            while stack and stack[-1] > char and (left_letter_count > repetition - stack_letter_count or stack[-1] != letter) and len(stack) + len(s) - i > k:
                pop_word = stack.pop()
                if letter == pop_word:
                    stack_letter_count -= 1
                
            if len(stack) < k:
                if char == letter:
                    stack.append(char)
                    stack_letter_count += 1
                elif k - len(stack) > repetition - stack_letter_count:
                    stack.append(char)
            
            if char == letter:
                left_letter_count -= 1
            
        return "".join(stack)