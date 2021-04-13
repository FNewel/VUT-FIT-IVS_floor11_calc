## @file profiling.py
#  @author Ondrej Kováč
#  @date 13.4.2021
#  @brief Profiling file used for analysis and discovery of inefficiencies in math functions from mathlib.py


import mathlib
import sys

#Read stdin into an array
num_arr = []
for line in sys.stdin:
    for num in line.split():
        num = int(num)
        num_arr.append(num)


#Create sums
num_amount = len(num_arr)
sum_xi = 0
sum_xi_raised_2 = 0
for num in num_arr:
    sum_xi = mathlib.add(sum_xi, num)
    sum_xi_raised_2 = mathlib.add(sum_xi_raised_2, mathlib.exp(num, 2))

#Overline x
overline_x = mathlib.mul(mathlib.div(1,num_amount), sum_xi)

#result = N*overlineX^2
result = mathlib.mul(num_amount, mathlib.exp(overline_x, 2))

#result Parentheses
result = mathlib.sub(sum_xi_raised_2, result)

#result = 1\(N-1) * Parentheses
result = mathlib.mul(mathlib.div(1, mathlib.sub(num_amount, 1)), result)

#result = sqr_root(1\(N-1) * Parentheses)
result = mathlib.root(2, result)

#Print the result
print(result)