# Hill Climbing Algorithm


def hill_climbing(start):
    current = start

    while True:
        print("Current State:", current)

        neighbors = [current - 1, current + 1]

        best = max(neighbors)

        if best <= current:
            print("Reached Goal:", current)
            break

        current = best


start = 0
hill_climbing(start)
