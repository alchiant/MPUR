import numpy as np
from scipy.optimize import linprog


# Define the coefficients matrix for constraints (aij)
# Rows correspond to specialized equipment and columns to product types
coefficients_matrix = np.array([
    [8, 10, 15, 17],
    [20, 18, 23, 25],
    [2, 1, 2, 3],
    [1, 2, 4, 3]
])

# Define the right-hand side of constraints (stock of resources)
rhs_constraints = np.array([1600, 3200, 240, 400])

# Define bounds for variables (x1, x2, x3, x4)
x_bounds = [(2, 40), (10, np.inf), (0, 50), (15, 15)]


# Define the objective coefficients for profit maximization (Cj - Sj)
objective_coefficients = np.array([300 - 220, 450 - 300, 600 - 400, 500 - 420])

# Solve the linear program for profit maximization
result = linprog(c=-objective_coefficients, A_ub=coefficients_matrix, b_ub=rhs_constraints, bounds=x_bounds, method='highs')

# Print the results
print("Optimal Production Plan (x1, x2, x3, x4):", str(np.floor(result.x)))
print("Maximum Profit:", str(np.floor(-result.fun))) # The objective function is minimized by linprog, so we negate it to get the maximum profit


# Define the objective coefficients for maximizing product output (all coefficients are 1)
objective_coefficients = np.array([1, 1, 1, 1])

# Solve the linear program for maximizing product output
result = linprog(c=-objective_coefficients, A_ub=coefficients_matrix, b_ub=rhs_constraints, bounds=x_bounds, method='highs')

# Print the results
print("Optimal Production Plan (x1, x2, x3, x4):", str(np.floor(result.x)))
print("Maximum Output:", str(np.floor(-result.fun))) # The objective function is minimized by linprog, so we negate it to get the maximum profit


# Define the objective coefficients for maximizing the load of specialized equipment
objective_coefficients = np.array([coefficients_matrix[0][0] + coefficients_matrix[1][0],
                                   coefficients_matrix[0][1] + coefficients_matrix[1][1],
                                   coefficients_matrix[0][2] + coefficients_matrix[1][2],
                                   coefficients_matrix[0][3] + coefficients_matrix[1][3]])

# Solve the linear program for maximizing the load of specialized equipment
result = linprog(c=-objective_coefficients, A_ub=coefficients_matrix, b_ub=rhs_constraints, bounds=x_bounds, method='highs')

# Print the results
print("Optimal Production Plan (x1, x2, x3, x4):", str(np.floor(result.x)))
print("Maximum Load:", str(np.floor(-result.fun))) # The objective function is minimized by linprog, so we negate it to get the maximum profit
