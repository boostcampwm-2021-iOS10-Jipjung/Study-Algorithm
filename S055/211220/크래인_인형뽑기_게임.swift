import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var stack = [Int]()
    var board = board
    var answer = 0
    moves.forEach { number in
        for i in (0..<board.count) {
            let item = board[i][number - 1]
            if item != 0 {
                if let last = stack.last {
                    if last == item {
                        stack.removeLast()
                        answer += 2
                    } else {
                        stack.append(item)
                    }
                } else {
                    stack.append(item)
                }
                
                board[i][number - 1] = 0
                break
            }
        }
    }
    
    return answer
}
