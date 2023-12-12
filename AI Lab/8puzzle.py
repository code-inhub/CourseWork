import heapq

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define a function to calculate the Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                row, col = divmod(state[i][j] - 1, 3)
                distance += abs(row - i) + abs(col - j)
    return distance

# Define the A* search algorithm
def solve_puzzle(initial_state):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (0 + manhattan_distance(initial_state), 0, initial_state))
    
    while open_list:
        _, g, current_state = heapq.heappop(open_list)
        
        if current_state == goal_state:
            return g  # Return the number of moves to reach the goal
        
        closed_set.add(tuple(map(tuple, current_state)))  # Convert to tuple for hashability
        
        
        print_state(current_state,g)
        # Find the position of the blank tile (0)
        for i in range(3):
            for j in range(3):
                if current_state[i][j] == 0:
                    blank_row, blank_col = i, j
        
        # Generate successor states
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        for dr, dc in moves:
            new_row, new_col = blank_row + dr, blank_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [list(row) for row in current_state]  # Create a copy
                new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
                
                if tuple(map(tuple, new_state)) not in closed_set:
                    heapq.heappush(open_list, (g + 1 + manhattan_distance(new_state), g + 1, new_state))
    
    return -1  # No solution found

def print_state(state, step):
    print(f"Step: {step +1 }")
    for row in state:
        print(row)
    print()
# Example usage:
initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
moves = solve_puzzle(initial_state)
if moves != -1:
    print(f"Number of moves to reach the goal: {moves}")
else:
    print("No solution found.")
