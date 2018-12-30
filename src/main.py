import pygame
from pygame.locals import * 

from Model import *
from View import * 
from GlobalData import *
from Status import *

def main():
    #初始化屏幕和屏幕标题
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    GlobalData.screen = screen
    pygame.display.set_caption('Test')
    #初始化时钟
    clock = pygame.time.Clock()
    GlobalData.clock = clock
    #初始化status，然后进入初状态
    view1,view2 = TextView(),TextView((0,200,0))
    model1,model2 = CounterModel(view1,114514),TimerModel(view2)
    personView = PersonView()
    axisView = AxisView()
    personModel = PersonModel(personView,0,0,0,0)
    axisModel = AxisModel(axisView)
    GlobalData.statusList = [CounterStatus(model1,view1),TimerStatus(model2,view2)]
    GlobalData.changeStatus(0)
    #进入消息循环
    while 1:
        clock.tick(60) #这个数字要<=60
        #得到当前状态，通知这个状态时间的流逝，然后处理事件
        status = GlobalData.getStatus()
        status.timeElapse()
        for event in pygame.event.get():
            status.handle(event)

if __name__ == '__main__': main()