# 8 Puzzle Problem using IDS


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


def depth_limited_search(state, goal, depth, path):
    if state == goal:
        return path

    if depth == 0:
        return None

    for neighbor in get_neighbors(state):
        if neighbor not in path:
            result = depth_limited_search(neighbor, goal, depth - 1, path + [neighbor])

            if result is not None:
                return result

    return None


def ids(start, goal):
    depth = 0

    while True:
        print("Searching at depth:", depth)

        result = depth_limited_search(start, goal, depth, [start])

        if result is not None:
            return result

        depth += 1


# Initial state
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)

# Goal state
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)


solution = ids(start, goal)

print("\nSolution Found!")
print("Number of moves:", len(solution) - 1)

for step in solution:
    display(step)
