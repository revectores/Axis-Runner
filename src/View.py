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
        pygame.draw.rect(GlobalData.screen,(70,70,70),(0,230,570,10))
        pygame.draw.polygon(GlobalData.screen,(70,70,70),((525,200),(555,230),(568,230),(538,200)))
        pygame.draw.polygon(GlobalData.screen,(70,70,70),((525,270),(555,240),(568,240),(538,270)))
        pygame.display.update()

    def update(self,type,val):
        GlobalData.screen.fill(self.bgColor)
        pygame.draw.rect(GlobalData.screen,(70,70,70),(0,230,570,10))
        pygame.draw.polygon(GlobalData.screen,(70,70,70),((525,200),(555,230),(568,230),(538,200)))
        pygame.draw.polygon(GlobalData.screen,(70,70,70),((525,270),(555,240),(568,240),(538,270)))


class PersonView(View):
    WALK = 4
    JUMP = 11
    SLOW_FACTOR = 2

    def draw(self,arg):
        self.pos = (arg[0],arg[1])
        GlobalData.screen.blit(self.run[0],self.pos)

    def update(self,type,val):
        if type == 'border':
            self.pos = (val[0],val[1])
            if self.mode == 'walk':
                GlobalData.screen.blit(self.run[self.walkTime // self.SLOW_FACTOR % self.WALK],self.pos)
                GlobalData.screen.blit(pygame.font.Font(None,20).render('(%d,0)' % (GlobalData.time),True,(100,100,100)),(self.pos[0]+20,self.pos[1]+92))
                self.walkTime += 1
            elif self.mode == 'jump':
                GlobalData.f = 12
                GlobalData.screen.blit(self.jump[self.jumpTime % self.JUMP],self.pos)
                GlobalData.screen.blit(pygame.font.Font(None,20).render('(%d,%d)' % (GlobalData.time,150-self.pos[1]),True,(100,100,100)),(self.pos[0]+20,self.pos[1]+92))
                self.jumpTime += 1
            else:
                GlobalData.screen.blit(self.down,self.pos)
                GlobalData.screen.blit(pygame.font.Font(None,20).render('(%d,0)' % (GlobalData.time),True,(100,100,100)),(self.pos[0]+20,self.pos[1]+60))
        elif type == 'maintain':
            if self.mode == 'walk':
                GlobalData.screen.blit(self.run[self.walkTime // self.SLOW_FACTOR  % self.WALK],self.pos)
                GlobalData.screen.blit(pygame.font.Font(None,20).render('(%d,0)' % (GlobalData.time),True,(100,100,100)),(self.pos[0]+20,self.pos[1]+92))
                self.walkTime += 1
            else:
                GlobalData.screen.blit(self.down,self.pos)
                GlobalData.screen.blit(pygame.font.Font(None,20).render('(%d,0)' % (GlobalData.time),True,(100,100,100)),(self.pos[0]+20,self.pos[1]+60))
                GlobalData.f = 12
        elif type == 'mode':
            GlobalData.f = 30
            self.mode = val
            if self.mode == 'walk':
                self.walkTime = 0
            elif self.mode == 'jump':
                self.jumpTime = 0

    def __init__(self,pos = (0,0),mode = 'walk'):
        self.pos,self.mode = pos,mode
        self.jump = []
        self.run = []
        for i in range(11):
            self.jump.append(pygame.transform.scale(pygame.image.load('../res/jump/%d.jpg' % (i + 1)),(76,92)))
        for i in range(4):
            self.run.append(pygame.transform.scale(pygame.image.load('../res/run/%d.jpg' % (i + 1)),(76,92)))
        self.down = pygame.transform.scale(pygame.image.load('../res/down.jpg'),(76,60))
        self.walkTime = 1
        self.jumpTime = 0

class AxisView(View):
    def draw(self,arg):
        pass
    
    def update(self,type,val):
        for point in val:
            pygame.draw.rect(GlobalData.screen,(100,100,100),(point.x,point.y,5,5))