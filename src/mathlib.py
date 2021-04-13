## @file mathlib.py
#  @author Ondrej Kováč
#  @date 13.4.2021
#  @brief Math library defining math operations (+,-,*,/,!,^,sqr_root, RNG)


## @brief Sum of 2 numbers
# @return a + b
def add(a,b):
    return a+b

## @brief Subtraction of 2 numbers
# @return a - b
def sub(a,b):
    return a-b

## @brief Product of 2 numbers
# @return a * b
def mul(a,b):
    return a*b

## @brief Division of 2 numbers
# @exception ZeroDivisionError if @p b is equal to 0
# @return a / b
def div(a,b):
    if b == 0:
        raise ZeroDivisionError
        
    return a/b




#End of file mathlib.py