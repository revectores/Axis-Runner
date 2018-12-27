class Model:
    def changeData(self,type,val):
        pass

    def __init__(self,listener):
        self.listener = listener

class CounterModel(Model):
    def __init__(self,listener,count):
        super().__init__(listener)
        self.count = count 
    
    def changeData(self,type,val):
        if type == 'add':
            self.count += val
        self.listener.update('',self.count)

class TimerModel(Model):
    def __init__(self,listener):
        super().__init__(listener)
        self.time = 0
     
    def changeData(self,type,val):
        if type == 'inc':
            self.time += val
        elif type == 'zero':
            self.time = 0
        self.listener.update('',self.time)