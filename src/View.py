import GlobalData
import pygame

class View:
    def draw(self, arg):  # 初始状态绘制
        pass
    
    def update(self,type,val):
        pass


class GameView(View):
    def __init__(self,bgColor,font,fontColor,pos):
        self.bgColor,self.font,self.fontColor,self.pos = bgColor,font,fontColor,pos
    
    def draw(self,arg):
        GlobalData.screen.fill(self.bgColor)
        GlobalData.screen.blit(self.font.render('得分：0',True,self.fontColor),self.pos)
        pygame.display.update()
    
    def update(self,type,val):
        GlobalData.screen.fill(self.bgColor)
        GlobalData.screen.blit(self.font.render('得分：%d' % (GlobalData.time),True,self.fontColor),self.pos)


class PersonView(View):
    def draw(self,arg):
        self.border = arg
        self.mode = 'walk'
        pygame.draw.rect(GlobalData.screen,[100,100,100],arg)

    def update(self,type,val):
        if type == 'border':
            self.border = val
            pygame.draw.rect(GlobalData.screen,[100,100,100],val)
            GlobalData.screen.blit(pygame.font.SysFont('SimHei',60).render(self.mode,True,[100,100,100]),(200,200))
        elif type == 'maintain':
            pygame.draw.rect(GlobalData.screen,[100,100,100],self.border)
            GlobalData.screen.blit(pygame.font.SysFont('SimHei',60).render(self.mode,True,[100,100,100]),(200,200))
        elif type == 'mode':
            self.mode = val
            pygame.draw.rect(GlobalData.screen,[100,100,100],self.border)
            GlobalData.screen.blit(pygame.font.SysFont('SimHei',60).render(val,True,[100,100,100]),(200,200))

    def __init__(self,border = 0,mode = 0):
        self.border,self.mode = border,mode