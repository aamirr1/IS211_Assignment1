#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week-1 Assignment1, Part 1 - Functions and Exceptions"""


def listDivide(numbers,divide=2):
        """This function returns the number of elements in the numbers list that
           are divisible by divide. 
        Args:
                numbers(list): Contains list of numbers 
                divide(int): comes with a default value of 2
        Return:
                int: returns the results 
        Example:
                >>> listDivide([]) 
                0
                >>> listDivide([1,2,3,4,5], 1)
                
        """
        result = 0
        for number1 in numbers:
                if number1 % divide == 0:
                        result += 1
        return result

class ListDivideException(Exception):
        pass

def testListDivide():

        try:
                listDivide([1,2,3,4,5])
        except:
                raise ListDivideException('Error')
        try:
                listDivide([2,4,6,8,10])
        except:
                raise ListDivideException('Error')
        try:
                listDivide([30,54,63,98,100], divide=10)
        except:
                raise ListDivideException('Error')
        try:
                listDivide([])
        except:
                raise ListDivideException('Error')
        try:
                listDivide([1,2,3,4,5],1)
        except:
                raise ListDivideException('Error')
        return

testListDivide()
