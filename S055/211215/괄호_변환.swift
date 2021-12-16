import Foundation

func solution(_ p:String) -> String {
    let arr = p.map { String($0) }

    return convertCorrect(arr).joined()
}

func convertCorrect(_ s: [String]) -> [String] {
    if s.isEmpty {
        return []
    }
    
    var prefix = [String]()
    var suffix = [String]()
    for i in (2...s.count) {
        prefix = Array(s.prefix(i))
        
        if isBalance(prefix) {
            suffix = Array(s.suffix(s.count - i))
            break
        }
    }
    
    if isCorrect(prefix) {
        return prefix + convertCorrect(suffix)
    } else {
        let temp = Array(prefix[1..<prefix.count - 1])
        return ["("] + convertCorrect(suffix) + [")"] + reverseBracket(temp)
    }
}

func reverseBracket(_ s: [String]) -> [String] {
    return s.map { $0 == "(" ? ")" : "(" }
}

func isCorrect(_ s: [String]) -> Bool {
    guard isBalance(s) else {
        return false
    }
    
    var count = 0
    for element in s {
        count += ("(" == element ? 1 : -1)

        if count < 0 {
            return false
        }
    }
    
    return count == 0
}

func isBalance(_ s: [String]) -> Bool {
    var count = 0
    s.forEach {
        if $0 == "(" {
            count += 1
        }
    }
    
    return count == s.count - count
}

/*
 
let ps = [
    "(()())()",
    ")(",
    "()))((()"
]

let answers = [
    "(()())()",
    "()",
    "()(())()"
]

zip(ps, answers).forEach {
    let result = solution($0)
    if result != $1 {
        print("source: \($0), expected: \($1), result: \(result)")
    }
}

*/
