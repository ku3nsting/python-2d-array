#!/usr/bin/env python

"""Squares on a plane are colored variously either black or white.We arbitrarily identify one square as the "ant". The ant can travel in any of the four cardinal directions at each step it takes. The "ant" moves according to the rules below:
At a white square, turn 90° right, flip the color of the square, move forward one unit
At a black square, turn 90° left, flip the color of the square, move forward one unit

Langton's ant can also be described as a cellular automaton, where the grid is colored black or white and the “ant” square has one of eight different colors assigned to encode the combination of black/white state and the current direction of motion of the ant.[2]"""

from random import randint

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
                
        def moveAnt(self, size, grid):
                grid.colorChange(self.row, self.col)
                
                if(self.direction == 'N'):
                        self.row = self.row - 1
                        self.direction = 'E'
                        return
                if(self.direction == 'E'):
                        self.com = self.col + 1
                        self.direction = 'S'
                        return
                if(self.direction == 'S'):
                        self.row = self.row + 1
                        self.direction = 'W'
                        return
                if(self.direction == 'W'):
                        self.col = self.col - 1
                        self.direction = 'N'
                        return

class Grid:
    def __init__(self):

        self.grid = []

    def colorChange(self, row, col):
           if (self.grid[row][col].character == ' '):
               self.grid[row][col].character = '0'
           else:
               self.grid[row][col].character == ' '

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

        self.grid[ant.row][ant.col].character = 'X'
        return ant

    def printLine(self, width):
        topline = ""
        for idx in range((width * 2 + 1)):
                topline += "-"
        print "+" + topline + "+"

    def printGrid(self, size):
        number = 1
        print number
        grid.printLine(size)
        line = "|"
        for rows in range(size):
                for columns in range(size):
                        line += " "+str(self.grid[rows][columns].character)
                print line + " |"
                line = "|"  #clear "line"
        grid.printLine(size)
        number = number + 1

####################################
#         MAIN PROGRAM LOOP        #
#                                  #
####################################

#write a user input method that takes number of rounds and whether first ant
#is central or random as arguments

grid  = Grid()
grid.initGrid(20)

ant = grid.generateAnt(20, 0)

for rounds in range(100):
        ant.moveAnt(20, grid)
        grid.printGrid(20)
