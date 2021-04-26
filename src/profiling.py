## @file profiling.py
#  @author Ondrej Kováč
#  @author Martin Talajka (optimization)
#  @date 13.4.2021
#  @brief Profiling file used for analysis and discovery of inefficiencies in math functions from mathlib.py


from mathlib import add, exp, mul, div, exp, sub, root
from sys import stdin

#Read stdin into an array
num_arr = [int(num) for line in stdin for num in line.split()]

#Create sums
num_amount, sum_xi, sum_xi_raised_2 = len(num_arr), 0, 0

for num in num_arr: sum_xi, sum_xi_raised_2 = add(sum_xi, num), add(sum_xi_raised_2, exp(num, 2))

#Overline x
overline_x = mul(div(1,num_amount), sum_xi)

#result = N*overlineX^2
result = mul(num_amount, exp(overline_x, 2))

#result Parentheses
result = sub(sum_xi_raised_2, result)

#result = 1\(N-1) * Parentheses
result = mul(div(1, sub(num_amount, 1)), result)

#result = sqr_root(1\(N-1) * Parentheses)
result = root(2, result)

#Print the result
print(result)
