import pygame


class Bres:

    def __init__(self):
        pygame.init()
        self.winsize = 1000
        self.bsize = 20
        self.surface = pygame.display.set_mode((self.winsize,self.winsize))
        self.center = (self.winsize/2,self.winsize/2)
        self.blocksize = ( self.bsize, self.bsize)
        self.blocks = []
        self.radius = 20
        self.calculate()
        self.tick()

    def calculate(self):
        self.x = 0
        self.y = self.radius
        self.x1 = 0
        self.y1 = 0
        self.d = 3-2*self.radius
        self.blocks = []
        while self.x <= self.y:
            self.generateCircle()

    def generateCircle(self):

        self.blocks.append((self.x1 + self.x, self.y1 + self.y))
        self.waitAndDraw()
        self.blocks.append((self.x1 + self.y, self.y1 + self.x))
        self.waitAndDraw()
        self.blocks.append((self.x1 - self.y, self.y1 + self.x))
        self.waitAndDraw()
        self.blocks.append((self.x1 - self.x, self.y1 + self.y))
        self.waitAndDraw()
        self.blocks.append((self.x1 - self.x, self.y1 - self.y))
        self.waitAndDraw()
        self.blocks.append((self.x1 - self.y, self.y1 - self.x))
        self.waitAndDraw()
        self.blocks.append((self.x1 + self.y, self.y1 - self.x))
        self.waitAndDraw()
        self.blocks.append((self.x1 + self.x, self.y1 - self.y))
        self.waitAndDraw()

        
        self.x += 1
        if self.d < 0:
            self.d += 4*self.x + 6
        else:
            self.y -= 1
            self.d += 4*(self.x - self.y) + 10

    def waitAndDraw(self, time = 50):
        pygame.time.wait(time)
        self.draw()

    def draw(self):
        sb1 = self.blocksize[0]
        sb2 = self.blocksize[1]
        self.surface.fill(pygame.color.Color('black'))
        for i in self.blocks:
            rect = pygame.Rect((self.center[0] + i[0]*sb1 - sb1/2, self.center[1] + i[1]*sb2 - sb2/2),(sb1, sb2))
            pygame.draw.rect(self.surface, pygame.color.Color('red'), rect, 3)        
        pygame.display.flip()

    def tickCall(self):
        while True:
            self.tick()

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
        self.draw()
        pygame.time.wait(5)

Bres()
