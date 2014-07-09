#messing around with class Unit. In dead end.


import pygame
from pygame.locals import*
import os
#import numpy
import random
import sys
pygame.init()



size = width, height = 1000, 1000

screen = pygame.display.set_mode((size))
running = 1

world = []
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
purple = 100, 0, 150
yellow = 255, 255, 0
arrayOffsetX = width / 5
arrayOffsetY = height / 10
amountBoxX = 20
amountBoxY = 20
amountBoxAll = amountBoxX * amountBoxY
boxSizeX = (width - 2 * arrayOffsetX) / amountBoxX #plus 2 for borders
boxSizeY = (height - 2 * arrayOffsetY) / amountBoxY
pathToSprite = "/home/lachlan/School Work/SDD/Year 12 Negotiate/sprites/"
#pathToSprite = 'D:/SDD LATEST/Year 12 Negotiate/sprites/'

#-------Images I have Photoshopped and are to be /implemented/ into the final product
#D:\SDD LATEST\Year 12 Negotiate
tile_img = pygame.image.load(pathToSprite + 'brickTile.png')
goldMine = pygame.image.load(pathToSprite + 'goldMine.png')

grass = pygame.image.load(pathToSprite + 'grass.png')

water = pygame.image.load(pathToSprite + 'threeWater1.png')

oneWater1 = pygame.image.load(pathToSprite + 'oneWater1.png')

twoStraightWater1 = pygame.image.load(pathToSprite + 'twoStraightWater1.png')

twoBendWater1 = pygame.image.load(pathToSprite + 'twoBendWater1.png')

solidWater1 = pygame.image.load(pathToSprite + 'solidWater1.png')

threeWater1 = pygame.image.load(pathToSprite + 'threeWater1.png')

fourWater1 = pygame.image.load(pathToSprite + 'fourWater1.png')

man = pygame.image.load(pathToSprite + 'man.png')


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
        #player = pygame.draw.rect(screen, self.colour, (self.world[self.pos].posx, self.world[self.pos].posy, boxSizeX, boxSizeY))
        #playerIcon = pygame.draw.rect(screen, self.colour, ((width/2 - boxSizeX) + self.playerNumber^2*boxSizeX, height - boxSizeY, boxSizeX, boxSizeY))
        screen.blit(man, (self.world[self.pos].posx, self.world[self.pos].posy))

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
        if self.randomNumber < 14: self.type = "grass"
        elif self.randomNumber < 20: self.type = "water"
        else: self.type = "goldMine"

      #  if self.pos

    def update(self):
        if self.type == "grass":
            screen.blit(self.sprite, self.bounds)
        elif self.type == "water":
            screen.blit(self.sprite, (self.posx, self.posy, boxSizeX, boxSizeY))
        elif self.type == "goldMine":
            screen.blit(self.sprite, (self.posx, self.posy, boxSizeX, boxSizeY))
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
        if self.type == "grass":
            self.sprite = grass
            self.sprite = pygame.transform.rotate(self.sprite, random.randint(0,4)*90)
        if self.type == "goldMine":
            self.sprite = goldMine
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
                self.type = "grass"
                self.sprite = grass
                self.sprite = pygame.transform.rotate(self.sprite, random.randint(0,4)*90)

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
        self.sprite = pygame.transform.scale(self.sprite, (boxSizeX, boxSizeY))

def draw_rimmed_box(screen, box_rect, box_color, rim_width=0, rim_color=Color('black')):
    if rim_width:
        rim_rect = Rect(box_rect.left - rim_width,
                        box_rect.top - rim_width,
                        box_rect.width + rim_width * 2,
                        box_rect.height + rim_width * 2)
        pygame.draw.rect(screen, rim_color, rim_rect)
    
    pygame.draw.rect(screen, box_color, box_rect)

def drawBackground():
    img_rect = tile_img.get_rect()

    nrows = int(screen.get_height() / img_rect.height) + 1
    ncols = int(screen.get_width() / img_rect.width) + 1

    for y in range(nrows):
        for x in range(ncols):
            img_rect.topleft = (x * img_rect.width,
                                y * img_rect.height)
            screen.blit(tile_img, img_rect)

    field_color = (109, 41, 1)
    draw_rimmed_box(screen, Rect(arrayOffsetX * 0.9, arrayOffsetY * 0.9, amountBoxX * boxSizeX + arrayOffsetX * 0.3, amountBoxY * boxSizeY + arrayOffsetY * 0.5), field_color, 4, Color('black'))

def worldGen():
    del world[:]
    posCount = 0
    for i in range(amountBoxX):
        for j in range(amountBoxY):
            world.append(Territory(screen, arrayOffsetX + (i+1)*boxSizeX, arrayOffsetY + (j+1)*boxSizeY, posCount))
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
    regenerateWorld = Button(screen, 50, 50, 50, 50, green, blue, red, "regenerate")
    buttons = []
    #buttons.append(endTurn, regenerateWorld)
    player1Turn = True
    colourBackRed = 0
    colourBackGreen = 0
    colourBackBlue = 0
#---------Main Game Loop--------
    running = 1
    while running:
        drawBackground()
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if endTurn.mouseClick(pygame.mouse.get_pos()):
                    if player1Turn:
                        player1Turn = False
                    else:
                        player1Turn = True
                if regenerateWorld.mouseClick(pygame.mouse.get_pos()):
                    worldGen()
        """
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            print "clicked"
            if endTurn.mouseClick(pygame.mouse.get_pos()):
                if player1Turn:
                    player1Turn = False
                else:
                    player1Turn = True
            if regenerateWorld.mouseClick(pygame.mouse.get_pos()):
                worldGen()
            #for button in buttons:
             #   print button
             #   button.mouseClick(pygame.mouse.get_pos())

             """

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
        regenerateWorld.update()
        
        pygame.display.flip()



runGame()
