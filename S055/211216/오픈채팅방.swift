import Foundation

enum MessageType: String {
    case enter = "님이 들어왔습니다."
    case leave = "님이 나갔습니다."
}

struct Log {
    let type: MessageType
    let identifier: String
}

func solution(_ record:[String]) -> [String] {
    var userDict = [String: String]()
    var logs = [Log]()
    record.forEach {
        let row = Array($0.split(separator: " "))
        let identifier = String(row[1])
        switch row[0] {
        case "Enter":
            userDict[identifier] = String(row[2])
            logs.append(Log(type: .enter, identifier: String(row[1])))
        case "Leave":
            logs.append(Log(type: .leave, identifier: String(row[1])))
        case "Change":
            userDict[identifier] = String(row[2])
        default: break
        }
    }
 
    return logs.map { userDict[$0.identifier]! + $0.type.rawValue }
}
