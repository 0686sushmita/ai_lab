# Forward Chaining

facts = {"A", "B"}

rules = [({"A", "B"}, "C"), ({"C"}, "D"), ({"D"}, "E")]


def forward_chaining(facts, rules, goal):
    while True:
        new_fact = False

        for condition, result in rules:
            if condition.issubset(facts) and result not in facts:
                facts.add(result)
                print("Derived:", result)
                new_fact = True

                if result == goal:
                    return True

        if not new_fact:
            return goal in facts


goal = "E"

if forward_chaining(facts, rules, goal):
    print("Goal Reached:", goal)
else:
    print("Goal Not Reached")
