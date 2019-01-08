from Function import *
import GlobalData

#Model表示一个游戏场景所需的局部数据，Model和View的关系是一种基于观察者模式的关系，View对Model进行监听，实时变化
class Model:
    def __init__(self,listener):
        self.listener = listener #这里的listener就是一个View。因为目前并没有Model与多个View相关联的情况，将来如果有可以把listener换成listenerList，简单修改代码即可。

    def changeData(self,type,val):
        pass


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
            return len([point for point in function.points if
                 pm.left < point.x < pm.left + pm.width and pm.top - pm.height < point.y < pm.top])


class PersonModel(Model):
    STAND_HEIGHT = 92  # 人物站立的高度
    DOWN_HEIGHT = 60   # 人物下蹲的高度
    WIDTH = 76          # 人物宽度

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
        self.v_x = 10
        self.v_y = 25
        self._mode = 'walk'
        self.jumpStart = 0
        self.max_border['top'] = self.STAND_HEIGHT + self.v_x ** 2 / GameModel.g
        self.attack_border['top'] = int(self.max_border['top'] * 1.5)
        self.attack_border['bottom'] = -int(self.max_border['bottom'] * 0.5)

    @staticmethod
    def real2screen_x(x):
        pass

    @staticmethod
    def real2screen_y(y):
        return GameModel.SCREEN_HEIGHT - y

    def borderUpdate(self):
        self.listener.update('border', [self.left, self.top, self.width, self.height])

    def modeUpdate(self):
        self.listener.update('mode', self.mode)

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, nextMode):
        self._mode = nextMode
        if nextMode == 'jump':
            self.height = self.STAND_HEIGHT
            self.top = self.STAND_TOP
            self.jumpStart = GlobalData.time

        if nextMode == 'down':
            self.jumpStart = 0
            self.height = self.DOWN_HEIGHT
            self.top = self.DOWN_TOP

        if nextMode == 'walk':
            self.jumpStart = 0
            self.height = self.STAND_HEIGHT
            self.top = self.STAND_TOP

        self.borderUpdate()
        self.modeUpdate() #通知view层换人物贴图。
        #关于轮播图片实现动画的问题这个让view自己管理一个图片列表和索引就好，因为每一帧都会有update请求送过去，每update一次view换图这样就可以。人物脚下的坐标也是同样方法实现。

    def getHeight(self):
        t = GlobalData.time - self.jumpStart
        return self.v_y * t - 1/2 * GameModel.g / 2 * t * t

    def jumpUpdate(self):
        h = self.getHeight()
        if h<=0:
            self.mode = 'walk'
            return
        self.top -= h
        self.borderUpdate()
        self.top +=h
        #if GlobalData.time - self.jumpStart >= 2 * self.v_y/GameModel.g:

    def maintain(self): #如果当前帧什么事件都没发生怎么办？
        self.listener.update('maintain', None) #view更新一下轮播贴图和人物坐标就行。


class AxisModel(Model):
    EXPRESSION = "%s, %d<x<%d"

    def __init__(self, listener):
        super().__init__(listener)
        self.functionList = []

    @staticmethod
    def getPosition():
        return GlobalData.speed * GlobalData.time

    @staticmethod
    def rangeBias(origin, bias):
        return range(origin[0] + bias, origin[-1] + bias)

    @staticmethod
    def realExp(function):
        rangeBias(function.definition, getPosition())
        form = function.formula_string.replace('x', '(x-%d)' % getPosition())
        real_def = rangeBias(function.definition, getPosition())
        return self.EXPRESSION % form, real_def[0], real_def[-1]

    def functionUpdate(self):
        for function in self.functionList:
            if function.expired_time > time():
                self.functionList.remove(function)
                continue

            fun_expression = realExp(function)
            function.definition = rangeBias(function.definition, funciton.extend_v)
            self.listener.update(fun_expression, function.points)

    def newLinear(self):
        kr = [-100, 100]
        br = [-PersonModel.STAND_HEIGHT//2, PersonModel.STAND_HEIGHT]  # 限制b的范围, 保证生成的直线对玩家存在威胁
        new_linear = FuncRandom.linear(kr, br)
        return new_linear


class UnitTest:
    def axisTest(self):
        axisModel = AxisModel(1)
        new_linear = axisModel.newLinear()
        prn_obj(new_linear)
        print([(point.x, point.y) for point in new_linear.points])


if __name__ == '__main__':
    def prn_obj(obj):
        print('\n'.join(['%s: %s' % item for item in obj.__dict__.items()]))

    unitTest = UnitTest()
    unitTest.axisTest()