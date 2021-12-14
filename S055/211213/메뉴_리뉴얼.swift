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

    result = [String](repeating: "", count: order.count) // 임시 저장공간을 order의 길이만큼 만들어준다
    combiDFS(phase: 0, startIndex: 0, result: result)
    
    return candidate
}

func solution(_ orders:[String], _ course:[Int]) -> [String] {
    var temp = [String: Int]() // "AB": 횟수

    for element in orders {
        makeCandidate(order: element).forEach { candidate in
            if let count = temp[candidate] {
                temp.updateValue(count + 1, forKey: candidate)
            } else {
                temp[candidate] = 1
            }
        }
    }
    
    let over1 = temp
        .filter { course.contains($0.key.count) }
        .filter { $0.value > 1 && $0.key.count > 1 } // 반복횟수 2회 이상

    var words = [[(String, Int)]](repeating: [], count: 11)
    over1.forEach {
        words[$0.key.count].append(($0.key, $0.value)) // 글자 길이별로 분리
    }

    var answer = [String]()
    for size in (0..<words.count) { // 반복횟수가 높은 순으로 정렬
        words[size].sort { $0.1 > $1.1 }
        if let firstItem = words[size].first {
            for element in words[size] {
                if element.1 >= firstItem.1 { // 같은 반복숫자만 자르기
                    answer.append(element.0)
                } else {
                    break
                }
            }
        }
    }

    return answer.sorted()
}
