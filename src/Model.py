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
    STAND = 233 #常量，人物站立的高度，随便改
    DOWN = 23 #常量，人物下蹲的高度，随便改

    def __init__(self,listener,top,left,height,width):
        super().__init__(listener)
        self.top = 0
        self.left = 0
        self.height = 0
        self.width = 0
        self.v_x = 0
        self.v_y = 0
        self._mode = 'walk'
        self.jumpTime = 0

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self,nextMode):
        self._mode = nextMode
        #jump的时候其实什么都不用干
        if nextMode == 'down':
            #TODO:人物身体高度设为下蹲值
        elif nextMode == 'walk':
            #TODO:人物身体高度设为正常值
        listener.update('mode',nextMode) #通知view层换人物贴图。
        #关于轮播图片实现动画的问题这个让view自己管理一个图片列表和索引就好，因为每一帧都会有update请求送过去，每update一次view换图这样就可以。人物脚下的坐标也是同样方法实现。

    def getHeight(self):
        g = 9.8
        t = self.jumpTime
        return self.v_y * t - 1/2 * g * t**2

    def jumpUpdate(self):
        h = self.getHeight(self.jumpTime)
        if self.jumpTime > 0 and h <= 0:
            self.mode = 'walk'
            self.height = 0
            listener.update('jstop',None) #通知view层改人物位置并且换贴图。
        else:
            self.height = h
            listener.update('height',h) #通知view层改人物位置
    
    def maintain(self): #如果当前帧什么事件都没发生怎么办？
        listener.update('maintain',None) #view更新一下轮播贴图和人物坐标就行。

class AxisModel(Model):
    def __init__(self,listener):
        super().__init__(listener)
        self.position = 0
        self.functionList = []

    @staticmethod
    def newFunction(self):
        funcModel = FuncModel()
        newFun = funcModel.linear(1,1)
        fun = Function(newFun, range(-10,10))
        return fun


class UnitTest:
    def AxisModelTest(self):
        funcModel = FuncModel()
        newFun = funcModel.exp(2.5)
        fun = Function(newFun, range(-10,10))
        return fun

if __name__ == '__main__':
    unitest = UnitTest()
    fun = unitest.AxisModelTest()
    [print(point) for point in fun.points]