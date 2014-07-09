import pygame
#import numpy
import random
pygame.init()

size = width, height = 1200, 800
screen = pygame.display.set_mode((size))
running = 1

red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
arrayOffsetX = width / 12
arrayOffsetY = height / 10
amountBoxX = 10
amountBoxY = 10
boxSizeX = width / (amountBoxX + 2) #plus 2 for borders
boxSizeY = height / (amountBoxY + 2)


class Player():
    def __init__(self, screen, pos, world, colour, name, playerNumber):
        self.pos = pos
        self.world = world
        self.name = name
        self.colour = colour
        self.playerNumber = playerNumber
        self.rightDown = False
        self.upDown = False
        self.downDown = False
        self.leftDown = False


    def move(self):
        key = pygame.key.get_pressed()

        #Stuff for LEFT
        if key[pygame.K_LEFT] and self.leftDown == False:
            if (self.pos - amountBoxY) > 0 and (self.pos - amountBoxY) < amountBoxY * amountBoxX:
                print "yes"
                self.pos -= amountBoxY
                self.leftDown = True
        if not key[pygame.K_LEFT]:
            self.leftDown = False

        #Stuff for RIGHT
        if key[pygame.K_RIGHT] and self.rightDown == False:
            if (self.pos + amountBoxY) > 0 and (self.pos + amountBoxY) < amountBoxY * amountBoxX:
                print "yes"
                self.pos += amountBoxY
                self.rightDown = True
        if not key[pygame.K_RIGHT]:
            self.rightDown = False

        #Stuff for UP
        if key[pygame.K_UP] and self.upDown == False:
            if (self.pos - 1) > 0 and (self.pos - 1) < amountBoxY * amountBoxX:
                if not ((self.pos - 1) % amountBoxY) == amountBoxY - 1:
                    print "yes"
                    self.pos -= 1
                    self.upDown = True
        if not key[pygame.K_UP]:
            self.upDown = False

        #stuff for DOWN
        if key[pygame.K_DOWN] and self.downDown == False:
            if (self.pos + 1) > 0 and (self.pos + 1) < amountBoxY * amountBoxX:
                if not ((self.pos + 1) % amountBoxY) == 0:
                    self.pos += 1
                    self.downDown = True
        if not key[pygame.K_DOWN]:
            self.downDown = False

    def update(self):
        player = pygame.draw.rect(screen, self.colour, (self.world[self.pos].posx, self.world[self.pos].posy, boxSizeX, boxSizeY))
        playerIcon = pygame.draw.rect(screen, self.colour, ((width/2 - boxSizeX) + self.playerNumber^2*boxSizeX, height - boxSizeY, boxSizeX, boxSizeY))


class Button():
    def __init__(self, screen, posx, posy, sizex, sizey, colour, colourActive, colourClick, function):
        self.posx = posx
        self.posy = posy
        self.sizex = sizex
        self.sizey = sizey
        self.colour = colour
        self.colourActive = colourActive
        self.colourClick = colourClick
        self.function = function
        self.active = False
        self.button = pygame.draw.rect(screen, self.colour, (self.posx, self.posy, self.sizex, self.sizey))

    def mouseClick(self, pos):
        if self.button.collidepoint(pos):
            self.button = pygame.draw.rect(screen, self.colourClick, (self.posx, self.posy, self.sizex, self.sizey))
            self.active = True
            return True

    def update(self):
        if self.active and not self.button.collidepoint(pygame.mouse.get_pos()):
            print "huh?"
            self.active = False

        if not self.active:
            if self.button.collidepoint(pygame.mouse.get_pos()):
                self.button = pygame.draw.rect(screen, self.colourActive, (self.posx, self.posy, self.sizex, self.sizey))
            else:
                self.button = pygame.draw.rect(screen, self.colour, (self.posx, self.posy, self.sizex, self.sizey))

class Territory():

    def __init__(self, screen, posx, posy, pos):
        self.posx = posx
        self.posy = posy
        self.owner = "nature"
        self.pos = pos
        self.troops = 0
        self.randomNumber = random.randint(0, 20)
        self.type = "none"
        
    def update(self):
        if self.randomNumber < 15:
            rect = pygame.draw.rect(screen, green, (self.posx, self.posy, boxSizeX, boxSizeY))
        elif self.randomNumber < 21:
            rect = pygame.draw.rect(screen, blue, (self.posx, self.posy, boxSizeX, boxSizeY))
        if rect.collidepoint(pygame.mouse.get_pos()):
            rect = pygame.draw.rect(screen, red, (self.posx, self.posy, boxSizeX, boxSizeY))
            self.troops += 1
            basicfont = pygame.font.SysFont(None, 48)
            text = basicfont.render(str(self.pos), True, (255, 0, 0), (255, 255, 255))
            textrect = text.get_rect()
            textrect.centerx = rect.centerx
            textrect.centery = rect.centery
            screen.blit(text, textrect)

def worldGen():
    screen.fill((0, 0, 0))
    for i in range(0, amountBoxX + 1): #plus 1 cause no idea
        pygame.draw.line(screen, red, (arrayOffsetX + i*boxSizeX, arrayOffsetY), (arrayOffsetX + i*boxSizeX, height - arrayOffsetY))

    for i in range(0, amountBoxY + 1):
        pygame.draw.line(screen, red, (arrayOffsetX, arrayOffsetY + i*boxSizeY), (width - arrayOffsetX, arrayOffsetY + i*boxSizeY))

def runGame():
#------Game Setup----------
    playerX = 25
    playerY = 25
    world = []
    posCount = 0
    for i in range(amountBoxX):
        for j in range(amountBoxY):
            world.append(Territory(screen, (i+1)*boxSizeX, (j+1)*boxSizeY, posCount))
            posCount += 1
    player1 = Player(screen, 5, world, red, "Lachlan", 1)
    player2 = Player(screen, 5, world, blue, "Lachlan", 2)
    endTurn = Button(screen, width - 50, height - 50, 45, 45, red, blue, green, "endTurn")
    buttons = []
    buttons.append(endTurn)
    player1Turn = True
#---------Main Game Loop--------
    running = 1
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            if endTurn.mouseClick(pygame.mouse.get_pos()):
                if player1Turn:
                    player1Turn = False
                else:
                    player1Turn = True
            #for button in buttons:
             #   print button
             #   button.mouseClick(pygame.mouse.get_pos())

        for territory in world:
            territory.update()

        #World()
        if player1Turn:
            player1.move()
            player1.update()
        else:
            player2.move()
            player2.update()
        endTurn.update()
        pygame.display.flip()



runGame()
