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
    eq = lambda x: x

    @staticmethod
    def linear(para, f=eq):
        k, b = para
        return lambda x: k * f(x) + b

    @staticmethod
    def exp(para, f=eq):
        base = para[0]
        return lambda x: base ** f(x)

    @staticmethod
    def power(para, f=eq):
        exp = para[0]
        return lambda x: f(x) ** exp

    @staticmethod
    def sin(f=eq):
        return lambda x: sin(f(x))

    @staticmethod
    def arcsin():
        pass


class FuncStrModel:
    @staticmethod
    def linear(para, str):
        k, b = para
        return "%d*%s+%d" % (k, str, b)

    @staticmethod
    def exp(para, str):
        base = para[0]
        return "%d**%s" % (base, str)

    @staticmethod
    def power(para, str):
        exp = para[0]
        return "%s**%d" % (str, exp)

    @staticmethod
    def sin(para, str):
        return "sin(%s)" % (str)

    @staticmethod
    def arcsin():
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

        exp1 = FuncModel.exp([2])
        exp2 = FuncStrModel.exp(2, 'x')
        formula = FuncModel.linear([k, b], exp1)
        formula_string = FuncStrModel.linear([k, b], exp2)
        # direction = FuncRandom.direction()
        # y_0, y_w = formula(0), formula(GlobalData.WIDTH)

        new_function = Function(formula, definition, formula_string, max_def, extend_v, mov_v)
        return new_function

    @staticmethod
    def simpleRandom():
        r = random()

    @staticmethod
    def random():
        pass


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
        pass

if __name__ == '__main__':
    unitest = UnitTest()
    unitest.funcModelTest()
