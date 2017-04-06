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
                
        def moveAnt(self, size, workingGrid):

        #change the color of the ant's current square based on what its value was before
        #store the value of the ant's destination
                self.valueReplaced = grid.colorChange(self.row, self.col, self)

        #calculate where the ant should go next
                self.moved = False
                
                if(self.direction == 'N' and self.moved == False):
                        self.row = self.row - 1
                        if (self.valueReplaced == ' '):
                                self.direction = 'E'
                        else:
                                self.direction = 'W'
                        self.moved = True
                if(self.direction == 'E' and self.moved == False):
                        self.com = self.col + 1
                        if (self.valueReplaced == ' '):
                                self.direction = 'S'
                        else:
                                self.direction = 'N'
                        self.moved = True
                if(self.direction == 'S' and self.moved == False):
                        self.row = self.row + 1
                        if (self.valueReplaced == ' '):
                                self.direction = 'W'
                        else:
                                self.direction = 'E'
                        self.moved = True
                if(self.direction == 'W' and self.moved == False):
                        self.col = self.col - 1
                        if (self.valueReplaced == ' '):
                                self.direction = 'N'
                        else:
                                self.direction = 'S'
                        self.moved = True
                        
        #move the ant to the destination
                grid.relocateAnt(self.row, self.col)
                

class Grid:
    def __init__(self):

        self.grid = []

    def colorChange(self, row, col, ant):
            val = ant.valueReplaced
            if (val == ' '):
                    self.grid[row][col].character = '0'
            else:
                    self.grid[row][col].character == ' '

            return val

    def relocateAnt(self, row, col):
            self.grid[row][col].character = 'X'

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
