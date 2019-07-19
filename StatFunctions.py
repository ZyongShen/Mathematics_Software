from sympy import *
from pandas import numpy


class StatFuncs():

    def mean(self, numSet=None):
        # Calculates the mean from the data set
        sum = 0
        result = 0
        if numSet is None:
            return "Cannot calculate."
        else:
            for num in numSet:
                sum += num
            result = sum / len(numSet)
            return result

    def median(self, numSet):
        # Calculates the median from the data set
        # Find the middle value and if there are two then divide the sum of the two by 2
        even = False
        index = -1
        medVal = 0
        if len(numSet) % 2 == 0:
            even = True
            index = (len(numSet)/2) - 0.5
            medVal = numSet[index]
            index = (len(numSet)/2) + 0.5
            medVal = medVal + numSet[index]
        else:
            even = False
            index = (len(numSet) / 2) + 0.5
            medVal = numSet[index]
        return medVal

    def mode(self, numSet):
        # Finds the most common number
        # mode: Value that is most common
        numDict = {}
        result = 0
        large = 0
        for num in numSet:
            if num not in numSet.keys():
                numDict[num] = 1
            else:
                numDict[num] += 1
        for val in numDict.keys():
            if numDict[val] > large:
                result = val
                large = numDict[val]
        return result

    def sum(self, numSet):
        # Finds the sum of numbers in a data set
        sum = 0
        for num in numSet:
            sum += num
        return sum

    def factorial(self, num):
        # Finds the factorial of a given number

        fact = 1
        if num == 0:
            return 1
        else:
            while num > 0:
                fact = fact * num
                num -= 1

        return fact

    def product(self, numSet):
        product = 1
        for num in numSet:
            product = product * num
        return product

    def max(self, numSet):
        max = 0
        for num in numSet:
            if num > max:
                max = num

        return max

    def min(self, numSet):
        min = 0
        for num in numSet:
            if num < min:
                min = num

        return min

    def variance(self, numSet):
        # returns the variance of the data set
        vari = numpy.var(numSet)
        return vari





