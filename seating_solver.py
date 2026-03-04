# Brute Force Seating Arrangement Solver
# Demonstrates how all possible seating permutations are checked
# to ensure that friends or students from the same city do not sit together.

import itertools

students = ["A", "B", "C", "D"]

# Example friend pairs
friends = [("A", "B")]

# Example same city pairs
same_city = [("C", "D")]

def is_valid(arrangement):
    for i in range(len(arrangement) - 1):
        pair = (arrangement[i], arrangement[i + 1])

        if pair in friends or pair[::-1] in friends:
            return False

        if pair in same_city or pair[::-1] in same_city:
            return False

    return True

print("Valid Seating Arrangements:\n")

for perm in itertools.permutations(students):
    if is_valid(perm):
        print(perm)
