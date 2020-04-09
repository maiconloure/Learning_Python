# List Comprehension is awesome;

"""
vals = [expression
        for value in collection
        if collection]

This is equivalent to:

vals = []
for value in collection:
        if collection:
                vals2.append(expression)
"""


# Example

even_squares = [x * x for x in range(10) if not x % 2]
print(even_squares)