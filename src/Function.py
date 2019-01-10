from math import *
from random import *
from time import time
from Model import *
import GlobalData

class Function:
    SCREEN_WIDTH = 640

    def __init__(self, formula, definition, formula_string, max_def, extend_v, mov_v):
        self.formula = formula               # 解析式
        self._definition = definition        # 定义域
        self.points = [Point(x, self.formula(x)) for x in definition]   # 离散点

        self._formula_string = formula_string  # 解析式字符串
        self.max_def = max_def                # 定义域最大长度
        self.extend_v = extend_v              # 定义域延伸(变化)速度
        self.mov_v = mov_v                    # 函数移动速度矢量
        self.expired_time = GlobalData.time + (Function.SCREEN_WIDTH + self.max_def)/abs(self.extend_v)
        #print(time(), self.expired_time)
        #print(self._formula_string)

    def getRealExp(self, x_position):
        fstr = self._formula_string.replace('x', '(x-%d)' % x_position)
        #print(self.definition)
        dstr = '%d<x<%d' % (self.definition[0] + x_position, self.definition[-1] + x_position)
        return "%s, %s" % (fstr, dstr)

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, definition):
        self._definition = definition
        self.points = [Point(x, self.formula(x)) for x in definition]

    @property
    def max(self):
        return max(self.points, key=lambda point: point.y).y

    @property
    def min(self):
        return min(self.points, key=lambda point: point.y).y


class BasicFunction:
    def __init__(self, formula, expression):
        self.formula = formula
        self.expression = expression

    def __add__(self, other):
        new_formula = lambda x: self.formula(x) + other.formula(x)
        new_expression = "(%s) + (%s)" % (self.expression, other.expression)
        return BasicFunction(new_formula, new_expression)

    def __sub__(self, other):
        new_formula = lambda x: self.formula(x) - other.formula(x)
        new_expression = "(%s) - (%s)" % (self.expression, other.expression)
        return BasicFunction(new_formula, new_expression)

    def __mul__(self, other):
        new_formula = lambda x: self.formula(other.formula(x))
        new_expression = self.expression.replace('x', "(%s)" % other.expression)
        return BasicFunction(new_formula, new_expression)


class FuncModel:
    FUNC_TYPE = 4
    eq = lambda x: x

    @staticmethod
    def linear(para, f=eq, s='x'):
        k, b = para
        formula = lambda x: k * f(x) + b
        expression = "%f*%s+%f" % (k, s, b)
        return BasicFunction(formula, expression)

    @staticmethod
    def exp(para, f=eq, s='x'):
        base = para[0]
        formula = lambda x: base ** f(x)
        expression = "%f**%s" % (base, s)
        return BasicFunction(formula, expression)

    @staticmethod
    def power(para, f=eq, s='x'):
        exp = para[0]
        formula = lambda x: int(f(x) ** exp)
        expression = "%s**%f" % (s, exp)
        return BasicFunction(formula, expression)

    @staticmethod
    def sin(para, f=eq, s='x'):
        formula = lambda x: sin(f(x))
        expression = "sin(%s)" % s
        return BasicFunction(formula, expression)

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
        formula = FuncModel.linear([k, b], exp1)
        # direction = FuncRandom.direction()
        # y_0, y_w = formula(0), formula(GlobalData.WIDTH)

        # new_function = Function(formula, definition, formula_string, max_def, extend_v, mov_v)
        # return new_function

    @staticmethod
    def randomUnit():
        funcMap = [
            lambda para: FuncModel.linear(para),
            lambda para: FuncModel.exp(para),
            lambda para: FuncModel.power(para),
            lambda para: FuncModel.sin(para)
        ]
        paraMap = [
            [randint(-1, 1), randint(-1, 1)],
            [randint(1, 1)],
            [randint(1, 1)],
            [randint(-2, 2)],
        ]

        r = randint(0, 3)
        #r = 0
        return funcMap[r](paraMap[r])

    @staticmethod
    def random(layer):
        if layer == 1: return BasicFunction(lambda x: x, 'x')
        composeMap = [
            lambda f1, f2: f1 + f2,
            lambda f1, f2: f1 - f2,
            lambda f1, f2: f1 * f2
        ]
        r = randint(0, 2)
        return composeMap[r](FuncRandom.randomUnit(), FuncRandom.random(layer-1))

    @staticmethod
    def adjust(fun):
        player_x = Function.SCREEN_WIDTH//2
        y_0 = fun.formula(player_x)
        #b = randint(PersonModel.attack_border['bottom'], PersonModel.attack_border['top'])
        b = randint(80, 200)
        adjust_linear = FuncModel.linear([0, b-y_0], lambda x: x, 'x')
        return fun + adjust_linear


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%f,%f)" % (self.x, self.y)

    def __sub__(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5


class UnitTest:
    def funcComposeTest(self):
        funcModel = FuncModel()
        linear1 = FuncModel.linear([1, 2])
        linear2 = FuncModel.linear([2, 3])
        print((linear1*linear2).formula(1))

    def randomFunTest(self):
        funcModel = FuncModel()
        rand_fun = FuncRandom.random(3)
        print(rand_fun.expression)
        print(rand_fun.formula(1))

    def funAdjustTest(self):
        rand_fun = FuncRandom.random(3)
        adjust_rand_fun = FuncRandom.adjust(rand_fun)

        print(rand_fun.expression)
        print(rand_fun.formula(Function.SCREEN_WIDTH//2))

        print(adjust_rand_fun.expression)
        print(adjust_rand_fun.formula(Function.SCREEN_WIDTH//2))


if __name__ == '__main__':
    unitest = UnitTest()
    # unitest.funcComposeTest()
    unitest.funAdjustTest()
