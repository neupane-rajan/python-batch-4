# set Mathematical operations

A = {1, 2, 3, 4}
B = {2, 4, 5, 6}

# 1.Union(|):union combines all unique elements from two sets
# using operator
union = A | B
# print(union)
# using method
union = A.union(B)
# print(union)

# Intersection(&):
# intersection returns the elements that are common to both sets.
intersection = A & B
# print(intersection)
# using method
# A.intersection(B)

# Difference(-)
# difference returns elements that are in the first set but not in the second set

difference = A - B
# print(difference)
# using
# difference = A.difference(B)

# symettrice Difference(^): symmetrice difference returns elements that belong to either set, but not both

symmetric_difference = A ^ B
print(A, B)
print(symmetric_difference)

# set comparison

A = {1, 2, 3}
B = {1, 2, 3}
C = {1, 2}

print(A == B)
print(B == C)


# set comprehension
# frozenset

# updating set operations
# intersection_update()
# difference_update()
# symmetric_difference_update()
# subset
# proper_subset
# superset
# Disjoint
