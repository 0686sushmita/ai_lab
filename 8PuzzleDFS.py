# 8 Puzzle Problem using DFS


def display(state):
    for i in range(0, 9, 3):
        print(state[i : i + 3])
    print()


def get_neighbors(state):
    neighbors = []
    pos = state.index(0)

    moves = [-3, 3, -1, 1]

    for move in moves:
        new_pos = pos + move

        if 0 <= new_pos < 9:
            if move == -1 and pos % 3 == 0:
                continue
            if move == 1 and pos % 3 == 2:
                continue

            new_state = list(state)
            new_state[pos], new_state[new_pos] = (new_state[new_pos], new_state[pos])

            neighbors.append(tuple(new_state))

    return neighbors


def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None


# Initial and Goal states
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Solve the puzzle
solution = dfs(start, goal)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for step in solution:
        display(step)
else:
    print("No solution found!")
