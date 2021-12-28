class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rotate_board = [["" for _ in range(len(board))] for _ in range(len(board[0]))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                rotate_board[j][i] = board[i][j]
        
        for _board in (board, rotate_board):
            row_strings = ["".join(row) for row in _board]
            for row_string in row_strings:
                for block in row_string.split("#"):
                    if self.is_block_can_make_word(block, word):
                        return True
        
        # print("#### ### ####".split("#"))
        return False
                    
    def is_block_can_make_word(self, block, word):
        if len(block) != len(word):
            return False
        
        is_forward = True
        for i in range(len(block)):
            if block[i] == word[i] or block[i] == " ":
                is_forward = True
            else:
                is_forward = False
                break
        
        is_reverse = True
        for i in range(len(block)):
            if block[len(block) - i - 1] == word[i] or block[len(block) - i - 1] == " ":
                is_reverse = True
            else:
                is_reverse = False
                break
                
        return is_forward or is_reverse