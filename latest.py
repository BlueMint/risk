'''
to down

make so dead units appear dead, bugged atm (especially unit 3?)
when dice is rolled, dead units buttons become clickable

'''

#Importing pygame 
import pygame
from pygame.locals import*
import os
#import numpy
import random
import sys
import eztext
pygame.init()


#------start variable-----------
size = width, height = 1200, 800
centreX = width / 2

screen = pygame.display.set_mode((size))
running = 1

world = []
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
darkPurple = 150, 0, 200
purple = 100, 0, 150
yellow = 255, 255, 0
black = 0, 0, 0
white = 255, 255, 255
brown = (109, 41, 1)
grey = (100, 100, 100)
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
titleFont = pygame.font.SysFont(None, 50)
subTitleFont = pygame.font.SysFont(None, 25)
pathToSprite = "sprites/"
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

splash = pygame.image.load(pathToSprite + 'splash.png')


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
        print "making this"
        self.pos = pos
        self.colour = colour
        self.world = world
        self.bounds = (self.world[self.pos].posx, self.world[self.pos].posy, boxSizeX, boxSizeY)
        self.isSelected = selected
        self.playerNumber = playerNumber
        self.unitNumber = unitNumber
        self.basicfont = pygame.font.SysFont(None, 20)
        self.power = 1
        self.dead = False

    def update(self):
        if not self.dead:
            print "blitting people!"
            self.player = pygame.draw.rect(screen, self.colour, (self.world[self.pos].posx, self.world[self.pos].posy, boxSizeX, boxSizeY))
            self.unitNumberText = self.basicfont.render(str(self.unitNumber), True, (255, 0, 255), brown)
            if self.playerNumber == 1:
                screen.blit(man1, (self.world[self.pos].posx, self.world[self.pos].posy))
            elif self.playerNumber == 2:
                screen.blit(man2, (self.world[self.pos].posx, self.world[self.pos].posy))
            screen.blit(self.unitNumberText, (self.world[self.pos].posx + manSizeX, self.world[self.pos].posy))

        


class Player:

    def __init__(self, screen, turn, pos, world, colour, name, playerNumber, playerStatsX):
        print "creating player"
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
        self.textCentre = 30
        self.points = 0
        self.rolled = False
        self.dead = False
        self.bonusDice = 0
        self.buttons = []
        if playerNumber == 1:
            self.unit1 = Unit(screen, self.pos, self.name, self.colour, self.world, True, self.playerNumber, 1)
            self.unit2 = Unit(screen, self.pos - 1, self.name, self.colour, self.world, False, self.playerNumber, 2)
            self.unit3 = Unit(screen, self.pos - 2, self.name, self.colour, self.world, False, self.playerNumber, 3)
            
        else:
            self.unit1 = Unit(screen, self.pos + amountBoxY * (amountBoxX - 1), self.name, self.colour, self.world, True, self.playerNumber, 1)
            self.unit2 = Unit(screen, self.pos - 1 + amountBoxY * (amountBoxX - 1), self.name, self.colour, self.world, False, self.playerNumber, 2)
            self.unit3 = Unit(screen, self.pos - 2 + amountBoxY * (amountBoxX - 1), self.name, self.colour, self.world, False, self.playerNumber, 3)
 
        self.units = [self.unit1, self.unit2, self.unit3]

        self.attackButton = Button(screen, (self.textPosition, self.textLine(10)), 100, 20, white, red, blue, "attackUnit", 20, "Attack!", "Kill Them!", "Attacking")

        self.unit1PowerUpgrade = Button(screen, (self.textPosition, self.textLine(16)), 100, 20, white, red, blue, "upgradeUnit", 20, "Upgrade Unit 1", "Upgrade Unit 1", "Unit 1 Upgraded")
        self.unit1SelectUnit = Button(screen, (self.textPosition, self.textLine(17)), 100, 20, white, red, blue, "selectUnit", 20, "Select Unit 1", "Select Unit 1", "Unit 1 Selected")
        self.unit2PowerUpgrade = Button(screen, (self.textPosition, self.textLine(19)), 100, 20, white, red, blue, "upgradeUnit", 20, "Upgrade Unit 2", "Upgrade Unit 2", "Unit 2 Upgraded")
        self.unit2SelectUnit = Button(screen, (self.textPosition, self.textLine(20)), 100, 20, white, red, blue, "selectUnit", 20, "Select Unit 2", "Select Unit 2", "Unit 2 Selected")
        self.unit3PowerUpgrade = Button(screen, (self.textPosition, self.textLine(22)), 100, 20, white, red, blue, "upgradeUnit", 20, "Upgrade Unit 3", "Upgrade Unit 3", "Unit 3 Upgraded")
        self.unit3SelectUnit = Button(screen, (self.textPosition, self.textLine(23)), 100, 20, white, red, blue, "selectUnit", 20, "Select Unit 3", "Select Unit 3", "Unit 3 Selected")

        self.moveUp = Button(screen, (self.textPosition + self.textCentre, self.textLine(6)), 30, 30, white, grey, black, "moveUp", 40, " ^", " ^", " ^", " -")
        self.moveLeft = Button(screen, (self.textPosition, self.textLine(7)), 30, 30, white, grey, black, "moveLeft", 40, " <", " <", " <", " -")
        self.moveRight = Button(screen, (self.textPosition + 2 * self.textCentre, self.textLine(7)), 30, 30, white, grey, black, "moveRight", 40, " >", " >", " >", " -")
        self.moveDown = Button(screen, (self.textPosition + self.textCentre, self.textLine(8)), 30, 30, white, grey, black, "moveDown", 40, " v", " v", " v", " -")

        self.dice = Dice(screen, (self.textPosition + self.textCentre, self.textLine(0))) 

        self.endTurn = Button(screen, (self.textPosition, self.textLine(30)), 100, 20, white, red, blue, "endTurn", 20, "End Turn", "End Turn", "Turn Ended")

        self.pointButtons = [self.unit1PowerUpgrade, self.unit2PowerUpgrade, self.unit3PowerUpgrade, self.moveUp, self.moveLeft, self.moveRight, self.moveDown]
        self.functionButtons = [self.endTurn, self.unit1SelectUnit, self.unit2SelectUnit, self.unit3SelectUnit, self.attackButton]


    def stats(self, enemy):
        self.enemy = enemy
        if self.unit1.dead and self.unit2.dead and self.unit3.dead:
            self.dead = True
        if self.enemy.unit1.dead and self.enemy.unit2.dead and self.enemy.unit3.dead:
            self.enemy.dead = True
        elif self.unit1.dead:
            self.unitDead(self.unit1)
        elif self.unit2.dead:
            self.unitDead(self.unit2)
        elif self.unit3.dead:
            self.unitDead(self.unit3)

        self.bonusDice = 0
        for unit in self.units:
            if self.world[unit.pos].type == "goldMine":
                self.bonusDice += 1 

        self.bonusDiceText = self.basicfont.render(("Goldmines: " + str(self.bonusDice)), True, (255, 0, 255), brown)
        self.unit1PowerText = self.basicfont.render(("Unit1 Power: " + str(self.unit1.power)), True, (255, 0, 255), brown)
        self.unit2PowerText = self.basicfont.render(("Unit2 Power: " + str(self.unit2.power)), True, (255, 0, 255), brown)
        self.unit3PowerText = self.basicfont.render(("Unit3 Power: " + str(self.unit3.power)), True, (255, 0, 255), brown)
        self.selectedUnitText = self.basicfont.render(("Selected Unit: Unit" + str(int(self.selectedUnit) + 1)), True, (255, 0, 255), brown)
        self.currentPointsText = self.basicfont.render(("Points: " + str(self.points)), True, (255, 0, 255), brown)
        self.nameDisplayText = self.basicfont.render(self.name, True, (255, 0, 255), brown)

        screen.blit(self.nameDisplayText, (self.textPosition, self.textLine(-1)))
        screen.blit(self.selectedUnitText, (self.textPosition, self.textLine(3)))
        screen.blit(self.currentPointsText, (self.textPosition, self.textLine(5)))
        screen.blit(self.bonusDiceText, (self.textPosition, self.textLine(4)))
        screen.blit(self.unit1PowerText, (self.textPosition, self.textLine(15)))
        screen.blit(self.unit2PowerText, (self.textPosition, self.textLine(18)))
        screen.blit(self.unit3PowerText, (self.textPosition, self.textLine(21)))

        self.dice.update()

        if self.points == 0:
            for button in self.pointButtons:
                button.greyed = True
                button.update()
        else:
            for button in self.pointButtons:
                button.greyed = False
                self.moveButtonUpdate()
                button.update()


        for button in self.functionButtons:
            button.update()



    def textLine(self, line):
        return line * self.lineSpace + arrayOffsetY

    def clickDetected(self, pos):
        if self.turn:
            if self.unit1PowerUpgrade.mouseClick(pos):
                self.unit1.power += 1
                self.points -= 1
            if self.unit2PowerUpgrade.mouseClick(pos):
                self.unit2.power += 1
                self.points -= 1
            if self.unit3PowerUpgrade.mouseClick(pos):
                self.unit3.power += 1
                self.points -= 1
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
            if self.attackButton.mouseClick(pos):
                self.attack()
            if self.endTurn.mouseClick(pos):
                self.turn = False
                self.points = 0
                self.dice.rolling = True
                self.rolled = False
            if self.dice.bounds.collidepoint(pos):
                if not self.rolled:
                    self.dice.clicked()
                    self.points = self.dice.roll
                    self.points += self.bonusDice
                    self.rolled = True
            if self.moveUp.mouseClick(pos):
                self.move("up")
                self.points -= 1
            if self.moveLeft.mouseClick(pos):
                self.move("left")
                self.points -= 1
            if self.moveRight.mouseClick(pos):
                self.move("right")
                self.points -= 1
            if self.moveDown.mouseClick(pos):
                self.move("down")
                self.points -= 1

    def moveButtonUpdate(self):
        if self.unit1.isSelected:
            self.selectedUnit = 0
        elif self.unit2.isSelected:
            self.selectedUnit = 1
        elif self.unit3.isSelected:
            self.selectedUnit = 2
        elif not self.unit1.dead:
            self.selectedUnit = 0
        elif not self.unit2.dead:
            self.selectedUnit = 1
        elif not self.unit3.dead:
            self.selectedUnit = 2
        #Checking for boarders and waters:
        #UP
        if (((self.units[self.selectedUnit].pos - 1) % amountBoxY) == amountBoxY - 1):
            self.moveUp.greyed = True
        elif world[self.units[self.selectedUnit].pos - 1].type == "water":
            self.moveUp.greyed = True
        else:
            self.moveUp.greyed = False
        for unit in self.enemy.units + self.units:
            if self.units[self.selectedUnit].pos - 1 == unit.pos:
                self.moveUp.greyed = True

        #LEFT
        if not ((self.units[self.selectedUnit].pos - amountBoxY) >= 0 and (self.units[self.selectedUnit].pos - amountBoxY) < amountBoxY * amountBoxX):
            self.moveLeft.greyed = True
        elif world[self.units[self.selectedUnit].pos - amountBoxY].type == "water":
            self.moveLeft.greyed = True
        else:
            self.moveLeft.greyed = False
        for unit in self.enemy.units + self.units:
            if self.units[self.selectedUnit].pos - amountBoxY == unit.pos:
                self.moveLeft.greyed = True

        #RIGHT
        if not ((self.units[self.selectedUnit].pos + amountBoxY) >= 0 and (self.units[self.selectedUnit].pos + amountBoxY) < amountBoxY * amountBoxX):
            self.moveRight.greyed = True
        elif world[self.units[self.selectedUnit].pos + amountBoxY].type == "water":
            self.moveRight.greyed = True
        else:
            self.moveRight.greyed = False
        for unit in self.enemy.units + self.units:
            if self.units[self.selectedUnit].pos + amountBoxY == unit.pos:
                self.moveRight.greyed = True

        #DOWN
        if (((self.units[self.selectedUnit].pos + 1) % amountBoxY) == 0):
            self.moveDown.greyed = True
        elif world[self.units[self.selectedUnit].pos + 1].type == "water":
            self.moveDown.greyed = True
        else:
            self.moveDown.greyed = False
        for unit in self.enemy.units + self.units:
            if self.units[self.selectedUnit].pos + 1 == unit.pos:
                self.moveDown.greyed = True

    def move(self, direction):
        if direction == "up":
            if (self.units[self.selectedUnit].pos - 1) >= 0 and (self.units[self.selectedUnit].pos - 1) < amountBoxY * amountBoxX:
                if not ((self.units[self.selectedUnit].pos - 1) % amountBoxY) == amountBoxY - 1:
                    self.units[self.selectedUnit].pos -= 1

        if direction == "left":
            if (self.units[self.selectedUnit].pos - amountBoxY) >= 0 and (self.units[self.selectedUnit].pos - amountBoxY) < amountBoxY * amountBoxX:
                self.units[self.selectedUnit].pos -= amountBoxY


        if direction == "right":
            if (self.units[self.selectedUnit].pos + amountBoxY) >= 0 and (self.units[self.selectedUnit].pos + amountBoxY) < amountBoxY * amountBoxX:
                self.units[self.selectedUnit].pos += amountBoxY


        if direction == "down":
            if (self.units[self.selectedUnit].pos + 1) >= 0 and (self.units[self.selectedUnit].pos + 1) < amountBoxY * amountBoxX:
                if not ((self.units[self.selectedUnit].pos + 1) % amountBoxY) == 0:
                    self.units[self.selectedUnit].pos += 1

    def update(self):
        self.unit1.update() 
        self.unit2.update() 
        self.unit3.update() 

    def unitDead(self, unit):
        if unit.unitNumber == 1:
            self.unit1PowerUpgrade.greyed = True
            self.unit1PowerUpgrade.greyedText = "Dead"
            self.unit1SelectUnit.greyed = True
            self.unit1SelectUnit.greyedText = " "
            self.unit1PowerUpgrade.update()
            self.unit1SelectUnit.update()
        if unit.unitNumber == 2:
            self.unit2PowerUpgrade.greyed = True
            self.unit2PowerUpgrade.greyedText = "Dead"
            self.unit2SelectUnit.greyed = True
            self.unit2SelectUnit.greyedText = " "
            self.unit2PowerUpgrade.update()
            self.unit2SelectUnit.update()
        if unit.unitNumber == 3:
            self.unit3PowerUpgrade.greyed = True
            self.unit3PowerUpgrade.greyedText = "Dead"
            self.unit3SelectUnit.greyed = True
            self.unit3SelectUnit.greyedText = " "
            self.unit3PowerUpgrade.update()
            self.unit3SelectUnit.update()

    def changeSelectedUnit(self):
        if self.unit1.isSelected == True:
            self.unit1.isSelected = False
            self.unit2.isSelected = True
        elif self.unit2.isSelected == True:
            self.unit2.isSelected = False
            self.unit3.isSelected = True
        elif self.unit3.isSelected == True:
            self.unit3.isSelected = False
            self.unit1.isSelected = True

    def attack(self):
        self.enemyPresence = 0
        self.enemyUp = self.enemyLeft = self.enemyRight = self.enemyDown = False
        for unit in self.enemy.units:
            if (self.units[self.selectedUnit].pos - 1) == unit.pos:
                self.enemyUp = True
                self.enemyPresence += unit.power
            if (self.units[self.selectedUnit].pos - amountBoxY) == unit.pos:
                self.enemyLeft = True
                self.enemyPresence += unit.power
            if (self.units[self.selectedUnit].pos + amountBoxY) == unit.pos:
                self.enemyRight = True
                self.enemyPresence += unit.power
            if (self.units[self.selectedUnit].pos + 1) == unit.pos:
                self.enemyDown = True
                self.enemyPresence += unit.power
        if self.units[self.selectedUnit].power > self.enemyPresence:
            if self.enemyUp:
                for unit in self.enemy.units:
                    if (self.units[self.selectedUnit].pos - 1) == unit.pos:
                        unit.dead = True
                        unit.power = 0
                        unit.pos = -1
                        unit.isSelected = False

            if self.enemyLeft:
                for unit in self.enemy.units:
                    if (self.units[self.selectedUnit].pos - amountBoxY) == unit.pos:
                        unit.dead = True
                        unit.power = 0
                        unit.pos = -1
                        unit.isSelected = False

            if self.enemyRight:
                for unit in self.enemy.units:
                    if (self.units[self.selectedUnit].pos + amountBoxY) == unit.pos:
                        unit.dead = True
                        unit.power = 0
                        unit.pos = -1
                        unit.isSelected = False


            if self.enemyDown:
                for unit in self.enemy.units:
                    if (self.units[self.selectedUnit].pos + 1) == unit.pos:
                        unit.dead = True
                        unit.power = 0
                        unit.pos = -1
                        unit.isSelected = False
        else:
            self.units[self.selectedUnit].dead = True
            self.changeSelectedUnit()


class Button:
    def __init__(self, screen, pos, sizex, sizey, colour, colourActive, colourClick, function, fontSize, text, hoverText, clickText, greyedText="Needs Points"):
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
        self.greyedText = greyedText
        self.greyed = False

    def mouseClick(self, pos):
        if self.button.collidepoint(pos) and not self.greyed:
            self.active = True
            return True

    def update(self):
        if self.greyed:
            self.button = pygame.draw.rect(screen, grey, (self.posx, self.posy, self.sizex, self.sizey))
            text = self.basicfont.render((self.greyedText), True, (0, 0, 0), grey)
        else:
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
        textRect = text.get_width
        screen.blit(text, (self.posx + (self.sizex - text.get_width()) / 2, self.posy))

class Territory:

    def __init__(self, screen, posx, posy, pos):
        self.posx = posx
        self.posy = posy
        self.owner = "nature"
        self.pos = pos
        self.troops = 0
        self.randomNumber = random.randint(0, 40)
        self.type = "none"
        self.bounds = (self.posx, self.posy, boxSizeX, boxSizeY)
        self.rect = pygame.draw.rect(screen, purple, self.bounds)
        self.sprite = oneWater1
        self.spriteRotate = 0
        self.goldMines = 4
        if self.randomNumber < 30: self.type = "grass"
        elif self.randomNumber > 29 and self.pos > amountBoxY and self.pos < amountBoxY * (amountBoxX - 1): self.type = "water"
        else: self.type = "grass"
        if self.pos < (amountBoxY * amountBoxX) / 1.5 and self.pos > (amountBoxY * amountBoxX) / 3:
            if random.randint(0, 12) == 6:
                self.type = "goldMine"

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
            self.sprite = pygame.transform.rotate(self.sprite, random.randint(0, 4) * 90)
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
                self.sprite = pygame.transform.rotate(self.sprite, random.randint(0, 4) * 90)

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
        self.roll = random.randint(1, 6)
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


def gameOverScreen(winner):
    exitButton = Button(screen, (centreX - 50, height - 50), 100, 300, darkPurple, purple, white, "exit", 30, "Exit Game", "Exit Game", "Exit Game")
    subTitle1 = subTitleFont.render(("It looks like the there is a winner!"), True, (0, 0, 0), brown)
    subTitle2 = subTitleFont.render((winner.name + " has been crowned as the conqueror!"), True, (0, 0, 0), brown)
    subTitle3 = subTitleFont.render(("Writing result to scores.txt"), True, (0, 0, 0), brown)
    title = titleFont.render(("Game Over!"), True, (0, 0, 0), brown)
    while True:
        drawBackground()
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if exitButton.mouseClick(pygame.mouse.get_pos()):
                   sys.exit()
        exitButton.update()
        screen.blit(title, (centreX - title.get_width() / 2, 20))
        screen.blit(subTitle1, (centreX - subTitle1.get_width() / 2, 150))
        screen.blit(subTitle2, (centreX - subTitle2.get_width() / 2, 180))
        screen.blit(subTitle3, (centreX - subTitle3.get_width() / 2, 210))
        pygame.display.flip()

def splashScreen():
    while not pygame.time.get_ticks() > 500:
        print pygame.time.get_ticks()
        screen.blit(splash, (0, 0))
        pygame.display.flip()

def menuScreen():
    menuScreen = True
    buttonSizeX = 400
    buttonSizeY = 75
    basicfont = pygame.font.SysFont(None, 50)
    startGame = Button(screen, (centreX - buttonSizeX / 2, 300), buttonSizeX, buttonSizeY, darkPurple, purple, white, "startGame", 40, "Start Game!", "Let's Go!", "Game Started!")
    howToPlay = Button(screen, (centreX - buttonSizeX / 2, 400), buttonSizeX, buttonSizeY, darkPurple, purple, white, "howToPlay", 40, "How To Play?", "How To Play!", "Check Documentation")
    credits = Button(screen, (centreX - buttonSizeX / 2, 500), buttonSizeX, buttonSizeY, darkPurple, purple, white, "credits", 40, "Credits", "Credits!", "By Lachlan Brown")
    title = basicfont.render(("Welcome to Negotiate!"), True, (0, 0, 0), brown)
    menuButtons = [startGame, howToPlay, credits]
    while menuScreen:
        drawBackground()
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if startGame.mouseClick(pygame.mouse.get_pos()):
                    menuScreen = False
                if howToPlay.mouseClick(pygame.mouse.get_pos()):
                    this = 0
                if credits.mouseClick(pygame.mouse.get_pos()):
                    this = 0
        for button in menuButtons:
            button.update()
        screen.blit(title, (centreX - title.get_width() / 2, 200))
        pygame.display.flip()

def gameIntroScreen(player1Name, player2Name):
    gameIntroScreen = True
    player1NameNotChosen = True
    title = titleFont.render(("Please Enter Player Names"), True, (0, 0, 0), brown)
    subTitle1 = subTitleFont.render(("(Type Player 1 Now, 10 chars max)"), True, (0, 0, 0), brown)
    subTitle2 = subTitleFont.render(("(Type Player 2 Now, 10 chars max)"), True, (0, 0, 0), brown)
    txtbx1 = eztext.Input(maxlength=10, color=(0, 0, 0), prompt='Player 1: ')
    txtbx1.set_pos(centreX - 150, 350)
    enterPlayerName = Button(screen, (centreX - 50, 400), 100, 30, darkPurple, purple, white, "enterName", 30, "Name Entered", "Name Entered", "Name Entered")
    while gameIntroScreen:
        drawBackground()
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if enterPlayerName.mouseClick(pygame.mouse.get_pos()):
                    if player1NameNotChosen:
                        player1Name = txtbx1.value
                        txtbx1.prompt = "Player 2: "
                        txtbx1.value = ""
                        player1NameNotChosen = False
                    else:
                        player2Name = txtbx1.value
                        gameIntroScreen = False

        txtbx1.update(eventList)
        txtbx1.draw(screen)
        enterPlayerName.update()
        screen.blit(title, (centreX - title.get_width() / 2, 200))
        screen.blit(subTitle1, (centreX - subTitle1.get_width() / 2, 250))
        pygame.display.flip()
    return player1Name, player2Name


def worldGenerationScreen():
    worldGenerationScreen = True
    newWorldButton = Button(screen, (centreX - 150, height - 50), 100, 30, darkPurple, purple, white, "regenWorld", 30, "New World", "New World", "New World")
    okayButton = Button(screen, (centreX + 50, height - 50), 100, 30, darkPurple, purple, white, "Continue", 30, "Continue", "Continue", "Continue")
    title = titleFont.render(("Please Enter Player Names"), True, (0, 0, 0), brown)
    worldGen()
    while worldGenerationScreen:
        drawBackground()
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if newWorldButton.mouseClick(pygame.mouse.get_pos()):
                    worldGen()
                if okayButton.mouseClick(pygame.mouse.get_pos()):
                    worldGenerationScreen = False
        newWorldButton.update()
        okayButton.update()
        screen.blit(title, (centreX - title.get_width() / 2, 20))
        for territory in world:
            territory.update()
        pygame.display.flip()


def firstTurnScreen(player1, player2):
    firstTurnScreen = True
    dice1Clicked = False
    dice2Clicked = False
    dice1 = Dice(screen, (centreX - 100, 300))
    dice2 = Dice(screen, (centreX + 100, 300))
    okayButton = Button(screen, (centreX - 50, height - 50), 100, 30, darkPurple, purple, white, "Continue", 30, "Continue", "Continue", "Continue")
    player1Text = subTitleFont.render((player1.name + "'s Dice"), True, (0, 0, 0), brown)
    player2Text = subTitleFont.render((player2.name + "'s Dice"), True, (0, 0, 0), brown)
    title = titleFont.render(("Click On Your Dice To Roll!"), True, (0, 0, 0), brown)
    okayButton.greyed = True
    okayButton.greyedText = "Roll Both Dice"
    subTitle = subTitleFont.render((player2.name + " has 0.5 roll advantage!"), True, (0, 0, 0), brown)
    while firstTurnScreen:
        drawBackground()
        eventList = pygame.event.get()
        if dice1Clicked and dice2Clicked:
            okayButton.greyed = False
        for event in eventList:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if dice1.bounds.collidepoint(pygame.mouse.get_pos()) and not dice1Clicked:
                    dice1.clicked()
                    dice1Clicked = True
                if dice2.bounds.collidepoint(pygame.mouse.get_pos()) and not dice2Clicked:
                    dice2.clicked()
                    dice2Clicked = True
                if okayButton.mouseClick(pygame.mouse.get_pos()):
                    if dice2.roll >= dice1.roll:
                        player1.turn = False
                        player2.turn = True
                    firstTurnScreen = False
        okayButton.update()
        dice1.update()
        dice2.update()
        screen.blit(player1Text, (centreX - 100 - player1Text.get_width() / 2, 275))
        screen.blit(player2Text, (centreX + 100 - player2Text.get_width() / 2, 275))
        screen.blit(title, (centreX - title.get_width() / 2, 20))
        screen.blit(subTitle, (centreX - subTitle.get_width() / 2, 70))
        pygame.display.flip()
    return player1, player2




        

def runGame():
#------Game Setup----------
    player1Name = "Player 1"
    player2Name = "Player 2"
    splashScreen()
    menuScreen()
    player1Name, player2Name = gameIntroScreen(player1Name, player2Name)
    worldGenerationScreen()
    player1 = Player(screen, True, 5, world, red, player1Name, 1, player1StatsX)
    player2 = Player(screen, False, 5, world, purple, player2Name, 2, player2StatsX)
    player1, player2 = firstTurnScreen(player1, player2)

#---------Main Game Loop--------
    running = 1
    while running:
        drawBackground()
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
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
            player1.stats(player2)


        elif player2.turn:
            player2.stats(player1)

        if player1.dead:
            gameOverScreen(player2)

        if player2.dead:
            gameOverScreen(player1)

        player1.update()
        player2.update()

        pygame.display.flip()



runGame()
