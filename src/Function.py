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

    def tri(self,name,A,k,phi):
        return lambda x: A*sin(k*x+phi)

    def arctri(self):
        pass


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class UnitTest:
    def funcModelTest(self):
        fm = FuncModel()
        tf = fm.tri('sin',1,1,0)
        print(tf(pi/2))


unitest = UnitTest()
unitest.funcModelTest()