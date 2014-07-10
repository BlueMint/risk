'''
TODO:

- Outline sqaures that are owned
- Give units power numbers
- Make interface look nice


'''


import pygame
from pygame.locals import*
import os
#import numpy
import random
import sys
pygame.init()



size = width, height = 1200, 800

screen = pygame.display.set_mode((size))
running = 1

world = []
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
purple = 100, 0, 150
yellow = 255, 255, 0
black = 0, 0, 0
white = 255, 255, 255
brown = (109, 41, 1)
arrayOffsetX = width / 4
arrayOffsetY = height / 8
amountBoxX = 15
amountBoxY = 10
amountBoxAll = amountBoxX * amountBoxY
boxSizeX = (width - 2 * arrayOffsetX) / amountBoxX #plus 2 for borders
boxSizeY = (height - 2 * arrayOffsetY) / amountBoxY
backgroundRimmedX = amountBoxX * boxSizeX * 1.2
backgroundRimmedY = amountBoxY * boxSizeY * 1.1
gameBoarderX = width / 2 - backgroundRimmedX / 2
gameBoarderY = height / 2 - backgroundRimmedY / 2
player1StatsX = gameBoarderX * 0.2 #0.2 for 1 part of 5 for boarder
player2StatsX = gameBoarderX * 0.2 + gameBoarderX + backgroundRimmedX
player1StatsWidth = gameBoarderX * 0.6 #0.6 for the 3 parts of space for width, 2 parts boarder.
player2StatsWidth = gameBoarderX * 0.6
gameScreen = Rect(gameBoarderX, gameBoarderY, backgroundRimmedX, backgroundRimmedY)
player1Screen = Rect(player1StatsX, gameBoarderY, player1StatsWidth, backgroundRimmedY)
player2Screen = Rect(player2StatsX, gameBoarderY, player2StatsWidth, backgroundRimmedY)
manSizeX = (int(boxSizeX / 1.5))
manSizeY = (int(boxSizeY / 1.5))
diceSizeX = 50
diceSizeY = 50
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

man1 = pygame.transform.scale(pygame.image.load(pathToSprite + 'man.png'), (manSizeX, manSizeY))

man2 = pygame.transform.flip(man1, True, False)


#for the dice:::::
dicePosition = (width/2), 100


diceOne = pygame.transform.scale(pygame.image.load(pathToSprite + 'diceOne.png'),(diceSizeX, diceSizeY))
diceTwo = pygame.transform.scale(pygame.image.load(pathToSprite + 'diceTwo.png'),(diceSizeX, diceSizeY))
diceThree = pygame.transform.scale(pygame.image.load(pathToSprite + 'diceThree.png'),(diceSizeX, diceSizeY))
diceFour = pygame.transform.scale(pygame.image.load(pathToSprite + 'diceFour.png'),(diceSizeX, diceSizeY))
diceFive = pygame.transform.scale(pygame.image.load(pathToSprite + 'diceFive.png'),(diceSizeX, diceSizeY))
diceSix = pygame.transform.scale(pygame.image.load(pathToSprite + 'diceSix.png'),(diceSizeX, diceSizeY))


class Unit:
    def __init__(self, screen, pos, name, colour, world, selected, playerNumber, unitNumber):
        self.pos = pos
        self.colour = colour
        self.world = world
        self.bounds = (self.world[self.pos].posx, self.world[self.pos].posy, boxSizeX, boxSizeY)
        self.isSelected = selected
        self.playerNumber = playerNumber
        self.unitNumber = unitNumber
        self.basicfont = pygame.font.SysFont(None, 20)
        self.power = 1

    def selected(self):
        return self.isSelected

    def update(self):
        #player = pygame.draw.rect(screen, self.colour, self.bounds)
        self.player = pygame.draw.rect(screen, self.colour, (self.world[self.pos].posx, self.world[self.pos].posy, boxSizeX, boxSizeY))
        self.unitNumberText = self.basicfont.render(str(self.unitNumber), True, (255, 0, 255), brown)
        if self.playerNumber == 1:
            screen.blit(man1, (self.world[self.pos].posx, self.world[self.pos].posy))
        elif self.playerNumber == 2:
            screen.blit(man2, (self.world[self.pos].posx, self.world[self.pos].posy))
        screen.blit(self.unitNumberText, (self.world[self.pos].posx + manSizeX, self.world[self.pos].posy))

        


class Player:

    def __init__(self, screen, turn, pos, world, colour, name, playerNumber, playerStatsX):
        self.turn = turn
        self.pos = pos
        self.world = world
        self.name = name
        self.colour = colour
        self.playerNumber = playerNumber
        self.rightDown = False
        self.upDown = False
        self.downDown = False
        self.leftDown = False
        self.selectedUnit = 0
        self.textPosition = playerStatsX + 20
        self.basicfont = pygame.font.SysFont(None, 20)
        self.lineSpace = 20
        self.points = 0
        self.rolled = False
        self.buttons = []
        if playerNumber == 1:
            self.unit1 = Unit(screen, self.pos + 1, self.name, self.colour, self.world, True, self.playerNumber, 1)
            self.unit2 = Unit(screen, self.pos + 2, self.name, self.colour, self.world, False, self.playerNumber, 2)
            self.unit3 = Unit(screen, self.pos + 3, self.name, self.colour, self.world, False, self.playerNumber, 3)
            self.dice = Dice(screen, (self.textPosition, self.textLine(0)))
            
        else:
            self.unit1 = Unit(screen, self.pos + 1 + amountBoxY * (amountBoxX - 1), self.name, self.colour, self.world, True, self.playerNumber, 1)
            self.unit2 = Unit(screen, self.pos + 2 + amountBoxY * (amountBoxX - 1), self.name, self.colour, self.world, False, self.playerNumber, 2)
            self.unit3 = Unit(screen, self.pos + 3 + amountBoxY * (amountBoxX - 1), self.name, self.colour, self.world, False, self.playerNumber, 3)
            self.dice = Dice(screen, (self.textPosition, self.textLine(0)))  
        self.units = [self.unit1, self.unit2, self.unit3]
        self.unit1PowerUpgrade = Button(screen, (self.textPosition, self.textLine(11)), 100, 20, white, red, blue, "upgradeUnit", 20, "Upgrade Unit 1", "Upgrade Unit 1", "Unit 1 Upgraded")
        self.unit1SelectUnit = Button(screen, (self.textPosition, self.textLine(12)), 100, 20, white, red, blue, "selectUnit", 20, "Select Unit 1", "Select Unit 1", "Unit 1 Selected")
        self.unit2PowerUpgrade = Button(screen, (self.textPosition, self.textLine(14)), 100, 20, white, red, blue, "upgradeUnit", 20, "Upgrade Unit 2", "Upgrade Unit 2", "Unit 2 Upgraded")
        self.unit2SelectUnit = Button(screen, (self.textPosition, self.textLine(15)), 100, 20, white, red, blue, "selectUnit", 20, "Select Unit 2", "Select Unit 2", "Unit 2 Selected")
        self.unit3PowerUpgrade = Button(screen, (self.textPosition, self.textLine(17)), 100, 20, white, red, blue, "upgradeUnit", 20, "Upgrade Unit 3", "Upgrade Unit 3", "Unit 3 Upgraded")
        self.unit3SelectUnit = Button(screen, (self.textPosition, self.textLine(18)), 100, 20, white, red, blue, "selectUnit", 20, "Select Unit 3", "Select Unit 3", "Unit 3 Selected")

        self.endTurn = Button(screen, (self.textPosition, self.textLine(25)), 100, 20, white, red, blue, "endTurn", 20, "End Turn", "End Turn", "Turn Ended")
        self.buttons = [self.unit1PowerUpgrade, self.unit2PowerUpgrade, self.unit3PowerUpgrade, self.unit1SelectUnit, self.unit2SelectUnit, self.unit3SelectUnit, self.endTurn]


    def textLine(self, line):
        return line * self.lineSpace + arrayOffsetY

    def clickDetected(self, pos):
        if self.unit1PowerUpgrade.mouseClick(pos):
            self.unit1.power += 1
        if self.unit2PowerUpgrade.mouseClick(pos):
            self.unit2.power += 1
        if self.unit3PowerUpgrade.mouseClick(pos):
            self.unit3.power += 1
        if self.unit1SelectUnit.mouseClick(pos):
            self.unit1.isSelected = True
            self.unit2.isSelected = False
            self.unit3.isSelected = False
        if self.unit2SelectUnit.mouseClick(pos):
            self.unit1.isSelected = False
            self.unit2.isSelected = True
            self.unit3.isSelected = False
        if self.unit3SelectUnit.mouseClick(pos):
            self.unit1.isSelected = False
            self.unit2.isSelected = False
            self.unit3.isSelected = True
        if self.endTurn.mouseClick(pos):
            self.turn = False
        if self.dice.bounds.collidepoint(pos):
            if not self.rolled:
                self.dice.clicked()
                self.points = self.dice.roll
                self.rolled = True


    def stats(self):
        self.unit1PowerText = self.basicfont.render(("Unit1 Power: " + str(self.unit1.power)), True, (255, 0, 255), brown)
        self.unit2PowerText = self.basicfont.render(("Unit2 Power: " + str(self.unit2.power)), True, (255, 0, 255), brown)
        self.unit3PowerText = self.basicfont.render(("Unit3 Power: " + str(self.unit3.power)), True, (255, 0, 255), brown)
        self.selectedUnitText = self.basicfont.render(("Selected Unit: Unit" + str(int(self.selectedUnit) + 1)), True, (255, 0, 255), brown)
        self.currentPointsText = self.basicfont.render(("Points: " + str(self.points)), True, (255, 0, 255), brown)

        screen.blit(self.unit1PowerText, (self.textPosition, self.textLine(10)))
        screen.blit(self.unit2PowerText, (self.textPosition, self.textLine(13)))
        screen.blit(self.unit3PowerText, (self.textPosition, self.textLine(16)))
        screen.blit(self.selectedUnitText, (self.textPosition, self.textLine(3)))
        screen.blit(self.currentPointsText, (self.textPosition, self.textLine(4)))
        for button in self.buttons:
            button.update()


    def move(self):
        key = pygame.key.get_pressed()
        if self.unit1.selected() == True:
            self.selectedUnit = 0
        elif self.unit2.selected() == True:
            self.selectedUnit = 1
        elif self.unit3.selected() == True:
            self.selectedUnit = 2
        #Stuff for LEFT
        if key[pygame.K_LEFT] and self.leftDown == False:
            if (self.units[self.selectedUnit].pos - amountBoxY) >= 0 and (self.units[self.selectedUnit].pos - amountBoxY) < amountBoxY * amountBoxX:
                self.units[self.selectedUnit].pos -= amountBoxY
                self.leftDown = True
        if not key[pygame.K_LEFT]:
            self.leftDown = False

        #Stuff for RIGHT
        if key[pygame.K_RIGHT] and self.rightDown == False:
            if (self.units[self.selectedUnit].pos + amountBoxY) >= 0 and (self.units[self.selectedUnit].pos + amountBoxY) < amountBoxY * amountBoxX:
                self.units[self.selectedUnit].pos += amountBoxY
                self.rightDown = True
        if not key[pygame.K_RIGHT]:
            self.rightDown = False

        #Stuff for UP
        if key[pygame.K_UP] and self.upDown == False:
            if (self.units[self.selectedUnit].pos - 1) >= 0 and (self.units[self.selectedUnit].pos - 1) < amountBoxY * amountBoxX:
                if not ((self.units[self.selectedUnit].pos - 1) % amountBoxY) == amountBoxY - 1:
                    self.units[self.selectedUnit].pos -= 1
                    self.upDown = True
        if not key[pygame.K_UP]:
            self.upDown = False

        #stuff for DOWN
        if key[pygame.K_DOWN] and self.downDown == False:
            if (self.units[self.selectedUnit].pos + 1) >= 0 and (self.units[self.selectedUnit].pos + 1) < amountBoxY * amountBoxX:
                if not ((self.units[self.selectedUnit].pos + 1) % amountBoxY) == 0:
                    self.units[self.selectedUnit].pos += 1
                    self.downDown = True
        if not key[pygame.K_DOWN]:
            self.downDown = False

    def update(self):
        self.unit1.update() 
        self.unit2.update() 
        self.unit3.update() 
        self.dice.update()

    def changeSelectedUnit(self):
        if self.unit1.selected() == True:
            self.unit1.isSelected = False
            self.unit2.isSelected = True
        elif self.unit2.selected() == True:
            self.unit2.isSelected = False
            self.unit3.isSelected = True
        elif self.unit3.selected() == True:
            self.unit3.isSelected = False
            self.unit1.isSelected = True
class Button:
    def __init__(self, screen, pos, sizex, sizey, colour, colourActive, colourClick, function, fontSize, text, hoverText, clickText):
        print "creating button"
        self.posx, self.posy = pos
        self.sizex = sizex
        self.sizey = sizey
        self.colour = colour
        self.colourActive = colourActive
        self.colourClick = colourClick
        self.function = function
        self.active = False
        self.button = pygame.draw.rect(screen, self.colour, (self.posx, self.posy, self.sizex, self.sizey))
        self.basicfont = pygame.font.SysFont(None, fontSize)
        self.text = text
        self.hoverText = hoverText
        self.clickText = clickText

    def mouseClick(self, pos):
        if self.button.collidepoint(pos):
            self.active = True
            return True

    def update(self):
        if self.active and not self.button.collidepoint(pygame.mouse.get_pos()):
            self.active = False
        elif self.active:
            self.button = pygame.draw.rect(screen, self.colourClick, (self.posx, self.posy, self.sizex, self.sizey))
            text = self.basicfont.render((self.clickText), True, (0, 0, 0), self.colourClick)
        if not self.active:
            if self.button.collidepoint(pygame.mouse.get_pos()):
                self.button = pygame.draw.rect(screen, self.colourActive, (self.posx, self.posy, self.sizex, self.sizey))
                text = self.basicfont.render((self.hoverText), True, (0, 0, 0), self.colourActive)
            else:
                self.button = pygame.draw.rect(screen, self.colour, (self.posx, self.posy, self.sizex, self.sizey))
                text = self.basicfont.render((self.text), True, (0, 0, 0), self.colour)
        screen.blit(text, (self.posx, self.posy))

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

class Dice():

    def __init__(self, screen, pos):
        print "creating"
        self.roll = 0
        self.dicePositionX, self.dicePositionY = pos
        self.diceCount = 1
        self.visible = True
        self.bounds = Rect(self.dicePositionX, self.dicePositionY, diceSizeX, diceSizeY)
        self.rolling = True

    def update(self):
        if self.visible:
            if self.rolling:
                if self.diceCount == 1:
                    self.diceSide = diceOne
                if self.diceCount == 2:
                    self.diceSide = diceTwo
                if self.diceCount == 3:
                    self.diceSide = diceThree
                if self.diceCount == 4:
                    self.diceSide = diceFour
                if self.diceCount == 5:
                    self.diceSide = diceFive
                if self.diceCount == 6:
                    self.diceSide = diceSix
                self.diceCount += 1
                if self.diceCount == 7: self.diceCount = 1
                screen.blit(self.diceSide, (self.dicePositionX, self.dicePositionY))
            else:
                screen.blit(self.diceSide, (self.dicePositionX, self.dicePositionY))

    def clicked(self):
        self.roll = random.randint(1,7)
        if self.roll == 1:
            self.diceSide = diceOne
        if self.roll == 2:
            self.diceSide = diceTwo
        if self.roll == 3:
            self.diceSide = diceThree
        if self.roll == 4:
            self.diceSide = diceFour
        if self.roll == 5:
            self.diceSide = diceFive
        if self.roll == 6:
            self.diceSide = diceSix
        self.rolling = False
        print self.roll

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

    draw_rimmed_box(screen, gameScreen, brown, 4, Color('black'))
    draw_rimmed_box(screen, player1Screen, brown, 4, Color('black'))
    draw_rimmed_box(screen, player2Screen, brown, 4, Color('black'))

    
def worldGen():
    del world[:]
    posCount = 0
    for i in range(amountBoxX):
        for j in range(amountBoxY):
            world.append(Territory(screen, arrayOffsetX + (i)*boxSizeX, arrayOffsetY + (j)*boxSizeY, posCount))
            posCount += 1
    for territory in world:
        territory.updateSprite()


def runGame():
#------Game Setup----------
    worldGen()
    player1 = Player(screen, True, 5, world, red, "Lachlan", 1, player1StatsX)
    player2 = Player(screen, False, 5, world, purple, "Lachlan", 2, player2StatsX)

    #endTurn = Button(screen, (width - 50, height - 50), 45, 45, red, blue, green, "endTurn", 20, "End Turn", "End Turn", "Turn Ended")
    regenerateWorld = Button(screen, (50, 0), 50, 50, green, blue, red, "regenerate", 20, "New World", "New World", "World Generated")
    changeUnit = Button(screen, (150, 0), 50, 50, red, blue, green, "changeUnit", 20, "Change Unit", "Change Unit", "Unit Changed")
    diceStop = Button(screen, dicePosition, diceSizeX, diceSizeY, white, black, white, "diceStop", 20, " ", " ", " ")
    endTurn = Button(screen, (250, 0), 50, 50, purple, blue, green, "endTurn", 20, "End Turn", "End Turn", "Turn Ended")
    buttons = [player1, player2, endTurn, regenerateWorld, changeUnit, diceStop, endTurn]

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
                if regenerateWorld.mouseClick(pygame.mouse.get_pos()):
                    worldGen()
                if changeUnit.mouseClick(pygame.mouse.get_pos()):
                    if player1.turn:
                        player1.changeSelectedUnit()
                    else:
                        player2.changeSelectedUnit()
                if player1Screen.collidepoint(pygame.mouse.get_pos()):
                    player1.clickDetected(pygame.mouse.get_pos())
                    if not player1.turn:
                        player2.turn = True
                if player2Screen.collidepoint(pygame.mouse.get_pos()):
                    player2.clickDetected(pygame.mouse.get_pos())
                    if not player2.turn:
                        player1.turn = True

        for territory in world:
            territory.update()


        if player1.turn:
            player1.stats()
            player1.move()


        elif player2.turn:
            player2.stats()
            player2.move()          


        for button in buttons:
            button.update()

        pygame.display.flip()



runGame()
