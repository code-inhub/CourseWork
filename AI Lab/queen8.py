from queue import PriorityQueue

def heuristic(state):
    attacks = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                attacks += 1
    return attacks

def solve_8_queen():
    priority_queue = PriorityQueue()
    priority_queue.put((0, ()))

    while not priority_queue.empty():
        (cost, state) = priority_queue.get()

        if len(state) == 8:
        
            return state

        for next_row in range(8):
            if next_row not in state:
            
                successor_state = state + (next_row,)
            
                successor_cost = len(successor_state) + heuristic(successor_state)
        
                priority_queue.put((successor_cost, successor_state))

    return None
      
solution = solve_8_queen()

if solution:
    print("Solution found:")
    for i in range(8):
        print("0" * solution[i] + "1" + "0" * (7 - solution[i]))
else:
    print("No solution found.")