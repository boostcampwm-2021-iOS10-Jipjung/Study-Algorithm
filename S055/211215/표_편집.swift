import Foundation

class Node {
    var prev: Node?
    var next: Node?
    var value: Int
    init(value: Int = -1) {
        self.value = value
    }
}

func solution(_ n:Int, _ k:Int, _ cmd:[String]) -> String {
    let head = Node()
    makeLinkedList(head: head, size: n)
    
    var answer = [String](repeating: "O", count: n)
    var cur: Node? = head.next
    var stack = [Node]()
    
    move(cur: &cur, distance: k)
    for element in cmd {
        let prefix = String(element.prefix(1))
        switch prefix {
        case "U":
            let num = Int(element.split(separator: " ").last!)!
            move(cur: &cur, distance: -num)
        case "D":
            let num = Int(element.split(separator: " ").last!)!
            move(cur: &cur, distance: num)
        case "C":
            answer[cur!.value] = "X"
            remove(cur: &cur, stack: &stack)
        case "Z":
            if let index = restore(stack: &stack) {
                answer[index] = "O"
            }
        default: break
        }
    }
    
    return answer.joined()
}

func makeLinkedList(head: Node, size: Int) {
    var p = head
    for i in (0..<size) {
        let node = Node(value: i)
        p.next = node
        node.prev = p
        p = p.next!
    }
}

func travelLinkedList(head: Node?) -> [Int] {
    var p = head
    var result = [Int]()
    while let cur = p {
        result.append(cur.value)
        p = p?.next
    }
    
    return result
}

func move(cur: inout Node?, distance: Int) {
    var count = 0
    if distance > 0 {
        while (cur != nil) && (count < distance) {
            cur = cur?.next
            count += 1
        }
    } else {
        while (cur != nil) && (count < -distance) {
            cur = cur?.prev
            count += 1
        }
    }
}

func remove(cur: inout Node?, stack: inout [Node]) {
    guard cur != nil else {
        return
    }
    
    cur?.prev?.next = cur?.next
    cur?.next?.prev = cur?.prev
    stack.append(cur!)
    
    if let next = cur?.next {
        cur = next
    } else {
        cur = cur?.prev!
    }
}

func restore(stack: inout [Node]) -> Int? {
    if let node = stack.popLast() {
        node.prev?.next = node
        node.next?.prev = node
        return node.value
    }
    return nil
}
