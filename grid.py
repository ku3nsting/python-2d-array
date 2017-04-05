#!/usr/bin/env python

"""Squares on a plane are colored variously either black or white.We arbitrarily identify one square as the "ant". The ant can travel in any of the four cardinal directions at each step it takes. The "ant" moves according to the rules below:
At a white square, turn 90° right, flip the color of the square, move forward one unit
At a black square, turn 90° left, flip the color of the square, move forward one unit

Langton's ant can also be described as a cellular automaton, where the grid is colored black or white and the “ant” square has one of eight different colors assigned to encode the combination of black/white state and the current direction of motion of the ant.[2]"""

grid = []

for index in range(20):
	grid.append([])
	for innerIndex in range(20):
		grid[index].append(' 0')

def printGrid(gridname, size):
        line = " "
        for rows in range(size):
                for columns in range(size):
                        line += str(gridname[rows][columns])
                print line
                line = " "

#grid[10][10] = 8
printGrid(grid, 20)
