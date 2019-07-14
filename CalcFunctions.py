from sympy import *


# make this is cleaner version of microsoft mathematics

class calcFuncs():

    # derivatives
    def derivative(self, func, var, numTimes):
        derVal = diff(func, var, numTimes)
        return derVal

    # Integrals

    def defInt(self, func, int1=None, int2=None, int3=None):
        if int1 is None:
            print("No result")
        elif int1 is not None and int2 is None and int3 is None:
            integral = integrate(func, int1)
            return integral
        elif int1 is not None and int2 is not None and int3 is None:
            integral = integrate(func, int1, int2)
            return integral
        elif int1 is None and int2 is not None and int3 is not None:
            integral = integrate(func, int1, int2, int3)
            return integral
        else:
            print("Cannot calculate")

    def indefInt(self, func, var1 = None, var2 = None, var3 = None):
        if var1 is None:
            print("No result")
        elif var1 is not None and var2 is None and var3 is None:
            integral = integrate(func, var1)
            return integral
        elif var1 is not None and var2 is not None and var3 is None:
            integral = integrate(func, var1, var2)
            return integral
        elif var1 is not None and var2 is not None and var3 is not None:
            integral = integrate(func, var1, var2, var3)
            return integral
        else:
            print("Cannot calculate")

    # limits
    def theLimit(self, func, var, lim, oneSide = None):
        if oneSide is None:
            limVal = limit(func, var, lim)
            return limVal
        else:
            limVal = limit(func, var, lim, oneSide)
            return limVal

    # series
    def expandSeries(self, func, var, low, up):
        expr = exp(func)
        expansion = expr.series(func, var, low, up)
        return expansion








