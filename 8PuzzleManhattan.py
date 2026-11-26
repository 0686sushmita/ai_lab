# 8 Puzzle using Manhattan Distance


def manhattan_distance(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])

            current_row = i // 3
            current_col = i % 3

            goal_row = goal_pos // 3
            goal_col = goal_pos % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


# Initial state
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)

# Goal state
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

distance = manhattan_distance(start, goal)

print("Initial State:")
for i in range(0, 9, 3):
    print(start[i : i + 3])

print("\nGoal State:")
for i in range(0, 9, 3):
    print(goal[i : i + 3])

print("\nManhattan Distance:", distance)
