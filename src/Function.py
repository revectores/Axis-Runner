from math import *

class Function:
    def __init__(self,formula,definition):
        self.formula = formula
        self.definition = definition
        self.points = [Point(x, formula(x)) for x in definition]


class FuncModel:
    def linear(self,k,b):
        return lambda x: k*x+b

    def exp(self,base):
        return lambda x: base**x

    def power(self,exp):
        return lambda x: x**exp

    def sin(self,A,k,phi):
        return lambda x: A*sin(k*x+phi)

    def arctri(self):
        pass

    def newFunction(self):
        funcModel = FuncModel()
        newFun = self.linear(1,1)
        fun = Function(newFun, range(-10,10))
        return fun

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%f,%f)"%(self.x, self.y)


class UnitTest:
    def funcModelTest(self):
        fm = FuncModel()
        tf = fm.sin(1,1,0)
        print(tf(pi/2))

if __name__ == '__main__':
    unitest = UnitTest()
    unitest.funcModelTest()