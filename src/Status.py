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

class StartStatus(Status):
    def handle(self,event):
        super().handle(event)
        if event.type == MOUSEBUTTONDOWN:
            print(self.model.mode)
            if self.model.mode == 'exit':
                pygame.quit()
                sys.exit()
            elif self.model.mode == 'start':
                GlobalData.changeStatus(GlobalData.statusDict['main'])
            elif self.model.mode == 'option':
                GlobalData.changeStatus(GlobalData.statusDict['option'])

    def init(self):
        self.view.draw(None)
        pygame.display.update()
    
    def timeElapse(self):
        mouse = pygame.mouse.get_pos()
        if 290*4//5+200*4//5 > mouse[0] > 290*4//5 and 265*4//5 +50*4//5 >mouse[1] > 265*4//5:#改
            self.model.changeData('start',None)
        elif 290*4//5+200*4//5 > mouse[0] > 290*4//5 and 365*4//5 + 50*4//5 >mouse[1] >365*4//5:
            self.model.changeData('exit',None)
        elif 290*4//5+200*4//5 > mouse[0] > 290*4//5 and 465*4//5 + 50*4//5 >mouse[1] >465*4//5:
            self.model.changeData('option',None)
        else:
            self.model.changeData('normal',None)
        pygame.display.update()

    @staticmethod
    def build():
        view = StartView()
        return StartStatus(ButtonResponseModel(view,'normal'),view)


class GameOverStatus(Status):
    def handle(self,event):
        super().handle(event)
        if event.type == MOUSEBUTTONDOWN:
            if self.model.mode == 'res':
                GlobalData.changeStatus(GlobalData.statusDict['main'])
            elif self.model.mode == 'ret':
                GlobalData.changeStatus(GlobalData.statusDict['start'])
    
    def init(self):
        self.view.draw(None)
        pygame.display.update()

    def timeElapse(self):
        mouse = pygame.mouse.get_pos()
        if 100*4//5+200*4//5 > mouse[0] > 100*4//5 and 350*4//5 +50*4//5 >mouse[1] > 350*4//5:#改
            self.model.changeData('res',None)
        elif 405*4//5+300*4//5 > mouse[0] > 405*4//5 and 350*4//5 + 50*4//5 >mouse[1] >350*4//5:
            self.model.changeData('ret',None)
        else:
            self.model.changeData('normal',None)
        pygame.display.update() 
    
    @staticmethod
    def build():
        view = GameOverView()
        return GameOverStatus(ButtonResponseModel(view,'normal'),view)


class OptionStatus(Status):
    def init(self):
        self.view.draw(None)
        pygame.display.update()
    
    def timeElapse(self):
        mouse = pygame.mouse.get_pos()
        if 510 * 4 // 5 > mouse[0] > 290 * 4 // 5 and 315 * 4 // 5 > mouse[1] > 265* 4 // 5 :
            self.model.changeData('sound',None)
        elif 510 * 4 // 5 > mouse[0] > 290 * 4 // 5 and 415 * 4 // 5 > mouse[1] > 365* 4 // 5 :
            self.model.changeData('level',None)
        elif 510* 4 // 5  > mouse[0] > 290* 4 // 5  and 515* 4 // 5  > mouse[1] > 465* 4 // 5 :
            self.model.changeData('ret',None) 
        else:
            self.model.changeData('normal',None)
        pygame.display.update()

    def handle(self,event):
        super().handle(event)
        if event.type == MOUSEBUTTONDOWN:
            if not self.model.flag:
                if self.model.mode == 'sound':
                    self.model.flag = 1
                    self.model.sNum = (self.model.sNum + 1) % 2
                    GlobalData.sound = self.model.sound[self.model.sNum]
                    if GlobalData.sound == 'Sound:Off':
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.play()
                elif self.model.mode == 'level':
                    self.model.flag = 1
                    self.model.lNum = (self.model.lNum + 1) % 3
                    GlobalData.level = self.model.level[self.model.lNum]
                    GlobalData.statusList[GlobalData.statusDict['main']] = GameStatus.build()
                elif self.model.mode == 'ret':
                    GlobalData.fromOption = 1
                    GlobalData.changeStatus(GlobalData.statusDict['start'])
        elif event.type == MOUSEBUTTONUP:
            if self.model.flag:
                self.model.flag = 0
        
    @staticmethod
    def build():
        view = OptionView()
        return OptionStatus(OptionModel(view,'normal'),view)


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
            GlobalData.score = GlobalData.time
            GlobalData.time = 0
            GlobalData.f = 30
            GlobalData.statusList[GlobalData.statusDict['main']] = GameStatus.build()
            GlobalData.changeStatus(GlobalData.statusDict['gameover'])
    
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
    