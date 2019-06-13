#Importing all the modules
try:
    import time, random, sys, os
except ImportError:
    print("Make sure to have the time module")
    sys.exit()
try:
    import pygame
except ImportError:
    print("Make sure you have python 3 and pygame.")
    sys.exit()
from pygame import freetype


#game_font = pygame.freetype.Font("Font.ttf", 75)
#text_surface, rect = game_font.render(("Programmer: 8BitToaster"), (0, 0, 0))
#gameDisplay.blit(text_surface, (150, 300))

# Initialize the game engine
pygame.init()


DisplayWidth,DisplayHeight = 1000, 800
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
pygame.display.set_caption("Name")

class Cell():
    def __init__(self, x, y, j, i):

        #Setting up cords and height/width
        self.x, self.y = x, y
        self.width, self.height = 30, 30
        self.StartY = self.y
        self.move = False
        self.Var = j + i
        #Setting up Color
        h = str(int(j/5)) + str(int(i/5)) + str(int(j/5)) + "F" + str(int(j/5)) + str(int(i/5))
        self.color = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    

    def draw(self):
        #Drawing each rect
        pygame.draw.rect(gameDisplay, self.color, (self.x, self.y, self.width, self.height), 0)

    def update(self):
        self.draw()

        #Moving the rectangles
        if self.move == False:
            self.y -= 1
            if self.y < self.StartY - self.Var:
                self.move = True
        else:
            self.y += 1
            if self.y > self.StartY + self.Var:
                self.move = False

def game_loop():
    game_run = True
    width, height = 55, 50
    Cells = [[0] * width for _ in range(height)]

    for j, row in enumerate(Cells):
        for i, tile in enumerate(row):
            Cells[j][i] = Cell(i*20, j*20 - 50, j, i)

    while game_run == True:

        gameDisplay.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #Updating all tiles
        for j, row in enumerate(Cells):
            for i, tile in enumerate(row):
                tile.update()


        pygame.display.flip()
        clock.tick(60)



game_loop()
