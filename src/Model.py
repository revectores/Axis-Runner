from Function import *
from View import *

#Model表示一个游戏场景所需的局部数据，Model和View的关系是一种基于观察者模式的关系，View对Model进行监听，实时变化
class Model:
    def changeData(self,type,val):
        pass

    def notify(self):
        self.listener.
    
    def __init__(self,listener):
        self.listener = listener #这里的listener就是一个View。因为目前并没有Model与多个View相关联的情况，将来如果有可以把listener换成listenerList，简单修改代码即可。

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
        self.listener.update('',self.time)

class PersonModel(Model):
    STAND_HEIGHT = 233 #常量，人物站立的高度，随便改
    DOWN_HEIGHT = 23 #常量，人物下蹲的高度，随便改
    WIDTH = 50

    STAND_TOP = GlobalData.hegiht/2 - STAND_HEIGHT
    DOWN_TOP = GlobalData.hegiht/2 - DOWN_HEIGHT
    LEFT = GlobalData.width/2 - WIDTH/2

    def __init__(self,listener,top,left,height,width):
        super().__init__(listener)
        self.top = self.STAND_TOP
        self.left = self.LEFT
        self.height = self.STAND_HEIGHT
        self.width = self.WIDTH
        self.v_x = 10
        self.v_y = 10
        self._mode = 'walk'
        self.jumpStart = 0

    def borderUpdate(self):
        self.listener.update('border',[self.top, self.left, self.height, self.width])

    def modeUpdate(self):
        self.listener.update('mode',self.mode)

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
            self.top = 0

        self.borderUpdate()
        self.modeUpdate() #通知view层换人物贴图。
        #关于轮播图片实现动画的问题这个让view自己管理一个图片列表和索引就好，因为每一帧都会有update请求送过去，每update一次view换图这样就可以。人物脚下的坐标也是同样方法实现。

    def getHeight(self):
        g = 9.8
        t = GlobalData.t - self.jumpStart
        return self.v_y * t - 1/2 * g * t**2

    def jumpUpdate(self):
        g = 9.8
        self.height = self.getHeight()
        self.borderUpdate()
        if GlobalData.t - self.jumpStart >= 2*self.v_y/g:
            self.mode = 'walk'

    def maintain(self): #如果当前帧什么事件都没发生怎么办？
        self.listener.update('maintain',None) #view更新一下轮播贴图和人物坐标就行。

class AxisModel(Model):
    def __init__(self,listener):
        super().__init__(listener)
        self.position = 0
        self.functionList = []

class UnitTest:
    pass

if __name__ == '__main__':
    pass