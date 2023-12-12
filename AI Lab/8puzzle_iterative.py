class PuzzleNode:
    def __init__(self, puzzle_state, parent=None, action=None):
        self.puzzle_state = puzzle_state
        self.parent = parent
        self.action = action

def print_solution(node): 
    if node.parent is None:
        print(node.puzzle_state)
        return
    print_solution(node.parent)
    print(node.puzzle_state)
    print()

def is_goal_state(puzzle_state): 
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return puzzle_state == goal_state

def get_possible_moves(puzzle_state):
    moves = []
    for i in range(3):
        for j in range(3):
            if puzzle_state[i][j] == 0:
                if i > 0:
                    moves.append(('up', i, j))
                if i < 2:
                    moves.append(('down', i, j))
                if j > 0:
                    moves.append(('left', i, j))
                if j < 2:
                    moves.append(('right', i, j))
    return moves

def apply_move(puzzle_state, move):
    new_state = [row[:] for row in puzzle_state]
    direction, i, j = move
    if direction == 'up':
        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
    elif direction == 'down':
        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
    elif direction == 'left':
        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
    elif direction == 'right':
        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
    return new_state

def iddfs(puzzle_state):
    depth = 0
    while True:
        result = dfs(PuzzleNode(puzzle_state), depth)
        if result:
            return result
        depth += 1

def dfs(node, depth_limit):
    if is_goal_state(node.puzzle_state):
        return node
    if depth_limit <= 0:
        return None
    for move in get_possible_moves(node.puzzle_state):
        child_state = apply_move(node.puzzle_state, move)
        child_node = PuzzleNode(child_state, node, move)
        result = dfs(child_node, depth_limit - 1)
        if result:
            return result
    return None

# Example usage
initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution_node = iddfs(initial_state)

if solution_node:
    print("Solution found:")
    print_solution(solution_node)
else:
    print("No solution found.")
