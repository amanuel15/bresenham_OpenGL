import pygame
import threading

class Bres:

    def __init__(self):
        pygame.init()
        self.winsize = 1000
        self.bsize = 20
        self.radius = 20
        self.surface = pygame.display.set_mode((self.winsize,self.winsize))
        self.center = (self.winsize/2,self.winsize/2)
        self.blocksize = ( self.bsize, self.bsize)
        self.blocks = []
        self.xa = 10
        self.calculate()
        self.tickCall()

    def increment1(self, x, y):
        return self.d + 2*y + 1

    def increment2(self, x, y):
        return self.d + 2*y - 2*x + 1

    def calculate(self):
        self.blocks = []
        self.blocksa = []
        self.d = 1 - self.radius
        self.points = (self.radius, 0)
        self.increment = 0
        self.generateCircle()

    def generateCircle(self):
        points  = self.points
        if points[1] <= points[0]:
            self.blocks.append(points)
            print(self.d)
            if self.increment == 0:
                self.d = self.increment1(points[0], points[1])
                if self.d < 0:
                    self.increment = 0
                    points = (points[0], points[1] + 1)
                else:
                    self.increment = 1
                    points = (points[0] - 1, points[1] + 1)
            elif self.increment == 1:
                self.d = self.increment2(points[0], points[1])
                if self.d < 0:
                    self.increment = 0
                    points = (points[0], points[1] + 1)
                else:
                    self.increment = 1
                    points = (points[0] - 1, points[1] + 1)
            self.points = points
        else:
            return 'mirror'

    def completeCircle(self, typ):
        if (typ % 2 == 0):
            sb = self.blocks.copy()
            for i in sb:
                self.blocks.append((i[1],i[0]))
            return 3
        if (typ % 3 == 0):
            sb = self.blocks.copy()
            for i in sb:
                self.blocks.append((-i[0],i[1]))
            return 5
        if (typ % 5 == 0): 
            sb = self.blocks.copy()
            for i in sb:
                self.blocks.append((i[0],-i[1]))
            return 'reset'
             




    def draw(self):
        sb1 = self.blocksize[0]
        sb2 = self.blocksize[1]
        for i in self.blocks:
            rect = pygame.Rect((self.center[0] + i[0]*sb1 - sb1/2, self.center[1] + i[1]*sb2 - sb2/2),(sb1, sb2))
            pygame.draw.rect(self.surface, pygame.color.Color('red'), rect, 3)

    def tickCall(self):
        val = 2
        while True:
            self.xa -= 1
            self.tick()
            if self.xa == 0:
                if val == 'reset':
                    break
                    #self.points = (self.radius,0)
                    #self.blocks = []
                    #val = 2
                if self.generateCircle() == 'mirror':
                    val = self.completeCircle(val)
                self.xa = 30
            pygame.time.wait(5)

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == 2:
                if event.dict['key'] == 273:
                    self.radius += 1
                    self.calculate()
                if event.dict['key'] == 274:
                    self.radius -= 1
                    self.calculate()

        self.surface.fill(pygame.color.Color('black'))
        self.draw()
        pygame.display.flip()

Bres()
