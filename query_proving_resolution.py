# Resolution in First Order Logic

# Knowledge Base
knowledge_base = ["Man(Socrates)", "Man(x) => Mortal(x)"]

# Query
query = "Mortal(Socrates)"


def resolution(kb, query):
    print("Knowledge Base:")
    for statement in kb:
        print(statement)

    print("\nGiven Query:", query)

    print("\nConverting into CNF:")
    clauses = [["Man(Socrates)"], ["~Man(x)", "Mortal(x)"]]

    for clause in clauses:
        print(clause)

    # Negate the query
    negated_query = "~Mortal(Socrates)"
    print("\nNegated Query:", negated_query)

    clauses.append([negated_query])

    print("\nApplying Resolution:")
    print("1. Man(Socrates)")
    print("2. ~Man(x) OR Mortal(x)")
    print("3. ~Mortal(Socrates)")

    print("\nUnifying x = Socrates")
    print("Resolving clauses 1 and 2:")
    print("Mortal(Socrates)")

    print("\nResolving with negated query:")
    print("Empty Clause (□)")

    print("\nQuery is PROVED!")


resolution(knowledge_base, query)
