from sympy import *

class BasicFunc():

    # comparison operators

    def compNums(self, x, y, func):
        # compare two numbers
        function = str(func).lower()
        if function is "greater":
            return x > y
        elif function is "lower":
            return x < y
        elif function is "equal":
            return x == y

    def factor(self, x):
        # find all the prime factors of the number
        primeFact = factorint(x)
        return primeFact

    def gcf(self, x, y):
        # This calculates using the euler method
        if y > x:
            if x == 0:
                return y
            self.gcf(y % x, x)
        else:
            if y == 0:
                return x
            self.gcf(y, x % y)

    def lcm(self, x, y):
        # Divide the product of prime factors by the gcd

        gcd = self.gcf(x, y)
        xFact = self.factor(x)
        yFact = self.factor(y)
        productX = 1
        productY = 1
        for num1 in xFact.items():
            for i in range(0, num1.value()):
                productX = productX * num1.key()
        for num1 in yFact.items():
            for i in range(0, num1.value()):
                productY = productY * num1.key()
        result = (productX * productY)/gcd
        return result

    # value times 10 to the power
    def pwr10(self, x, pwr):
        result = x * 10^pwr
        return result

    def absolute(self, x):
        return abs(x)

    # Expand a function from factored to unfactored
    def xpanFunc(self, func1="", func2=""):
        if func1 is "" or func2 is "":
            return None
        result = expand(func1, func2)
        return result






