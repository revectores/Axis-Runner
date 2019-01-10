import pygame
from pygame.locals import * 

from Model import *
from View import * 
import GlobalData 
from Status import *

def main():
    #初始化屏幕和屏幕标题
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    GlobalData.screen = screen
    pygame.display.set_caption('Axis Runner')
    #初始化时钟
    clock = pygame.time.Clock() 
    GlobalData.clock = clock 
    #初始化status，然后进入初状态
    GlobalData.init([GameStatus,StartStatus,GameOverStatus,OptionStatus],{'main':0,'start':1,'gameover':2,'option':3},1)
    #进入消息循环
    while 1:
        clock.tick(GlobalData.f)
        #得到当前状态，通知这个状态时间的流逝，然后处理事件
        GlobalData.update()
        status = GlobalData.getStatus()
        status.timeElapse()
        for event in pygame.event.get():
            status.handle(event)

if __name__ == '__main__': main()