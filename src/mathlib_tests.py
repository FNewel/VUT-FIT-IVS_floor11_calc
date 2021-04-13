## @file mathlib_tests.py
#  @author Ondrej Kováč
#  @date 27.3.2021
#  @brief Unit tests for mathematical library "mathlib"

import unittest
import mathlib

## @brief Tests for addition
class TestAddition(unittest.TestCase):
    
    def test_add(self):

        #Test boudary values
        self.assertEqual(mathlib.add(0.1, -0.2), -0.1)
        self.assertEqual(mathlib.add(0.2, -0.1), 0.1)
        self.assertEqual(mathlib.add(0, 0.1), 0.1)
        self.assertEqual(mathlib.add(0, -0.1), -0.1)
        
        #Test result = 0
        self.assertEqual(mathlib.add(-5,5), 0)
        self.assertEqual(mathlib.add(1000,-1000), 0)
        self.assertEqual(mathlib.add(-0.725, 0.725), 0)

        #Test two negative values
        self.assertEqual(mathlib.add(-20, -10), -30)
        self.assertEqual(mathlib.add(-1000, -2000), -3000)
        self.assertEqual(mathlib.add(-0.725, -0.275), -1)


## @brief Tests for subtraction
class TestSubtraction(unittest.TestCase):
    
    def test_sub(self):

        #Test boundary values
        self.assertEqual(mathlib.sub(0.1, 0.2), -0.1)
        self.assertEqual(mathlib.sub(-0.1, -0.2), 0.1)
        self.assertEqual(mathlib.sub(0, 0.1), -0.1)
        self.assertEqual(mathlib.sub(0, -0.1), 0.1)
        self.assertEqual(mathlib.sub(0.1, 0), 0.1)
        self.assertEqual(mathlib.sub(-0.1, 0), -0.1)


        #Test result = 0
        self.assertEqual(mathlib.sub(5,5), 0)
        self.assertEqual(mathlib.sub(1000,1000), 0)
        self.assertEqual(mathlib.sub(2.25, 2.25), 0)
        self.assertEqual(mathlib.sub(0.725,0.725), 0)

        #Test two negative values
        self.assertEqual(mathlib.sub(-20, -10), -10)
        self.assertEqual(mathlib.sub(-1000, -2000), 1000)
        self.assertEqual(mathlib.sub(-0.725, -0.225), -0.5)

        #Test one negative value
        self.assertEqual(mathlib.sub(-20, 10), -30)
        self.assertEqual(mathlib.sub(20, -10), 30)
        self.assertEqual(mathlib.sub(1000, -2000), 3000)
        self.assertEqual(mathlib.sub(-1000, 2000), -3000)
        self.assertEqual(mathlib.sub(-0.725, 0.275), -1)
        self.assertEqual(mathlib.sub(0.725, -0.275), 1)


## @brief Tests for multiplication
class TestMultiplication(unittest.TestCase):
    
    def test_mul(self):

        #Test positive and negative variations
        self.assertEqual(mathlib.mul(1,-1), -1)
        self.assertEqual(mathlib.mul(-1,1), -1)
        self.assertEqual(mathlib.mul(1,1), 1)
        self.assertEqual(mathlib.mul(-1,-1), 1)

        #Test result = 0
        self.assertEqual(mathlib.mul(5,0), 0)
        self.assertEqual(mathlib.mul(-5,0), 0)
        self.assertEqual(mathlib.mul(0,0), 0)

        #Test fractions
        self.assertEqual(mathlib.mul(10, 0.25), 2.5)
        self.assertEqual(mathlib.mul(10, -0.25), -2.5)
        self.assertEqual(mathlib.mul(-0.25, -0.5), 0.125)
        self.assertEqual(mathlib.mul(0.25, -0.5), -0.125)
        self.assertEqual(mathlib.mul(15.5, 0.01), 0.155)
        self.assertEqual(mathlib.mul(0.01, 15.5), 0.155)
        


## @brief Tests for division
class TestDivision(unittest.TestCase):
    
    def test_div(self):

        #Test positive and negative variations
        self.assertEqual(mathlib.div(20, 10), 2)
        self.assertEqual(mathlib.div(-20, -10), 2)
        self.assertEqual(mathlib.div(-20, 10), -2)
        self.assertEqual(mathlib.div(20, -10), -2)

        #Test division by zero
        self.assertRaises(ZeroDivisionError, mathlib.div, 1, 0)
        self.assertRaises(ZeroDivisionError, mathlib.div, 0, 0)

        #Test division of zero
        self.assertEqual(mathlib.div(0, 20), 0)
        self.assertEqual(mathlib.div(0, -20), 0)

        #Test fractions
        self.assertEqual(mathlib.div(10, 0.1), 100)
        self.assertEqual(mathlib.div(-10, 0.1), -100)
        self.assertEqual(mathlib.div(0.25, 0.05), 5)
        self.assertEqual(mathlib.div(0.25, 0.5), 0.5)
        self.assertEqual(mathlib.div(0.25, 5), 0.05)


## @brief Tests for factorial
class TestFactorial(unittest.TestCase):
    
    def test_fact(self):

        #Test a > 0
        self.assertEqual(mathlib.fact(1), 1)
        self.assertEqual(mathlib.fact(4), 24)

        #Test a = 0
        self.assertEqual(mathlib.fact(0), 1)

        #Test a < 0
        self.assertRaises(ValueError, mathlib.fact, -3)
        self.assertRaises(ValueError, mathlib.fact, -3.000)

        #Test number is a float
        self.assertRaises(TypeError, mathlib.fact, 2.25)
        self.assertRaises(TypeError, mathlib.fact, 0.5)

        #Test number is an integer-like float
        self.assertEqual(mathlib.fact(2.00), 2)
        self.assertEqual(mathlib.fact(4.0000), 24)


## @brief Tests for exponent
class TestExponent(unittest.TestCase):
    
    def test_exp(self):
        
        #Test n is not an integer
        self.assertRaises(TypeError, mathlib.exp, 2, 2.5)

        #Test n < 0
        self.assertRaises(ValueError, mathlib.exp, 2, -2)
        self.assertRaises(ValueError, mathlib.exp, 0, -3)

        #Test n = 0
        self.assertEqual(mathlib.exp(2, 0), 1)
        self.assertEqual(mathlib.exp(2.5, 0), 1)
        self.assertEqual(mathlib.exp(-5, 0), 1)
        self.assertEqual(mathlib.exp(0, 0), 1)

        #Test n > 0, n is even
        self.assertEqual(mathlib.exp(2, 2), 4)
        self.assertEqual(mathlib.exp(-2, 2), 4)
        self.assertEqual(mathlib.exp(0, 2), 0)
        self.assertEqual(mathlib.exp(-0.5, 2), 0.25)

        #Test n > 0, n is odd
        self.assertEqual(mathlib.exp(2, 3), 8)
        self.assertEqual(mathlib.exp(-2, 3), -8)
        self.assertEqual(mathlib.exp(0, 3), 0)
        self.assertEqual(mathlib.exp(-0.5, 3), -0.125)

## @brief Tests for root
class TestRoot(unittest.TestCase):

    def test_root(self):

        #Test n = 0
        self.assertRaises(ZeroDivisionError, mathlib.root, 0, 4)

        #Test n < 0
        self.assertRaises(ValueError, mathlib.root, -2, 4)
        self.assertRaises(ValueError, mathlib.root, -3, 8)

        #Test n is not an integer
        self.assertRaises(TypeError, mathlib.root, 2.5, 2)
        self.assertRaises(TypeError, mathlib.root, 0.5, 2)

        #Test n > 0, n is even
        #x > 0
        self.assertEqual(mathlib.root(2, 16), 4)
        self.assertEqual(mathlib.root(4, 16), 2)
        #x = 0
        self.assertEqual(mathlib.root(2, 0), 0)
        self.assertEqual(mathlib.root(4, 0), 0)
        #x < 0
        self.assertRaises(ValueError, mathlib.root, 2, -8)
        
        #Test n > 0, n is odd
        #x > 0
        self.assertEqual(mathlib.root(1, 8), 8)
        self.assertEqual(mathlib.root(3, 8), 2)
        #x = 0
        self.assertEqual(mathlib.root(1, 0), 0)
        self.assertEqual(mathlib.root(3, 0), 0)
        #x < 0
        self.assertEqual(mathlib.root(1, -8), -8)
        self.assertEqual(mathlib.root(3, -8), -2)

## @brief Tests for random number generator
class TestRNG(unittest.TestCase):

    def test_rng(self):

        #Test a and b not integers
        self.assertRaises(TypeError, mathlib.rng, 10, 15.6)
        self.assertRaises(TypeError, mathlib.rng, 10.5, 15)
        self.assertRaises(TypeError, mathlib.rng, 10.5, 15.6)

        #Test b < a
        self.assertRaises(ValueError, mathlib.rng, 20,10)
        self.assertRaises(ValueError, mathlib.rng, 2,3)

        #Test a = b
        self.assertRaises(ValueError, mathlib.rng, 5,5)
        self.assertRaises(ValueError, mathlib.rng, 0,0)

        #Test positive interval, should return integer
        self.assertEqual((mathlib.rng(0, 20) % 1), 0)
        self.assertTrue(0 <= (mathlib.rng(0,20)) <= 20)
        self.assertEqual((mathlib.rng(50,120) % 1), 0)
        self.assertTrue(50 <= (mathlib.rng(0,20)) <= 120)

        #Test negative interval, should return integer
        self.assertEqual((mathlib.rng(-20, 0) % 1), 0)
        self.assertTrue(-20 <= (mathlib.rng(-20, 0)) <= 0)
        self.assertEqual((mathlib.rng(-120, -50) % 1), 0)
        self.assertTrue(-120 <= (mathlib.rng(-120, -50)) <= -50)

        #Test negative-positive interval, should return integer
        self.assertEqual((mathlib.rng(-20, 30) % 1), 0)
        self.assertTrue(-20 <= (mathlib.rng(-20, 30)) <= 30)
        self.assertEqual((mathlib.rng(-120, 50) % 1), 0)
        self.assertTrue(-120 <= (mathlib.rng(-120, 50)) <= 50)
                 

if __name__ == '__main__':
    unittest.main()

# End of file mathlib_tests.py        
