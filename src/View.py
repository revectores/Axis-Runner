import GlobalData
import pygame
import random

class View:
    def draw(self, arg):  # 初始状态绘制
        pass
    
    def update(self,type,val):
        pass

class StartView(View):
    def __init__(self):
        def text_objects(text,font):
            textsurface = font.render(text,True,(0,0,0))
            return textsurface
        self.bg = pygame.image.load('../res/bg.jpg')
        self.titlefont = pygame.font.Font('../res/font/ar.ttf',115 *4//5)
        self.subfont = pygame.font.Font('../res/font/ar.ttf',40*4//5)
        self.textsurf = text_objects('Axis Runner',self.titlefont)
        self.stt = text_objects('Start',self.subfont)
        self.ex = text_objects('Exit',self.subfont)
        self.op = text_objects('Option',self.subfont)

    def draw0(self):
        grey = (139,139,139)

        GlobalData.screen.blit(self.bg,(0,0))

        GlobalData.screen.blit(self.textsurf, (50,90))

        pygame.draw.rect(GlobalData.screen,grey,(290*4//5,265*4//5,200*4//5,50*4//5))
        GlobalData.screen.blit(self.stt, (335*4//5,265*4//5))

        pygame.draw.rect(GlobalData.screen, grey,(290*4//5,365*4//5,200*4//5,50*4//5))
        GlobalData.screen.blit(self.ex, (353*4//5,365*4//5))

        pygame.draw.rect(GlobalData.screen, grey,(290*4//5,465*4//5,200*4//5,50*4//5))
        GlobalData.screen.blit(self.op, (330*4//5,465*4//5))
    
    def draw(self,arg):
        self.draw0()
        if GlobalData.fromOption:
            GlobalData.fromOption = 0
        else:
            if GlobalData.sound == 'Sound:On':
                pygame.mixer.music.load('../res/bgm/bg1.mp3')
                pygame.mixer.music.play(loops = 114514)
                pygame.mixer.music.set_volume(0.2)

    def update(self,type,val):
        bright_grey = (185,185,185)
        self.draw0()
        if type == 'start':
            pygame.draw.rect(GlobalData.screen, bright_grey,(290*4//5,265*4//5,200*4//5,50*4//5))
            GlobalData.screen.blit(self.stt, (335*4//5,265*4//5))
        elif type == 'exit':
            pygame.draw.rect(GlobalData.screen, bright_grey,(290*4//5,365*4//5,200*4//5,50*4//5))
            GlobalData.screen.blit(self.ex, (353*4//5,365*4//5))
        elif type == 'option':
            pygame.draw.rect(GlobalData.screen, bright_grey,(290*4//5,465*4//5,200*4//5,50*4//5))
            GlobalData.screen.blit(self.op, (330*4//5,465*4//5))


class GameView(View):
    def __init__(self,bgColor,font,fontColor,pos):
        self.bgColor,self.font,self.fontColor,self.pos = bgColor,font,fontColor,pos
        self.bg = pygame.image.load('../res/bg.jpg')
    
    def draw(self,arg):
        if GlobalData.sound == 'Sound:On':
            pygame.mixer.music.load('../res/bgm/bg2.mp3')
            pygame.mixer.music.play(loops = 114514)
            pygame.mixer.music.set_volume(0.2)
        GlobalData.screen.blit(self.bg,(0,0))
        pygame.draw.rect(GlobalData.screen,(70,70,70),(0,230,570,10))
        pygame.draw.polygon(GlobalData.screen,(70,70,70),((525,200),(555,230),(568,230),(538,200)))
        pygame.draw.polygon(GlobalData.screen,(70,70,70),((525,270),(555,240),(568,240),(538,270)))
        pygame.display.update()

    def update(self,type,val):
        GlobalData.screen.blit(self.bg,(0,0))
        pygame.draw.rect(GlobalData.screen,(70,70,70),(0,230,570,10))
        pygame.draw.polygon(GlobalData.screen,(70,70,70),((525,200),(555,230),(568,230),(538,200)))
        pygame.draw.polygon(GlobalData.screen,(70,70,70),((525,270),(555,240),(568,240),(538,270)))


class GameOverView(View):
    def __init__(self):
        def text_objects(text,font,color):
            textsurface = font.render(text,True,color)
            return textsurface
        self.titlefont = pygame.font.Font("../res/font/go.ttf",115 * 4 // 5)
        self.textsurf = text_objects("Game Over!",self.titlefont,(0,0,0))
        self.subfont = pygame.font.Font("../res/font/ar.ttf",40* 4 // 5)
        self.restart = text_objects("Restart",self.subfont,(0,0,0))
        self.ret = text_objects("Back to Menu",self.subfont,(0,0,0))
        self.bg = pygame.image.load('../res/bg.jpg')

    def draw0(self):
        GlobalData.screen.blit(self.bg,(0,0))
        GlobalData.screen.blit(self.textsurf, (40* 4 // 5,150* 4 // 5))
        
        pygame.draw.rect(GlobalData.screen,(189,181,80),(100* 4 // 5,350* 4 // 5,200* 4 // 5,50* 4 // 5))
        GlobalData.screen.blit(self.restart,(120* 4 // 5,350* 4 // 5))

        pygame.draw.rect(GlobalData.screen,(189,181,80),(405* 4 // 5,350* 4 // 5,300* 4 // 5,50* 4 // 5))
        GlobalData.screen.blit(self.ret,(420* 4 // 5,350* 4 // 5))

        GlobalData.screen.blit(pygame.font.Font(None,30).render('x = %d' % (GlobalData.score),True,(0,0,0)),(270,230))

    def draw(self,arg):
        if GlobalData.sound == 'Sound:On':
            pygame.mixer.music.load('../res/bgm/bg3.mp3')
            pygame.mixer.music.play(loops = 114514)
            pygame.mixer.music.set_volume(0.2)
        self.draw0()

    def update(self,type,val):
        self.draw0()
        if type == 'res':
            pygame.draw.rect(GlobalData.screen,(189,183,107),(100* 4 // 5,350* 4 // 5,200* 4 // 5,50* 4 // 5))
            GlobalData.screen.blit(self.restart,(120* 4 // 5,350* 4 // 5))
        elif type == 'ret':
            pygame.draw.rect(GlobalData.screen,(189,183,107),(405* 4 // 5,350* 4 // 5,300* 4 // 5,50* 4 // 5))
            GlobalData.screen.blit(self.ret,(420* 4 // 5,350* 4 // 5))


class OptionView(View):
    def __init__(self):
        def text_objects(text, font, color):
            textsurface = font.render(text, True, color)
            return textsurface
        self.titlefont = pygame.font.Font('../res/font/ar.ttf', 115* 4 // 5 )
        self.subfont = pygame.font.Font('../res/font/ar.ttf', 40* 4 // 5 )
        self.subfont2 = pygame.font.Font('../res/font/ar.ttf', 30* 4 // 5 )
        self.textsurf = text_objects('Option',self.titlefont,(0,0,0))
        self.bg = self.bg = pygame.image.load('../res/bg.jpg')

    def draw(self,arg):
        GlobalData.screen.blit(self.bg,(0,0))
        GlobalData.screen.blit(self.textsurf,(200* 4 // 5 ,90* 4 // 5 ))

        pygame.draw.rect(GlobalData.screen,(189,181,80),(290* 4 // 5 ,265* 4 // 5 ,220* 4 // 5 ,50* 4 // 5 ))
        GlobalData.screen.blit(self.subfont.render(GlobalData.sound,True,(0,0,0)),(310* 4 // 5 ,265* 4 // 5 ))

        pygame.draw.rect(GlobalData.screen,(189,181,80),(290* 4 // 5 ,365* 4 // 5 ,220* 4 // 5 ,50* 4 // 5 ))
        GlobalData.screen.blit(self.subfont2.render(GlobalData.level,True,(0,0,0)),(298* 4 // 5 ,365* 4 // 5 ))

        pygame.draw.rect(GlobalData.screen,(189,181,80),(290* 4 // 5 ,465* 4 // 5 ,220* 4 // 5 ,50* 4 // 5 ))
        GlobalData.screen.blit(self.subfont.render('Return',True,(0,0,0)),(330* 4 // 5 ,465* 4 // 5 ))

    def update(self,type,val):
        self.draw(None)
        if type == 'sound':
            pygame.draw.rect(GlobalData.screen,(189,183,107),(290* 4 // 5 ,265* 4 // 5 ,220* 4 // 5 ,50* 4 // 5 ))
            GlobalData.screen.blit(self.subfont.render(GlobalData.sound,True,(0,0,0)),(310* 4 // 5 ,265* 4 // 5 ))
        elif type == 'level':
            pygame.draw.rect(GlobalData.screen,(189,183,107),(290* 4 // 5 ,365* 4 // 5 ,220* 4 // 5 ,50* 4 // 5 ))
            GlobalData.screen.blit(self.subfont2.render(GlobalData.level,True,(0,0,0)),(298* 4 // 5 ,365* 4 // 5 ))
        elif type == 'ret':
            pygame.draw.rect(GlobalData.screen,(189,183,107),(290* 4 // 5 ,465* 4 // 5 ,220* 4 // 5 ,50* 4 // 5 ))
            GlobalData.screen.blit(self.subfont.render('Return',True,(0,0,0)),(330* 4 // 5 ,465* 4 // 5 ))


class PersonView(View):
    WALK = 4
    JUMP = 11
    SLOW_FACTOR = 2

    def draw(self,arg):
        GlobalData.screen.blit(self.run[0],self.pos)
        GlobalData.time = 0
    def update(self,type,val):
        if type == 'border':
            self.pos = (val[0],val[1])
            if self.mode == 'walk':
                GlobalData.screen.blit(self.run[self.walkTime // self.SLOW_FACTOR % self.WALK],self.pos)
                GlobalData.screen.blit(pygame.font.Font(None,20).render('(%d,0)' % (GlobalData.time),True,(100,100,100)),(self.pos[0]+20,self.pos[1]+92))
                self.walkTime += 1
                if not GlobalData.time % 100: 
                    if GlobalData.sound == 'Sound:On':
                        self.runSound.play()
            elif self.mode == 'jump':
                GlobalData.f = 15
                if self.jumpTime < self.JUMP:
                    GlobalData.screen.blit(self.jump[self.jumpTime],self.pos)
                else:
                    GlobalData.screen.blit(self.jump[self.JUMP - 1],self.pos)
                GlobalData.screen.blit(pygame.font.Font(None,20).render('(%d,%d)' % (GlobalData.time,150-self.pos[1]),True,(100,100,100)),(self.pos[0]+20,self.pos[1]+92))
                self.jumpTime += 1
            else:
                GlobalData.screen.blit(self.down,self.pos)
                GlobalData.screen.blit(pygame.font.Font(None,20).render('(%d,0)' % (GlobalData.time),True,(100,100,100)),(self.pos[0]+20,self.pos[1]+60))
        elif type == 'mode':
            GlobalData.f = 30
            self.mode = val
            if self.mode == 'down':
                self.runSound.stop()
                if GlobalData.sound == 'Sound:On':
                    self.downSound.play()
                self.downTime = 0
            elif self.mode == 'walk':
                self.walkTime = 0
            elif self.mode == 'jump':
                self.runSound.stop()
                self.downSound.stop()
                if GlobalData.sound == 'Sound:On':
                    self.upSound.play()
                self.jumpTime = 0

    def __init__(self,pos = (282,148),mode = 'walk'):
        self.pos,self.mode = pos,mode
        self.jump = []
        self.run = []
        for i in range(11):
            self.jump.append(pygame.transform.scale(pygame.image.load('../res/person/jump/%d.jpg' % (i + 1)),(76,92)))
        for i in range(4):
            self.run.append(pygame.transform.scale(pygame.image.load('../res/person/run/%d.jpg' % (i + 1)),(76,92)))
        self.down = pygame.transform.scale(pygame.image.load('../res/person/down.jpg'),(76,60))
        self.walkTime = 1
        self.jumpTime = 0
        self.downTime = 0
        self.downSound = pygame.mixer.Sound('../res/se/down.ogg')
        self.runSound = pygame.mixer.Sound('../res/se/run.ogg')
        self.upSound = pygame.mixer.Sound('../res/se/jump.ogg')


class AxisView(View):
    def draw(self,arg):
        pass
    
    def update(self,type,val):
        for point in val:
            pygame.draw.rect(GlobalData.screen,(100,100,100),(point.x,point.y,5,5))