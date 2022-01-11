# 파이썬의 배열 슬라이싱에 대해서 찾아보게 되었다.

class Solution:
    def reverse_array(self, arr, rear, front):
        length = front - rear + 1
        for i in range(length // 2):
            temp = arr[rear + i]
            arr[rear + i] = arr[front - i]
            arr[front - i] = temp

    def reversePrefix(self, word: str, ch: str) -> str:
        wordList = list(word)
        front = 0
        rear = -1
        length = len(wordList)

        while front < length:
            if wordList[front] == ch:
                self.reverse_array(wordList, rear + 1, front)
                break
            front += 1
        return "".join(wordList)
