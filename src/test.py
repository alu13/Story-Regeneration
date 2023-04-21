import numpy as np
from scipy.optimize import linear_sum_assignment


n = 2
m = 3
# Create a cost matrix with random values
cost_matrix = np.random.rand(n, m)

print(cost_matrix)
# Solve the assignment problem
row_ind, col_ind = linear_sum_assignment(cost_matrix, maximize = True)

# Print the indices of the optimal assignment
print(row_ind)  # Indices of the rows that are matched
print(col_ind)  # Indices of the columns that are matched

total = cost_matrix[row_ind, col_ind].sum()
print(total)

k = np.zeros((3, 3))
print(k)