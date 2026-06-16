'''Problem: The Duplicate Filter
You and your friend both made a list of your favourite numbers, but there are some duplicates between them.'''




s1 = [4, 8, 15, 8, 16, 4, 23]
s2 = [42, 8, 15, 99, 23, 42]

# Step 1 — convert to sets (this removes duplicates automatically)
set1 = set(s1)
set2 = set(s2)

# Step 2 — now use set operations
print("My unique numbers:", set1)
print("Friend unique numbers:", set2)
print("Common numbers:", set1.intersection(set2))
print("Only in your list:", set1 - set2)
print("All combined:", set1.union(set2))

