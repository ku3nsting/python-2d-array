#!/usr/bin/env python

"""Squares on a plane are colored variously either black or white.We arbitrarily identify one square as the "ant". The ant can travel in any of the four cardinal directions at each step it takes. The "ant" moves according to the rules below:
At a white square, turn 90? right, flip the color of the square, move forward one unit
At a black square, turn 90? left, flip the color of the square, move forward one unit

Langton's ant can also be described as a cellular automaton, where the grid is colored black or white and the ?ant? square has one of eight different colors assigned to encode the combination of black/white state and the current direction of motion of the ant.[2]"""

from random import randint

import os

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
                        if (self.valueReplaced == '0' or self.valueReplaced == ' '):
                                self.direction = 'E'
                                self.col = self.col + 1
                        else:
                                self.direction = 'W'
                                self.col = self.col - 1
                        self.moved = True
                        
                if(self.direction == 'E' and self.moved == False):
                        if (self.valueReplaced == '0' or self.valueReplaced == ' '):
                                self.direction = 'S'
                                self.row = self.row + 1
                        else:
                                self.direction = 'N'
                                self.row = self.row - 1
                        self.moved = True
                        
                if(self.direction == 'S' and self.moved == False):
                        if (self.valueReplaced == '0' or self.valueReplaced == ' '):
                                self.direction = 'W'
                                self.col = self.col - 1
                        else:
                                self.direction = 'E'
                                self.col = self.col + 1
                        self.moved = True
                        
                if(self.direction == 'W' and self.moved == False):
                        if (self.valueReplaced == '0' or self.valueReplaced == ' '):
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
            if (val == '0' or val == ' '):
                    self.grid[r][c].character = '#'
            elif (val == '#'):
                    self.grid[r][c].character = ' '

    def getValReplaced(self, row, col):
            val = self.grid[row][col].character
            return val

    def relocateAnt(self, rowx, colx):
            self.grid[rowx][colx].character = '\x1b[0;33;40m' + 'X' + '\x1b[0m'

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

        self.grid[ant.row][ant.col].character = '\x1b[0;33;40m' + 'X' + '\x1b[0m'
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

#write a user input method that takes number of rounds and whether first ant
#is central or random as arguments

size = 64
grid  = Grid()
grid.initGrid(size)

ant = grid.generateAnt(size, 0)
num = 1

for rounds in range(11000):
        ant.moveAnt(size, grid)
        cls()
        num = grid.printGrid(size, num)
