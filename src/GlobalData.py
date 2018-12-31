class GlobalData:
    statusList = []
    currentStatus = 0
    clock = None
    screen = None
    speed = 10
    time = 0

    @staticmethod
    def getStatus(): #获得当前状态
        return GlobalData.statusList[GlobalData.currentStatus]
    
    @staticmethod
    def changeStatus(nextStatus): #更改状态，然后让该游戏状态初始化
        GlobalData.currentStatus = nextStatus
        GlobalData.getStatus().init()

    @staticmethod
    def update():
        GlobalData.time += 1