class Node:
     def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

def alpha_beta(node, alpha, beta, maximizing_player):
    if not node.children:
        return node.value

    if maximizing_player:
        v = float('-inf')
        for child in node.children:
            v = max(v, alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v
    else:
        v = float('inf')
        for child in node.children:
            v = min(v, alpha_beta(child, alpha, beta, True))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v


leaf1 = Node(36)
leaf2 = Node(12)
leaf3 = Node(8)
leaf4 = Node(2)
node1 = Node(2, [leaf1, leaf2])
node2 = Node(8, [leaf3, leaf4])
root = Node(0, [node1, node2])

 
result = alpha_beta(root, float('-inf'), float('inf'), True)
print("Optimal value:", result)
