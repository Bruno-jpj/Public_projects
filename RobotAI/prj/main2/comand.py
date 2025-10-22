# 0: cmd stop
# 1: cmd start auto exploretion
# 2: cmd start move to (x,y) pos

import pygame as pg
import CONST as c

pg.init()
font = pg.font.Font(None, 25)

setCmd = {
    0: 'stop',
    1: 'start auto-exploration',
    2: 'insert (x,y) & move'
}

class SimulationCMDPanel():
    def __init__(self, w = 640, h = 480):
        self.w = w
        self.h = h

        self.display = pg.display.set_mode((self.w, self.h))
        
        # Set the caption of the screen
        pg.display.set_caption('CMD Panel')

        self.clock = pg.time.Clock()

        self.ui(None)
    #
    def ui(self, command):
        self.display.fill(c.BLACK)

        text = font.render(f"last comand: {command}", True, c.WHITE)

        self.display.blit(text, [0,0])

        pg.display.flip()
        self.clock.tick(c.SPEED)
    #
    def updateText(self):
        pass
#
class Cmd:
    def __init__(self):
        self.cmd = None
    #
    def insertCmd(self):
        pass
    #
    def checkCmd(self):
        pass
    #
    def executeCmd(self):
        pass
#
def main():
    cmd = Cmd()
    cmdPanel = SimulationCMDPanel()

    running = True

    while running:  
    # for loop through the event queue  
        for event in pg.event.get():
        
            # Check for QUIT event      
            if event.type == pg.QUIT:
                running = False
                

#
if __name__ == "__main__":
    main()