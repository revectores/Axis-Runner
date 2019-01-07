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
    pygame.display.set_caption('Test')
    #初始化时钟
    clock = pygame.time.Clock() 
    GlobalData.clock = clock 
    #初始化status，然后进入初状态
    GlobalData.init([GameStatus],{'main':0},0)
    #进入消息循环
    while 1:
        clock.tick(60) #这个数字要<=60
        #得到当前状态，通知这个状态时间的流逝，然后处理事件
        GlobalData.update()
        status = GlobalData.getStatus()
        status.timeElapse()
        for event in pygame.event.get():
            status.handle(event)

if __name__ == '__main__': main()