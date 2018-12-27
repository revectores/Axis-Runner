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
