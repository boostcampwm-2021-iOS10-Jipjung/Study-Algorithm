import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    var leftHand = [3, 0]
    var rightHand = [3, 2]
    
    var dict = [Int: [Int]]()
    var count = 1
    for row in (0..<3) {
        for col in (0..<3) {
            dict[count] = [row, col]
            count += 1
        }
    }
    dict[0] = [3, 1]
    
    return numbers.map { key in
        switch key {
        case 1, 4, 7: // 무조건 왼손
            leftHand = dict[key]!
            return "L"
        case 3, 6, 9: // 무조건 오른손
            rightHand = dict[key]!
            return "R"
        default:
            let pos = dict[key]!
            let left = getDistance(lhs: leftHand, rhs: pos)
            let right = getDistance(lhs: rightHand, rhs: pos)
            
            if left == right {
                if hand == "right" {
                    rightHand = pos
                    return "R"
                } else {
                    leftHand = pos
                    return "L"
                }
            }
            if left > right {
                rightHand = pos
                return "R"
            } else {
                leftHand = pos
                return "L"
            }
        }
    }.joined()
}

func getDistance(lhs: [Int], rhs: [Int]) -> Int {
    return abs(lhs[0] - rhs[0]) + abs(lhs[1] - rhs[1])
}
