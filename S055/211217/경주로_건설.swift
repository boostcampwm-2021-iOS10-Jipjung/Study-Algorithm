import Foundation

struct Node {
    let isStartNode: Bool
    let pos: [Int]
    let prev: Int
    let cost: Int
}

func solution(_ board:[[Int]]) -> Int {
    let directions = [[1,0], [0,1], [-1,0], [0,-1]]
    let temp = board.map { $0.map { _ in -1 } } // -1 = 미방문
    var visited = [temp, temp, temp, temp] // 각 진입방향별로 cost 저장
    var queue = [Node(isStartNode: true, pos: [0, 0], prev: 0, cost: 0)]

    for i in (0..<visited.count) {
        visited[i][0][0] = 0
    }
    
    var answer = Int.max
    while queue.isEmpty == false {
        let node = queue.removeFirst()
        
        if node.pos == [board.count - 1, board.count - 1] {
            if answer > node.cost {
                answer = node.cost
            }
            continue
        }
        
        for (i, dir) in directions.enumerated() {
            let newPos = [node.pos[0] + dir[0], node.pos[1] + dir[1]]
            if isInBoard(newPos, size: board.count) == false {
                continue
            }
            if isBlock(newPos, board: board) {
                continue
            }
            
            let additionalFee = (node.isStartNode || !isNeedToMakeCorner(node.prev, i)) ? 0 : 500
            let fee = additionalFee + 100
            let cost = node.cost + fee
            if visited[i][newPos[0]][newPos[1]] < 0 || visited[i][newPos[0]][newPos[1]] > cost {
                visited[i][newPos[0]][newPos[1]] = cost
                queue.append(Node(isStartNode: false, pos: newPos, prev: i, cost: cost))
            }
        }
    }
    
    return answer
}

func isNeedToMakeCorner(_ prev: Int, _ next: Int) -> Bool {
    return prev != next
}

func isBlock(_ pos: [Int], board: [[Int]]) -> Bool {
    return board[pos[0]][pos[1]] == 1
}

func isGoal(_ pos: [Int], size: Int) -> Bool {
    return (pos[0] == size - 1) && (pos[1] == size - 1)
}

func isInBoard(_ pos: [Int], size: Int) -> Bool {
    return ((0..<size) ~= pos[0]) && ((0..<size) ~= pos[1])
}
