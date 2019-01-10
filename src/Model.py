from Function import *
import GlobalData
from random import random, randint
from math import log

#Model表示一个游戏场景所需的局部数据，Model和View的关系是一种基于观察者模式的关系，View对Model进行监听，实时变化
class Model:
    def __init__(self,listener):
        self.listener = listener #这里的listener就是一个View。因为目前并没有Model与多个View相关联的情况，将来如果有可以把listener换成listenerList，简单修改代码即可。

    def changeData(self,type,val):
        pass


class ButtonResponseModel(Model):
    def changeData(self,type,val):
        self.mode = type
        self.listener.update(type,None)
    
    def __init__(self,listener,mode):
        super().__init__(listener)
        self.mode = mode


class GameModel(Model):
    SCREEN_HEIGHT = 480
    SCREEN_WIDTH = 640
    g = 9.8

    def __init__(self,listener, personModel, axisModel):
        super().__init__(listener)
        self.personModel = personModel
        self.axisModel = axisModel

    def collisionDetection(self):
        pm = self.personModel
        for function in self.axisModel.functionList:
            print(pm.left, pm.top)
            print([(point.x, point.y) for point in function.points if
                 pm.left < point.x < pm.left + pm.width and pm.top < point.y < pm.top + pm.height])
            return len([point for point in function.points if
                 pm.left < point.x < pm.left + pm.width and pm.top < point.y < pm.top + pm.height])


class OptionModel(ButtonResponseModel):
    def __init__(self,listener,val):
        super().__init__(listener,val)
        self.sound = ['Sound:On','Sound:Off']
        self.level = ['Level:Linear','Level:Quadratic','Level:Cubic']
        self.sNum = 0
        self.lNum = 1
        self.flag = 0


class PersonModel(Model):
    STAND_HEIGHT = 92  # 人物站立的高度
    DOWN_HEIGHT = 60   # 人物下蹲的高度
    WIDTH = 76         # 人物宽度

    STAND_TOP = GameModel.SCREEN_HEIGHT/2 - STAND_HEIGHT   # 正常站立的人物头部边界
    DOWN_TOP = GameModel.SCREEN_HEIGHT/2 - DOWN_HEIGHT     # 下蹲的人物头部边界
    LEFT = GameModel.SCREEN_WIDTH/2 - WIDTH/2

    max_border = {'top': 0, 'bottom': 0, 'left': LEFT, 'right': LEFT + WIDTH}
    attack_border = {'top': 150, 'bottom': -50, 'left': LEFT, 'right': LEFT + WIDTH}

    def __init__(self, listener):
        super().__init__(listener)
        self.top = self.STAND_TOP
        self.left = self.LEFT
        self.height = self.STAND_HEIGHT
        self.width = self.WIDTH
        self.v_x = 15
        self.v_y = 35
        self._mode = 'walk'
        self._lr_mode = 'normal'
        self.jumpStart = 0
        self.lrStart = 0
        self.max_border['top'] = self.STAND_HEIGHT + self.v_x ** 2 / GameModel.g
        self.attack_border['top'] = int(self.max_border['top'] * 1.5)
        self.attack_border['bottom'] = -int(self.max_border['bottom'] * 0.5)

#    @staticmethod
#    def real2screen_x(x):
#        pass

#    @staticmethod
#    def real2screen_y(y):
#        return GameModel.SCREEN_HEIGHT - y

    def borderUpdate(self):
        self.listener.update('border', [self.left, self.top, self.width, self.height])

    def modeUpdate(self):
        self.listener.update('mode', self.mode)

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, nextMode):
        lastMode = self._mode
        self._mode = nextMode
        if nextMode == 'walk':
            self.jumpStart = 0
            self.lrStart = 0
            self.height = self.STAND_HEIGHT
            self.top = self.STAND_TOP

        if nextMode == 'down':
            self.jumpStart = 0
            self.height = self.DOWN_HEIGHT
            self.top = self.DOWN_TOP

        if nextMode == 'jump':
            self.height = self.STAND_HEIGHT
            self.top = self.STAND_TOP
            self.jumpStart = GlobalData.time

        #self.borderUpdate()
        self.modeUpdate() #通知view层换人物贴图。
        #关于轮播图片实现动画的问题这个让view自己管理一个图片列表和索引就好，因为每一帧都会有update请求送过去，每update一次view换图这样就可以。人物脚下的坐标也是同样方法实现。

    @property
    def lr_mode(self):
        return self._lr_mode

    @lr_mode.setter
    def lr_mode(self, nextMode):
        lastMode = self._lr_mode
        self._lr_mode = nextMode
        if nextMode == 'left':
            self.lrStart = GlobalData.time

        if nextMode == 'right':
            self.lrStart = GlobalData.time

        if nextMode == 'back':
            if lastMode == 'left':
                self.left = self.LEFT

            if lastMode == 'right':
                self.left = self.LEFT

    def getHeight(self):
        t = GlobalData.time - self.jumpStart
        return self.v_y * t - 1/2 * GameModel.g / 2 * t * t

    def jumpUpdate(self):
        h = self.getHeight()
        if h <= 0:
            self.mode = 'walk'
            return
        self.top = GameModel.SCREEN_HEIGHT/2 - self.height - h
        #self.borderUpdate()
        #if GlobalData.time - self.jumpStart >= 2 * self.v_y/GameModel.g:

    def getLR(self):
        t = GlobalData.time - self.lrStart
        return self.v_x*log((abs(self.left - self.LEFT) + 3))

    def lrUpdate(self):
        r = self.getLR()
        self.left = GameModel.SCREEN_WIDTH/2 - self.width/2 - (r if self.lr_mode == 'left' else -r)
        #self.borderUpdate()

    def backUpdate(self):
        r = self.getLR()


class AxisModel(Model):
    EXPRESSION = "%s, %d<x<%d"

    def __init__(self, listener):
        super().__init__(listener)
        self.functionList = []
        self.lastNew = GlobalData.time
        if GlobalData.level == 'Level:Linear':
            self.internalTime = 150
        elif GlobalData.level == 'Level:Quadratic':
            self.internalTime = 100
        else:
            self.internalTime = 50

    @staticmethod
    def getPosition():
        return GlobalData.speed * GlobalData.time

    @staticmethod
    def rangeBias(origin, bias):
        return range(origin[0] + bias, origin[-1] + bias + 1)

    @staticmethod
    def realExp(function):
        rangeBias(function.definition, getPosition())
        form = function.formula_string.replace('x', '(x-%d)' % getPosition())
        real_def = rangeBias(function.definition, getPosition())
        return self.EXPRESSION % form, real_def[0], real_def[-1]

    def functionUpdate(self):
        # if len(self.functionList) < DMAP[0]['function_num']:
        if GlobalData.time > self.lastNew + self.internalTime:
            print(len(self.functionList))
            self.newFunction()
            self.lastNew = GlobalData.time
            print([(point.x, point.y) for point in self.functionList[0].points])

        for function in self.functionList:
            if GlobalData.time > function.expired_time:
                self.functionList.remove(function)
                print('!!!!!!')
                continue

            fun_expression = function.getRealExp(self.getPosition())
            function.definition = self.rangeBias(function.definition, function.extend_v)
            self.listener.update(fun_expression, function.points)

    def newLinear(self):
        kr = [-100, 100]
        br = [-PersonModel.STAND_HEIGHT//2, PersonModel.STAND_HEIGHT]  # 限制b的范围, 保证生成的直线对玩家存在威胁
        new_linear = FuncRandom.linear(kr, br)
        return new_linear

    def newFunction(self):
        power1 = FuncModel.linear([0.5, 0]) * FuncModel.power([2]) * FuncModel.linear([1, -320])
        power2 = FuncModel.linear([0.005, randint(-1000, -300)]) * FuncModel.power([2])
        power3 = FuncModel.linear([0.001, randint(-1000, 200)]) * FuncModel.power([2])
        sin1 = FuncModel.linear([100, 100]) * FuncModel.sin([1]) * FuncModel.linear([0.01, randint(-100, 300)])
        exp1 = FuncModel.linear([1,0]) * FuncModel.exp([2]) * FuncModel.linear([1,0])
        print(sin1.expression)
        basic_fun = sin1
        # basic_fun = FuncRandom.adjust(FuncRandom.random(3))
        formula = basic_fun.formula
        formula_string = basic_fun.expression
        max_def = 200
        if random() > 0.5:
            extend_v = randint(5, 10)
            definition = range(-max_def, 0)
        else:
            extend_v = randint(-10, -5)
            definition = range(GameModel.SCREEN_WIDTH, GameModel.SCREEN_WIDTH + max_def)
        newFun = Function(formula, definition, formula_string, max_def, extend_v, 0)
        self.functionList.append(newFun)
        return True


class UnitTest:
    def axisTest(self):
        axisModel = AxisModel(1)
        axisModel.newFunction()
        prn_obj(axisModel.functionList[0])
        print([(point.x, point.y) for point in axisModel.functionList[0].points])


if __name__ == '__main__':
    def prn_obj(obj):
        print('\n'.join(['%s: %s' % item for item in obj.__dict__.items()]))

    unitTest = UnitTest()
    unitTest.axisTest()
