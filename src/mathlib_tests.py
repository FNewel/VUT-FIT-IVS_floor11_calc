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
        self.assertEqual(mathlib.add(0, -0.1) -0.1)
        
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
        self.assertEqual(mathlib.sub(-20, -10), -20)
        self.assertEqual(mathlib.sub(-1000, -2000), 1000)
        self.assertEqual(mathlib.sub(-0.725, -0.275), -0.5)

        #Test one negative value
        self.assertEqual(mathlib.sub(-20, 10), -30)
        self.assertEqual(mathlib.sub(20, -10), 30)
        self.assertEqual(mathlib.sub(1000, -2000), -1000)
        self.assertEqual(mathlib.sub(-1000, 2000), -3000)
        self.assertEqual(mathlib.sub(-0.725, 0.275), -1)
        self.assertEqual(mathlib.sub(0.725, -0.275), 0.5)


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
    
    def tes_div(self):

        #Test positive and negative variations
        self.assertEqual(mathlib.div(20, 10), 2)
        self.assertEqual(mathlib.div(-20, -10), 2)
        self.assertEqual(mathlib.div(-20, 10), -2)
        self.assertEqual(mathlib.div(20, -10), -2)

        #Test division by zero
        self.assertRaises(ZeroDivisionError, mathlib.div(1,0))
        self.assertRaises(ZeroDivisionError, mathlib.div(0,0))

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
    #TODO

## @brief Tests for exponent
class TestExponent(unittest.TestCase):
    #TODO

## @brief Tests for root
class TestRoot(unittest.TestCase):
    #TODO

if __name__ == '__main__':
    unittest.main()

# End of file mathlib_tests.py        
