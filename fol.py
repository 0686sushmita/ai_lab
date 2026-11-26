# Unification in First Order Logic


def unify(x, y, substitution={}):
    if substitution is None:
        return None

    if x == y:
        return substitution

    if isinstance(x, str) and x.islower():
        substitution[x] = y
        return substitution

    if isinstance(y, str) and y.islower():
        substitution[y] = x
        return substitution

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y):
            return None

        for a, b in zip(x, y):
            substitution = unify(a, b, substitution)

            if substitution is None:
                return None

        return substitution

    return None


# Example
x = ("Knows", "x", "John")
y = ("Knows", "Mary", "John")

result = unify(x, y)

if result:
    print("Unification Successful")
    print("Substitution:", result)
else:
    print("Unification Failed")
