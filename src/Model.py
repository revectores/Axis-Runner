from Function import *

#Model表示一个游戏场景所需的局部数据，Model和View的关系是一种基于观察者模式的关系，View对Model进行监听，实时变化
class Model:
    def __init__(self,listener):
        self.listener = listener #这里的listener就是一个View。因为目前并没有Model与多个View相关联的情况，将来如果有可以把listener换成listenerList，简单修改代码即可。

    def changeData(self,type,val):
        pass

class CounterModel(Model):
    def __init__(self,listener,count):
        super().__init__(listener)
        self.count = count
    
    def changeData(self,type,arg): #数据改变的时候就调用这个函数，type表示数据改变的类型（字符串），arg是这次数据改变所需的参数
        if type == 'add':
            self.count += arg
        self.listener.update('',self.count) #通知监听者

class TimerModel(Model):
    def __init__(self,listener):
        super().__init__(listener)
        self.time = 0
     
    def changeData(self,type,val): #能看懂上一个Model，看懂这个不难。
        if type == 'inc':
            self.time += val
        elif type == 'zero':
            self.time = 0
        self.listener.update('', self.time)


class GameModel(Model):
    SCREEN_HEIGHT = 0
    SCREEN_WIDTH = 0
    g = 9.8

    def __init__(self,listener, personModel, axisModel):
        super().__init__(listener)
        self.personModel = personModel
        self.axisModel = axisModel

    def collsionDetection(self):
        pm = self.personModel
        for function in self.axisModel.functionList:
            return len([point for point in function.points if
                 pm.left < point.x < pm.left + pm.width and pm.top - pm.height < point.y < pm.top])


class PersonModel(Model):
    STAND_HEIGHT = 100  # 人物站立的高度
    DOWN_HEIGHT = 50    # 人物下蹲的高度
    WIDTH = 50          # 人物宽度

    STAND_TOP = GameModel.SCREEN_HEIGHT/2 - STAND_HEIGHT   # 正常站立的人物头部边界
    DOWN_TOP = GameModel.SCREEN_HEIGHT/2 - DOWN_HEIGHT     # 下蹲的任务头部边界
    LEFT = GameModel.SCREEN_WIDTH/2 - WIDTH/2

    max_border = {'top': 0, 'button': 0, 'left': LEFT, 'right': LEFT + WIDTH}

    def __init__(self,listener, top, left, height, width):
        super().__init__(listener)
        self.top = self.STAND_TOP
        self.left = self.LEFT
        self.height = self.STAND_HEIGHT
        self.width = self.WIDTH
        self.v_x = 10
        self.v_y = 10
        self._mode = 'walk'
        self.jumpStart = 0
        self.max_border['top'] = self.STAND_HEIGHT + self.v_x**2/GameModel.g

    def borderUpdate(self):
        self.listener.update('border', [self.top, self.left, self.height, self.width])

    def modeUpdate(self):
        self.listener.update('mode', self.mode)

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, nextMode):
        self._mode = nextMode
        if nextMode == 'jump':
            pass

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
        t = GlobalData.t - self.jumpStart
        return self.v_y * t - 1/2 * GameModel.g * t**2

    def jumpUpdate(self):
        g = 9.8
        self.height = self.getHeight()
        self.borderUpdate()
        if GlobalData.t - self.jumpStart >= 2*self.v_y/GameModel.g:
            self.mode = 'walk'

    def maintain(self): #如果当前帧什么事件都没发生怎么办？
        self.listener.update('maintain', None) #view更新一下轮播贴图和人物坐标就行。


class AxisModel(Model):
    EXPRESSION = "%s, %d<x<%d"

    def __init__(self, listener):
        super().__init__(listener)
        self.functionList = []

    @staticmethod
    def getPosition():
        return GlobalData.speed * GlobalData.t

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
