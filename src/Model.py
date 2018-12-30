#Model表示一个游戏场景所需的局部数据，Model和View的关系是一种基于观察者模式的关系，View对Model进行监听，实时变化
class Model:
    def changeData(self,type,val):
        pass

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
        if nextMode == 'jump':
            pass
        if nextMode == 'down':
            pass
        if nextMode == 'walk':
            pass

    @staticmethod
    def getHeight(self):
        g = 9.8
        t = self.jumpTime
        return self.v_y * t - 1/2 * g * t**2

    @staticmethod
    def jumpUpdate(self):
        h = self.getHeight(self.jumpTime)
        if self.jumpTime > 0 and h <= 0:
            self.mode = 'walk'
        self.heihgt = h

class AxisModel(Model):
    def __init__(self,listener):
        super().__init__(listener)


# class EnvironmentModel(Model):
#     def __init__(self,listener):
#         super().__init__(listener)

