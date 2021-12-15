class Node:
    def __init__(self, num, head = None, tail = None):
        self.num = num
        self.head = head
        self.tail = tail

def link_list(upper_bound):
    node_list = [None]
    for i in range(upper_bound):
        node_list.append(Node(i))
    node_list.append(None)

    for i in range(1, upper_bound + 1):
        node_list[i].head = node_list[i - 1]
    for i in range(1, upper_bound + 1):
        node_list[i].tail = node_list[i + 1]

    return node_list[1]

def cmd_U(n, node):
    for _ in range(n):
        node = node.head        
    return node

def cmd_D(n, node):
    for _ in range(n):
        node = node.tail      
    return node

def cmd_C(node, trash):
    if node.head != None:
        node.head.tail = node.tail
    if node.tail != None:
        node.tail.head = node.head
    trash += [node]
    if node.tail == None:
        node = trash[-1].head
    else:
        node = trash[-1].tail
    return (node, trash)

def cmd_Z(trash):
    node = trash.pop()
    if node.head != None:
        node.head.tail = node
    if node.tail != None:
        node.tail.head = node
    return trash

def debug_list(node):
    if node == None:
        print("\n-----------")
        return
    print(node.num, end = " -> ")
    debug_list(node.tail)

def solution(n, k, cmds):
    trash = []
    root_node = link_list(n)
    node = cmd_D(k, root_node)
    for cmd in cmds:
        if cmd[0] == "U":
            node = cmd_U(int(cmd[2:]), node)
        elif cmd[0] == "D":
            node = cmd_D(int(cmd[2:]), node)
        elif cmd[0] == "C":
            node, trash = cmd_C(node, trash)
        elif cmd[0] == "Z":
            trash = cmd_Z(trash)

    answer = ["O" for _ in range(n)]
    for deleted_node in trash:
        answer[deleted_node.num] = "X"
    return "".join(answer)