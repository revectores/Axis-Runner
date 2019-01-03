import pygame
from pygame.locals import *
from GlobalData import *
import sys

class Status: #Status表示一个游戏场景，本质就是MVC设计模式中的Controller
    def timeElapse(self): #当时间流逝时，当前状态可能会发生变化
        pass
    
    def handle(self,event): #事件处理函数
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    def init(self): #游戏状态初始化
        pass
    
    @staticmethod
    def build(): #工厂方法
        pass

    def __init__(self,model,view):
        self.model = model
        self.view = view

class CounterStatus(Status):
    def handle(self,event):
        super().handle(event)
        if event.type == KEYDOWN:
            self.model.changeData('add',1)
        elif event.type == MOUSEBUTTONDOWN:
            GlobalData.changeStatus(1) #更改状态

    def init(self):
        self.view.draw(self.model.count) #初始化时通知view完成最初的绘制

class TimerStatus(Status):
    def handle(self,event):
        super().handle(event)
        if event.type == KEYDOWN:
            self.model.changeData('zero',23333)
        elif event.type == MOUSEBUTTONDOWN:
            GlobalData.changeStatus(0)
    
    def timeElapse(self): #时间流逝时计时器数字变化
        self.model.changeData('inc',1)
    
    def init(self):
        self.view.draw(0)

class PersonStatus(Status):
    def handle(self,event):
        if self.model.mode == 'jump': #跳跃过程中一切操作无用
            return
        if event.type == KEYDOWN:
            if event.key == K_w: #按w挑起
                self.model.mode('jump')
            elif event.key == K_s: #按s持续下蹲
                self.model.mode('down')               
        elif event.type == KEYUP:
            if event.key == K_s: #松开s站起
                self.model.mode('walk')
        
    def timeElapse(self):
        if self.model.mode == 'jump':
            self.model.jumpUpdate()
        else:
            self.model.maintain()

    def init(self):
        self.view.draw()

class AxisStatus(Status):
    def handle(self,event):
        pass

    def timeElapse(self):
        self.model.functionUpdate()

    def init(self):
        pass

class ComposedStatus(Status):
    def __init__(self,subStatusList,model,view):
        self.subStatusList,self.model,self.view = subStatusList,model,view

    def handle(self,event):
        super().handle(event)
        for s in self.subStatusList:
            s.handle(event)
    
    def timeElapse(self):
        for s in self.subStatusList:
            s.timeElapse()
    
    def init(self):
        for s in self.subStatusList:
            s.init()
        self.model.init()

class GameStatus(ComposedStatus):
    def timeElapse(self):
        super().timeElapse()
        if self.model.collisionDetection():
            GlobalData.changeStatus(GlobalData.StatusEnum.END_GAME)
        
    