import pygame
from pygame.locals import*
import os
#import numpy
import random
pygame.init()

size = width, height = 800, 800
screen = pygame.display.set_mode((size))
running = 1

world = []
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
purple = 100, 0, 150
yellow = 255, 255, 0
arrayOffsetX = width / 12
arrayOffsetY = height / 10
amountBoxX = 10
amountBoxY = 10
amountBoxAll = amountBoxX * amountBoxY
boxSizeX = width / (amountBoxX + 2) #plus 2 for borders
boxSizeY = height / (amountBoxY + 2)
pathToSprite = "/home/lachlan/School Work/SDD/Year 12 Negotiate/sprites/"

#-------Images I have Photoshopped and are to be /implemented/ into the final product
#D:\SDD LATEST\Year 12 Negotiate
goldMine = pygame.image.load(pathToSprite + 'goldMine.png')
goldMine = pygame.transform.scale(goldMine, (boxSizeX, boxSizeY))

grass = pygame.image.load(pathToSprite + 'grass.png')
grass = pygame.transform.scale(grass, (boxSizeX, boxSizeY))

water = pygame.image.load(pathToSprite + 'threeWater1.png')
water = pygame.transform.scale(water, (boxSizeX, boxSizeY))

oneWater1 = pygame.image.load(pathToSprite + 'oneWater1.png')
oneWater1 = pygame.transform.scale(oneWater1, (boxSizeX, boxSizeY))

twoStraightWater1 = pygame.image.load(pathToSprite + 'twoStraightWater1.png')
twoStraightWater1 = pygame.transform.scale(twoStraightWater1, (boxSizeX, boxSizeY))

twoBendWater1 = pygame.image.load(pathToSprite + 'twoBendWater1.png')
twoBendWater1 = pygame.transform.scale(twoBendWater1, (boxSizeX, boxSizeY))

solidWater1 = pygame.image.load(pathToSprite + 'solidWater1.png')
solidWater1 = pygame.transform.scale(solidWater1, (boxSizeX, boxSizeY))

threeWater1 = pygame.image.load(pathToSprite + 'threeWater1.png')
threeWater1 = pygame.transform.scale(threeWater1, (boxSizeX, boxSizeY))

fourWater1 = pygame.image.load(pathToSprite + 'fourWater1.png')
fourWater1 = pygame.transform.scale(fourWater1, (boxSizeX, boxSizeY))


class Player:
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

class Button:
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
            self.active = True
            return True

    def update(self):
        if self.active and not self.button.collidepoint(pygame.mouse.get_pos()):
            print "huh?"
            self.active = False
        elif self.active:
            self.button = pygame.draw.rect(screen, self.colourClick, (self.posx, self.posy, self.sizex, self.sizey))
        if not self.active:
            if self.button.collidepoint(pygame.mouse.get_pos()):
                self.button = pygame.draw.rect(screen, self.colourActive, (self.posx, self.posy, self.sizex, self.sizey))
            else:
                self.button = pygame.draw.rect(screen, self.colour, (self.posx, self.posy, self.sizex, self.sizey))

class Territory:

    def __init__(self, screen, posx, posy, pos):
        self.posx = posx
        self.posy = posy
        self.owner = "nature"
        self.pos = pos
        self.troops = 0
        self.randomNumber = random.randint(0, 20)
        self.type = "none"
        self.bounds = (self.posx, self.posy, boxSizeX, boxSizeY)
        self.rect = pygame.draw.rect(screen, purple, self.bounds)
        self.sprite = oneWater1
        self.spriteRotate = 0
        if self.randomNumber < 10: self.type = "grass"
        elif self.randomNumber < 20: self.type = "water"
        else: self.type = "goldMine"

      #  if self.pos

    def update(self):
        if self.type == "grass":
            screen.blit(grass, self.bounds)
        elif self.type == "water":
            screen.blit(self.sprite, (self.posx, self.posy, boxSizeX, boxSizeY))
        elif self.type == "goldMine":
            screen.blit(goldMine, (self.posx, self.posy, boxSizeX, boxSizeY))
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            rect = pygame.draw.rect(screen, red, (self.posx, self.posy, boxSizeX, boxSizeY))
            self.troops += 1
            basicfont = pygame.font.SysFont(None, 48)
            text = basicfont.render(str(self.pos), True, (255, 0, 0), (255, 255, 255))
            textrect = text.get_rect()
            textrect.centerx = rect.centerx
            textrect.centery = rect.centery
            screen.blit(text, textrect)

    def updateSprite(self):
        if self.type == "water":
            waterUp = False
            waterRight = False
            waterDown = False
            waterLeft = False
            if self.pos - 1 > 0 and self.pos - 1 < amountBoxAll:
                if world[self.pos - 1].type == "water":
                    #print "yep, water up at" + str(self.pos)
                    waterUp = True
            if self.pos + amountBoxY > 0 and self.pos + amountBoxY < amountBoxAll:
                if world[self.pos + amountBoxY].type == "water":
                    waterRight = True
            if self.pos + 1 > 0 and self.pos + 1 < amountBoxAll:
                if world[self.pos + 1].type == "water":
                    waterDown = True
            if self.pos - amountBoxY > 0 and self.pos - amountBoxY < amountBoxAll:
                if world[self.pos - amountBoxY].type == "water":
                    waterLeft = True

            #print "waterUp: " + str(waterUp) + " at pos " + str(self.pos)
            #Solid Water---------------
            if not waterUp and not waterRight and not waterDown and not waterLeft:
                self.sprite = solidWater1

        #For water with one entrace ---------------------
            elif waterUp and not waterRight and not waterDown and not waterLeft:
                #Connect to water up
                self.sprite = oneWater1
                self.sprite = pygame.transform.rotate(self.sprite, 180)
            elif not waterUp and waterRight and not waterDown and not waterLeft:
                #connects to water right
                self.sprite = oneWater1
                self.sprite = pygame.transform.rotate(self.sprite, 90)
            elif not waterUp and not waterRight and waterDown and not waterLeft:
                #Connects to water down
                self.sprite = oneWater1
            elif not waterUp and not waterRight and not waterDown and waterLeft:
                #Connects to water left
                self.sprite = oneWater1
                self.sprite = pygame.transform.rotate(self.sprite, 270)

        #For water with two entrances ----------------------
            elif waterUp and not waterRight and waterDown and not waterLeft:
                #Connects to water above and below
                self.sprite = twoStraightWater1
            elif not waterUp and waterRight and not waterDown and waterLeft:
                #Connects to water to left and right
                self.sprite = twoStraightWater1
                self.sprite = pygame.transform.rotate(self.sprite, 90)
            elif waterUp and not waterRight and not waterDown and waterLeft:
                #Connects to water up and left
                self.sprite = twoBendWater1
                self.sprite = pygame.transform.rotate(self.sprite, 180)
            elif waterUp and waterRight and not waterDown and not waterLeft:
                #Connects to water up and right
                self.sprite = twoBendWater1
                self.sprite = pygame.transform.rotate(self.sprite, 90)
            elif not waterUp and not waterRight and waterDown and waterLeft:
                #Connects to water down and left
                self.sprite = twoBendWater1
                self.sprite = pygame.transform.rotate(self.sprite, 270)
            elif not waterUp and waterRight and waterDown and not waterLeft:
                #Connects to water down and right
                self.sprite = twoBendWater1
                self.sprite = pygame.transform.rotate(self.sprite, 90)
                self.sprite = pygame.transform.flip(self.sprite, False, True)
            elif not waterUp and not waterRight and waterDown and waterLeft:
                self.sprite = twoBendWater1
                self.sprite = pygame.transform.rotate(self.sprite, 270)
        #For Water with three entrances!!--------------
            elif waterUp and not waterRight and waterDown and waterLeft:
                self.sprite = threeWater1
                self.sprite = pygame.transform.rotate(self.sprite, 270)
            elif waterUp and waterRight and waterDown and not waterLeft:
                self.sprite = threeWater1
                self.sprite = pygame.transform.rotate(self.sprite, 90)
            elif not waterUp and waterRight and waterDown and waterLeft:
                self.sprite = threeWater1
            elif waterUp and waterRight and not waterDown and waterLeft:
                self.sprite = threeWater1
                self.sprite = pygame.transform.rotate(self.sprite, 180)

            elif waterUp and waterRight and waterDown and waterLeft:
                self.sprite = fourWater1

def worldGen():
    
    posCount = 0
    for i in range(amountBoxX):
        for j in range(amountBoxY):
            world.append(Territory(screen, (i+1)*boxSizeX, (j+1)*boxSizeY, posCount))
            posCount += 1
    for territory in world:
        territory.updateSprite()

def runGame():
#------Game Setup----------
    playerX = 25
    playerY = 25
    worldGen()
    player1 = Player(screen, 5, world, red, "Lachlan", 1)
    player2 = Player(screen, 5, world, purple, "Lachlan", 2)
    endTurn = Button(screen, width - 50, height - 50, 45, 45, red, blue, green, "endTurn")
    buttons = []
    buttons.append(endTurn)
    player1Turn = True
    colourBackRed = 0
    colourBackGreen = 0
    colourBackBlue = 0
#---------Main Game Loop--------
    running = 1
    while running:
        backColour = colourBackRed, colourBackGreen, colourBackBlue
        screen.fill(backColour)
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
            
        else:
            player2.move()
        player1.update()
        player2.update()
        endTurn.update()
        
        colourBackRed += 2
        colourBackGreen += 4
        colourBackBlue += 6
        if colourBackRed > 255: colourBackRed = 0
        if colourBackGreen > 255: colourBackGreen = 0
        if colourBackBlue > 255: colourBackBlue = 0
        pygame.display.flip()



runGame()
