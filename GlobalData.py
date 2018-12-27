class GlobalData:
    statusList = []
    currentStatus = 0
    clock = None
    screen = None
    lock = None
    @staticmethod
    def getStatus():
        return GlobalData.statusList[GlobalData.currentStatus]
    
    @staticmethod
    def changeStatus(nextStatus):
        GlobalData.currentStatus = nextStatus
        GlobalData.getStatus().init()