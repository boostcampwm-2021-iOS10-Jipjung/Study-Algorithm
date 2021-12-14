import Foundation

typealias Position = (y: Int, x: Int)

func solution(_ places:[[String]]) -> [Int] {
    let places = places.map {
        $0.map { row in
            row.map { character in
                String(character)
            }
        }
    }
    
    var answer = [Int]()
    for place in places {
        let result = isComplyRegulation(map: place) ? 1 : 0
        answer.append(result)
    }
    
    return answer
}

func isComplyRegulation(map: [[String]]) -> Bool {
    var students = [Position]()
    for row in (0..<map.count) {
        for col in (0..<map.count) {
            let newPos = Position(row, col)
            if isStudent(pos: newPos, map: map) {
                students.append(newPos)
            }
        }
    }
    
    for student in students {
        if searchStudent(from: student, map: map) {
            return false
        }
    }
    
    return true
}

func isBlocked(pos: Position, map: [[String]]) -> Bool {
    return map[pos.y][pos.x] == "X"
}

func isStudent(pos: Position, map: [[String]]) -> Bool {
    return map[pos.y][pos.x] == "P"
}

func getDistance(lhs: Position, rhs: Position) -> Int {
    return abs(lhs.y - rhs.y) + abs(lhs.x - rhs.x)
}

func searchStudent(from origin: Position, map: [[String]]) -> Bool {
    var visited = [[Bool]](repeating: [Bool](repeating: false, count: 5), count: 5)
    var stack = [Position]()
    let direction: [Position] = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    stack.append(origin)

    while stack.isEmpty == false {
        let pos = stack.removeFirst()
        visited[pos.y][pos.x] = true

        if getDistance(lhs: origin, rhs: pos) >= 2 {
            continue
        }

        for element in direction {
            let newPos = Position(pos.y + element.y, pos.x + element.x)
            guard 0..<5 ~= newPos.y && 0..<5 ~= newPos.x else {
                continue
            }

            if isBlocked(pos: newPos, map: map) {
                continue
            }
            
            if visited[newPos.y][newPos.x] {
                continue
            }
            
            if isStudent(pos: newPos, map: map) {
                return true
            }
            
            stack.append(newPos)
        }
    }
    
    return false
}
