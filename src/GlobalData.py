statusList = []
currentStatus = 0
clock = None
screen = None
speed = 10
time = 0
statusDict = {}
f = 30

def getStatus(): #获得当前状态
    return statusList[currentStatus]
    
def changeStatus(nextStatus): #更改状态，然后让该游戏状态初始化
    global currentStatus
    currentStatus = nextStatus
    getStatus().init()

def update():
    global time
    time += 1

def init(classList,aStatusDict,firstStatus):
    for c in classList:
        statusList.append(c.build())
    global statusDict
    statusDict = aStatusDict
    changeStatus(firstStatus)