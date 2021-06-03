class Player(object):
    def __init__(self, name):
        self.name = name
        self.current_pos = 0
    
    def getCurrentPos(self):
        return self.current_pos
    
    def updateCurrentPos(self, new_current_pos):
        self.current_pos = new_current_pos
