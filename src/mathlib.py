## @file mathlib.py
#  @author Ondrej Kováč
#  @date 13.4.2021
#  @brief Math library defining math operations (+,-,*,/,!,^,nth_root, RNG)


from random import randint


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

## @brief Factorial of a whole number
# @exception ValueError if @p n is negative
# @exception TypeError if @p n is a fraction
# @return n!
def fact(n):
    if n < 0:
        raise ValueError
    if n % 1 != 0:
        raise TypeError 

    n = int(n)
    result = 1
    for i in range(1, n+1):
        result *= i

    return result

## @brief Exponentiation of a base @p b by an exponent @p n 
# @exception ValueError if @p n is negative
# @exception TypeError if @p n is a fraction
# @return b^n
def exp(b,n):
    if n < 0:
        raise ValueError
    if n % 1 != 0:
        raise TypeError 
    
    n = int(n)
    return (b ** n)

## @brief Finding @p n th root of number @p x
# @exception ZeroDivisionError if @p n is zero
# @exception ValueError if @p n is negative
# @exception TypeError if @p n is a fraction
# @exception ValueError if @p n is even and @p x is negative
# @return x^(1/n)
def root(n,x):
    if n == 0:
        raise ZeroDivisionError
    if n < 0:
        raise ValueError
    if n % 1 != 0:
        raise TypeError
    if (n % 2 == 0) and (x < 0):
        raise ValueError

    if (n % 2 == 1) and (x < 0):
        x = abs(x)
        return -(x ** (1/n))
    else:
        return x ** (1/n)

## @brief Producing a random number in a given range
# @exception ValueError if @p b <= @p a
# @exception TypeError if @p a and @p b are fractions
# @return Random number from range <a,b>
def rng(a,b):
    if b <= a:
        raise ValueError
    if (a % 1 != 0) or (b % 1 != 0):
        raise TypeError

    return randint(a,b)



#End of file mathlib.py