from math import *
from random import *

class Function:
    def __init__(self, formula, definition, formula_string, max_def, extend_v, mov_v):
        self.formula = formula               # 解析式
        self._definition = definition        # 定义域
        self.points = [Point(x, self.formula(x)) for x in definition]   # 离散点

        self.formula_string = formula_string  # 解析式字符串
        self.max_def = max_def                # 定义域最大长度
        self.extend_v = extend_v              # 定义域延伸(变化)速度
        self.mov_v = mov_v                    # 函数移动速度矢量
        self.max = max(self.points, key=lambda point: point.y)
        self.min = min(self.points, key=lambda point: point.y)

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, definition):
        self._definition = definition
        self.points = [Point(x, self.formula(x)) for x in definition]
        self.max = max(self.points, key=lambda point: point.y)
        self.min = min(self.points, key=lambda point: point.y)


class FuncModel:
    @staticmethod
    def linear(k, b):
        return lambda x: k*x + b

    @staticmethod
    def exp(base):
        return lambda x: base**x

    @staticmethod
    def power(exp):
        return lambda x: x**exp

    @staticmethod
    def sin(A, k, phi):
        return lambda x: A*sin(k*x+phi)

    @staticmethod
    def arctri():
        pass


class FuncRandom:
    @staticmethod
    def linear(kr, br):
        k = random(kr[0], kr[1])
        b = random(br[0], br[1])
        max_def, extend_v, mov_v = 60, 20, 0
        formula = FuncModel.linear(k, b)
        formula_string = "%f*x+%f" % (k, b)
        definition = []

        new_function = Function(formula, definition, formula_string, max_def, extend_v, mov_v)
        return new_function

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%f,%f)" % (self.x, self.y)

    def __sub__(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

class UnitTest:
    def funcModelTest(self):
        fm = FuncModel()
        tf = fm.sin(1,1,0)
        print(tf(pi/2))

if __name__ == '__main__':
    unitest = UnitTest()
    unitest.funcModelTest()