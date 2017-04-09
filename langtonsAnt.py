#!/usr/bin/env python

"""Squares on a plane are colored variously either black or white.We arbitrarily identify one square as the "ant". The ant can travel in any of the four cardinal directions at each step it takes. The "ant" moves according to the rules below:
At a white square, turn 90? right, flip the color of the square, move forward one unit
At a black square, turn 90? left, flip the color of the square, move forward one unit

Langton's ant can also be described as a cellular automaton, where the grid is colored black or white and the ?ant? square has one of eight different colors assigned to encode the combination of black/white state and the current direction of motion of the ant.[2]"""

from random import randint

import os

####################################
#          INPUT VALIDATOR         #
#                                  #
####################################
def validate_ints(number, upper):
        while True:
                number = input()
                try:
                        number = int(number)
                except ValueError:
                        print "Invalid Input. Please try again:\n"
                        continue

                if (0 < number and number <= upper):
                        return number
                else:
                        print "Invalid Input. Please try again:\n"
                        continue

####################################
#          INTRO FUNCTION          #
#                                  #
####################################

print " ** LANGTON'S ANT IMPLEMENTATION **"
print " Choose a color scheme for the simulation:"
print " 1.\tMagenta and Green"
print " 2.\tRed and Gray"
print " 3.\tBlack and White"

choice = 0
choice = validate_ints(choice, 3)

color = choice

####################################
#          DEFINE COLORS           #
#                                  #
####################################

        #magenta and green
if(color == 1):
        X = '\x1b[0;30;43m' + 'X' + '\x1b[0m'
        W = '\x1b[1;30;42m' + '0' + '\x1b[0m'
        B = '\x1b[1;35;40m' + '#' + '\x1b[0m'

        #red and blue
if(color == 2):
        X = '\x1b[0;30;43m' + 'X' + '\x1b[0m'
        W = '\x1b[1;35;42m' + '0' + '\x1b[0m'
        B = '\x1b[1;31;40m' + '#' + '\x1b[0m'

        #black and white
if(color == 3):
        X = '\x1b[0;30;43m' + 'X' + '\x1b[0m'
        W = '\x1b[1;30;40m' + '0' + '\x1b[0m'
        B = '\x1b[1;37;47m' + '#' + '\x1b[0m'


####################################
#          DEFINE CLASSES          #
#                                  #
####################################
class Cell:
        def __init__(self, char, r, c):
                self.visits = 0
                self.character = char
                self.row = r
                self.col = c

class Ant:
        def __init__(self, r, c):
                self.direction = 'N'
                self.row = r
                self.col = c
                self.moved = False
                self.valueReplaced = ' '
                
        def moveAnt(self, size, workingGrid):

                #turn the ant
                self.moved = False
                oldCol = self.col
                oldRow = self.row
                
                if(self.direction == 'N' and self.moved == False):
                        if (self.valueReplaced == W or self.valueReplaced == ' '):
                                self.direction = 'E'
                                self.col = self.col + 1
                        else:
                                self.direction = 'W'
                                self.col = self.col - 1
                        self.moved = True
                        
                if(self.direction == 'E' and self.moved == False):
                        if (self.valueReplaced == W or self.valueReplaced == ' '):
                                self.direction = 'S'
                                self.row = self.row + 1
                        else:
                                self.direction = 'N'
                                self.row = self.row - 1
                        self.moved = True
                        
                if(self.direction == 'S' and self.moved == False):
                        if (self.valueReplaced == W or self.valueReplaced == ' '):
                                self.direction = 'W'
                                self.col = self.col - 1
                        else:
                                self.direction = 'E'
                                self.col = self.col + 1
                        self.moved = True
                        
                if(self.direction == 'W' and self.moved == False):
                        if (self.valueReplaced == W or self.valueReplaced == ' '):
                                self.direction = 'N'
                                self.row = self.row - 1
                        else:
                                self.direction = 'S'
                                self.row = self.row + 1
                        self.moved = True

                grid.colorChange(oldRow, oldCol, self.valueReplaced)

                self.valueReplaced = grid.getValReplaced(self.row, self.col)
                print self.valueReplaced
                
                grid.relocateAnt(self.row, self.col)
                

class Grid:
    def __init__(self):

        self.grid = []

    def colorChange(self, r, c, val):
            if (val == W or val == ' '):
                    self.grid[r][c].character = B
            elif (val == B):
                    self.grid[r][c].character = W

    def getValReplaced(self, row, col):
            val = self.grid[row][col].character
            return val

    def relocateAnt(self, rowx, colx):
            self.grid[rowx][colx].character = X

    def initGrid(self, size):
        for idx in range(size):
            self.grid.append([])
            for innerIndex in range(size):
                newCell = Cell(' ', idx, innerIndex)
                self.grid[idx].append(newCell)

    def generateAnt(self, size, rand):
        if (rand == 1):
            locationr = randint(0, size-1)
            locationc = randint(0, size-1)
            ant = Ant(locationr, locationc)
        if (rand == 0):
            location = (size/2)-1
            ant = Ant(location, location)

        self.grid[ant.row][ant.col].character = X
        return ant

    def printLine(self, width):
        topline = ""
        for idx in range((width * 2 + 1)):
                topline += "-"
        print "+" + topline + "+"

    def printGrid(self, size, number):
        #print number
        #grid.printLine(size)
        line = "|"
        for rows in range(size):
                for columns in range(size):
                        line += " "+str(self.grid[rows][columns].character)
                print line + " |"
                line = "|"  #clear "line"
        #grid.printLine(size)
        number = number + 1
        return number

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


####################################
#         MAIN PROGRAM LOOP        #
#                                  #
####################################

size = 64
grid  = Grid()
grid.initGrid(size)
running = True

ant = grid.generateAnt(size, 0)
num = 1

while(running == True):

        for rounds in range(11000):
                ant.moveAnt(size, grid)
                cls()
                num = grid.printGrid(size, num)

        #-----------------------------
        # ASK USER WHETHER TO CONTINUE
        #-----------------------------
        print "\nWould you like to run the Ant again?"
        print "1. \tYes"
        print "2. \tNo\n"
        print "Input your selection, then press ENTER:\n"
        running = validate_ints(keepGoing, 2)

print "Thanks, bye!"
