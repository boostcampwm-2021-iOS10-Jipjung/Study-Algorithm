import Foundation

typealias FailureRate = (stage: Int, rate: Double)

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var stageSum = [Int](repeating: 0, count: N + 1)
    
    for stage in stages where stage <= N {
        stageSum[stage] += 1
    }
    
    let total = stages.count
    var sum = 0
    let failureRates = (1...N).map { (stage) -> FailureRate in
        let numberOfChallenger = stageSum[stage]
        let remainder = total - sum
        if remainder == 0 {
            return (stage, 0)
        }
        
        let failureRate = Double(numberOfChallenger) / Double(remainder)
        
        sum += numberOfChallenger
        return (stage, failureRate)
    }
    
    return failureRates
        .sorted { $0.rate == $1.rate ? $0.stage < $1.stage : $0.rate > $1.rate }
        .map { $0.stage }
}
