from math import *
from random import *
from time import time

class Function:
    SCREEN_WIDTH = 800

    def __init__(self, formula, definition, formula_string, max_def, extend_v, mov_v):
        self.formula = formula               # 解析式
        self._definition = definition        # 定义域
        self.points = [Point(x, self.formula(x)) for x in definition]   # 离散点

        self._formula_string = formula_string  # 解析式字符串
        self.expression = self.getExp(formula_string, definition)  # 解析式和定义域字符串
        self.max_def = max_def                # 定义域最大长度
        self.extend_v = extend_v              # 定义域延伸(变化)速度
        self.mov_v = mov_v                    # 函数移动速度矢量
        self.expired_time = time() + (Function.SCREEN_WIDTH + self.max_def)//abs(self.extend_v)

    @staticmethod
    def getExp(formula_string, definition):
        return

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, definition):
        self._definition = definition
        self.expression = self.getExp(self._formula_string, self.definition)
        self.points = [Point(x, self.formula(x)) for x in definition]

    @property
    def max(self):
        return max(self.points, key=lambda point: point.y).y

    @property
    def min(self):
        return min(self.points, key=lambda point: point.y).y


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
    def direction():
        return random() > 0.5

    @staticmethod
    def linear(kr, br):
        k = randint(kr[0], kr[1])
        b = randint(br[0], br[1])
        max_def, extend_v, mov_v = 60, 20, 0

        if FuncRandom.direction():
            definition = range(-max_def, 0)
        else:
            extend_v = -extend_v
            definition = range(Function.SCREEN_WIDTH, Function.SCREEN_WIDTH + max_def)

        formula = FuncModel.linear(k, b)
        formula_string = "%d*x+%d" % (k, b)
        # direction = FuncRandom.direction()
        # y_0, y_w = formula(0), formula(GlobalData.WIDTH)

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
