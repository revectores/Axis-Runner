from GlobalData import *
import pygame


class View:
    def draw(self, arg):  # 初始状态绘制
        pass

    def update(self, type, val):  # 实时更新
        pass


class TextView(View):
    def __init__(self, bgColor=(0, 0, 200), fontColor=(255, 255, 255)):
        self.bgColor, self.fontColor = bgColor, fontColor

    def draw(self, arg):

        GlobalData.screen.fill(self.bgColor)
        GlobalData.screen.blit(pygame.font.Font(None, 60).render(str(arg), True, self.fontColor), (100, 100))
        pygame.display.update()  # 写什么都别忘了update，要不然屏幕不会更新

    def update(self, type, val):
        time = GlobalData.
        speed = GlobalData.
        arg = time*speed
        draw(arg)
        GlobalData.screen.fill(self.bgColor)
        GlobalData.screen.blit(pygame.font.Font(None, 60).render(str(val), True, self.fontColor),
                               (100, 100))  # 其实没有必要重绘整个画面，如果速度太慢可以优化。
        pygame.display.update()


class PersonView(View):
    def __init__(self):
        self.image = ['walk.png', 'jump.png', 'down.png']
        self.size =
        self.position =
        self.screen =
        self.presta = 0
        self.preval = 0

    def draw(self, sta=0, position):
        runner = pygame.image.load(self.image[sta])
        GlobalData.screen.blit(runner,position)
        pygame.display.update()

    def update(self, Type, val):

        if Type == 'mode':
            if val == 'walk':
                sta = 0
            elif val == 'jump':
                Type = 'height'
                sta = 1
            elif val = 'down':
                sta = 2
        elif Type == 'height':
            sta = 1;
            self.position =
        elif Type == 'maintain':
            update(self,self.presta,self.preval)
        elif Type == 'jstop':
            sta = 0
            draw(sta, self.position)
        self.presta = Type;self.preval = val



class AxisView(View):
    def __init__(self):

    def draw(self, pos):
        pygame.screen.set_at(pos, color)
        pygame.display.update()

    def update(self):
        from collections import Iterator
        from collections import Iterable
        L = function()
        Iter = L.__iter__()
        while True:
            try:
                draw(next(L))
            except:
                break
        pygame.display.update()

person = personview(status,,value)
