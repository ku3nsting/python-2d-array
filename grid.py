#!/usr/bin/env python

"""Squares on a plane are colored variously either black or white.We arbitrarily identify one square as the "ant". The ant can travel in any of the four cardinal directions at each step it takes. The "ant" moves according to the rules below:
At a white square, turn 90° right, flip the color of the square, move forward one unit
At a black square, turn 90° left, flip the color of the square, move forward one unit

Langton's ant can also be described as a cellular automaton, where the grid is colored black or white and the “ant” square has one of eight different colors assigned to encode the combination of black/white state and the current direction of motion of the ant.[2]"""

from random import randint

grid = []

for idx in range(20):
	grid.append([])
	for innerIndex in range(20):
		grid[idx].append('  ')

def printLine(width):
        topline = ""
        for idx in range((width * 2) + 2):
                topline += "-"
        print "+" + topline + "+"
        
def printGrid(gridname, size):
        printLine(size)
        line = "| "
        for rows in range(size):
                for columns in range(size):
                        line += str(gridname[rows][columns])
                print line + " |"
                line = "| "  #clear "line"
        printLine(size)

def generateAnt(gridname, size, rand):
        if (rand == 0):
                locationr = randint(0, size-1)
                locationc = randint(0, size-1)
                gridname[locationr][locationc] =" X"
        if (rand == 1):
                gridname[(size/2)-1][(size/2)-1] = " X"

#def moveAnt(gridname, size):
        
        
##MAIN PROGRAM LOOP##
for rounds in range(1):
        generateAnt(grid, 20, 1)
        printGrid(grid, 20)
