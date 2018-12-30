from GlobalData import *
import pygame

class View:
    def draw(self,arg): #初始状态绘制
        pass

    def update(self,type,val): #实时更新
        pass
       
class TextView(View):
    def __init__(self,bgColor = (0,0,200),fontColor = (255,255,255)):
        self.bgColor,self.fontColor = bgColor,fontColor
    
    def draw(self,arg):
        GlobalData.screen.fill(self.bgColor)
        GlobalData.screen.blit(pygame.font.Font(None,60).render(str(arg),True,self.fontColor),(100,100))
        pygame.display.update() #写什么都别忘了update，要不然屏幕不会更新

    def update(self,type,val):
        GlobalData.screen.fill(self.bgColor)
        GlobalData.screen.blit(pygame.font.Font(None,60).render(str(val),True,self.fontColor),(100,100)) #其实没有必要重绘整个画面，如果速度太慢可以优化。
        pygame.display.update()

class PersonView(View):
    def __init__(self):
        pass

    def draw(self):
        pygame.display.update()

    def update(self):
        pygame.display.update()

class AxisView(View):
    def __init__(self):
        pass

    def draw(self):
        pygame.display.update()

    def update(self):
        pygame.display.update()