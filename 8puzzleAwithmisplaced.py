# 8 Puzzle using A* with Misplaced Tiles


def heuristic(state, goal):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count


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


def astar(start, goal):
    open_list = [(heuristic(start, goal), 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, state, path = open_list.pop(0)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_h = heuristic(neighbor, goal)
                new_f = new_g + new_h

                open_list.append((new_f, new_g, neighbor, path + [neighbor]))

    return None


def display(state):
    for i in range(0, 9, 3):
        print(state[i : i + 3])
    print()


start = (1, 2, 3, 4, 0, 6, 7, 5, 8)

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution = astar(start, goal)

if solution:
    print("Solution Found!")
    print("Number of moves:", len(solution) - 1)

    for step in solution:
        display(step)
else:
    print("No solution found!")
