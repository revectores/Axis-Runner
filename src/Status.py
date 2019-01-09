import pygame
from pygame.locals import *
from View import *
from Model import *
import GlobalData
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


class PersonStatus(Status):
    def __init__(self,model,view):
        super().__init__(model,view)

    def handle(self,event):
        if self.model.lr_mode == 'back' or  self.model.lr_mode == 'normal':
            if event.type == KEYDOWN:
                if event.key == K_a:
                    self.model.lr_mode = 'left'
                elif event.key == K_d:
                    self.model.lr_mode = 'right'
        else:
            if event.type == KEYUP:
                if event.key == K_a:
                    if self.model.lr_mode == 'left':
                        self.model.lr_mode = 'back'
                elif event.key == K_d:
                    if self.model.lr_mode == 'right':
                        self.model.lr_mode = 'back'
        if self.model.mode == 'jump': #跳跃过程中一切操作无用
            return
        if event.type == KEYDOWN:
            if event.key == K_w: #按w挑起
                self.model.mode = 'jump'
            elif event.key == K_s: #按s持续下蹲
                self.model.mode = 'down'              
        elif event.type == KEYUP:
            if event.key == K_s: #松开s站起
                self.model.mode = 'walk'
        
    def timeElapse(self):
        if self.model.mode == 'jump':
            self.model.jumpUpdate()
        if self.model.lr_mode == 'back':
            self.model.backUpdate()
        elif self.model.lr_mode != 'normal':
            self.model.lrUpdate()
        self.model.borderUpdate()

    def init(self):
        self.view.draw([200,200,100,100])
    
    @staticmethod
    def build():
        view = PersonView()
        return PersonStatus(PersonModel(view),view)

class GameStatus(Status):
    def __init__(self,personStatus,axisStatus,model,view):
        super().__init__(model,view)
        self.personStatus,self.axisStatus = personStatus,axisStatus
     
    def timeElapse(self):
        self.view.update('',0)
        self.personStatus.timeElapse()
        self.axisStatus.timeElapse()
        pygame.display.update()
        if self.model.collisionDetection():
            GlobalData.changeStatus(GlobalData.StatusEnum.END_GAME)
    
    def init(self):
        self.view.draw((200,200))
        self.personStatus.init()

    def handle(self,event):
        super().handle(event)
        self.personStatus.handle(event)
    
    @staticmethod
    def build():
        pst = PersonStatus.build()
        ast = AxisStatus.build()
        return GameStatus(pst,ast,GameModel(None,pst.model,ast.model),GameView((196,191,169),pygame.font.SysFont('SimHei', 60),(0,0,0),(20,20)))

class AxisStatus(Status):
    def timeElapse(self):
        self.model.functionUpdate()
    
    @staticmethod
    def build():
        view = AxisView()
        return AxisStatus(AxisModel(view),view)
    