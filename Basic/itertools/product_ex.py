from itertools import product

data = ['A','B','C']

result = list(product(data, repeat=2))
print(result)

#[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]