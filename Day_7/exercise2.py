# Day 7 exercise 2
A = {1, 2, 3, 4, 5}
B = {3, 5, 6, 7, 8}

union_set = A | B
print(f"A U B (Union): {union_set}")

intersection_set = A & B 
print(f"A ∩ B (Intersection): {intersection_set}")
is_subset = A.issubset(B)
print(f"Is A a subset of B?: {is_subset}") 

are_disjoint = A.isdisjoint(B)
print(f"Are A and B disjoint?: {are_disjoint}")  
symmetric_difference = A ^ B  
print(f"A Δ B (Symmetric Difference): {symmetric_difference}")  

del A
del B