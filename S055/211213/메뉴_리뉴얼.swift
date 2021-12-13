//
//  main.swift
//  codingTest
//
//  Created by turu on 2021/12/09.
//

import Foundation

func makeCandidate(order: String) -> Set<String> {
    let order = order.map { String($0) }
    var candidate = Set<String>()
    var result = [String]()
    
    func combiDFS(phase: Int, startIndex: Int, result: [String]) {
        var result = result
        if phase == result.count {
            return
        } else {
            for i in (startIndex..<order.count) {
                result[phase] = order[i]
                candidate.insert(result.sorted().joined())
                combiDFS(phase: phase + 1, startIndex: i + 1, result: result)
            }
        }
    }

    result = [String](repeating: "", count: order.count + 1)
    combiDFS(phase: 0, startIndex: 0, result: result)
    
    return candidate
}

func solution(_ orders:[String], _ course:[Int]) -> [String] {
    var answer = [String: Int]()
    for element in orders {
        makeCandidate(order: element).forEach { candidate in
            if let count = answer[candidate] {
                answer.updateValue(count + 1, forKey: candidate)
            } else {
                answer[candidate] = 1
            }
        }
    }
    
    let over1 = answer.filter{ course.contains($0.key.count)}
        .filter { $0.value > 1 && $0.key.count > 1} // 반복횟수 2회 이상

    var words = [[(String, Int)]](repeating: [], count: 10)
    over1.forEach {
        words[$0.key.count].append(($0.key, $0.value)) // 글자 길이별로 분리
    }

    var ans = [String]()
    for size in (0..<words.count) { // 반복횟수가 높은 순으로 정렬
        words[size].sort { $0.1 > $1.1 }
        if let firstItem = words[size].first {
            for element in words[size] {
                if element.1 >= firstItem.1 { // 같은 반복숫자만 자르기
                    ans.append(element.0)
                } else {
                    break
                }
            }
        }
    }

    return ans.sorted()
}

let sol1 = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) // ["AC", "ACDE", "BCFG", "CDE"]
print(sol1)

let sol2 = solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]) // ["ACD", "AD", "ADE", "CD", "XYZ"]
print(sol2)

let sol3 = solution(["XYZ", "XWY", "WXA"], [2,3,4]) // ["WX", "XY"]
print(sol3)


