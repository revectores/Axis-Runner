import pygame
from pygame.locals import *
from GlobalData import *
import sys

class Status:
    def timeElapse(self):
        pass
    
    def handle(self,event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    def init(self):
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
            GlobalData.changeStatus(1)

    def init(self):
        self.view.draw(self.model.count)

class TimerStatus(Status):
    def handle(self,event):
        super().handle(event)
        if event.type == KEYDOWN:
            self.model.changeData('zero',23333)
        elif event.type == MOUSEBUTTONDOWN:
            GlobalData.changeStatus(0)
    
    def timeElapse(self):
        self.model.changeData('inc',1)
    
    def init(self):
        self.view.draw(0)
