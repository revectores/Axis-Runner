from GlobalData import *
import pygame

class View:
    def draw(self,arg):
        pass

    def update(self,type,val):
        pass
       
class TextView(View):
    def __init__(self,bgColor = (0,0,200),fontColor = (255,255,255)):
        self.bgColor,self.fontColor = bgColor,fontColor
    
    def draw(self,arg):
        GlobalData.screen.fill(self.bgColor)
        GlobalData.screen.blit(pygame.font.Font(None,60).render(str(arg),True,self.fontColor),(100,100))
        pygame.display.update()

    def update(self,type,val):
        GlobalData.screen.fill(self.bgColor)
        GlobalData.screen.blit(pygame.font.Font(None,60).render(str(val),True,self.fontColor),(100,100))
        pygame.display.update()