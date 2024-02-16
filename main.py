#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 22:30:06 2024

@author: jakubsz
"""

import numpy as np
import matplotlib.pyplot as plt


def howManyAliveNeighbours(check_grid, x,y):
    '''
    It doesnt work near edges, change it.

    Parameters
    ----------
    check_grid : game grid.
    x : x position of checked field.
    y : y position of checked grid.

    Returns
    -------
    count : number of alive cell around the point. Max 8.

    '''
    count = 0
    
    if ((x == 0) or (y == 0) or (x == len(check_grid)-1) or (y == len(check_grid)-1)):
        pass
    else:
        if check_grid[x-1, y+1] == 1: count +=1     
        if check_grid[x, y+1] == 1: count +=1
        if check_grid[x+1, y+1] == 1: count +=1
        if check_grid[x-1, y] == 1: count +=1
        if check_grid[x+1, y] == 1: count +=1
        if check_grid[x-1, y-1] == 1: count +=1
        if check_grid[x, y-1] == 1: count +=1
        if check_grid[x+1, y-1] == 1: count +=1
    
    return count

def display_grid(inputGrid):
    '''
    Displays grid using imshow().

    Parameters
    ----------
    inputGrid : 2D grid showing game map.

    '''
    ax.clear()
    ax.imshow(inputGrid, origin='lower', cmap='magma')
    ax.set_axis_off()
    plt.title("Conway's Game of Life")
    plt.suptitle(f'Generation: {generation}')

# grid initialization
Y_SIZE = 80
X_SIZE = 80

grid = np.zeros((Y_SIZE,X_SIZE))
counted_neighbours = np.zeros((Y_SIZE,X_SIZE))

# LWSS
start_point_x = 10
start_point_y = 10

grid[start_point_x, start_point_y] = 1
grid[start_point_x+3, start_point_y] = 1
grid[start_point_x, start_point_y+2] = 1
grid[start_point_x+1, start_point_y+3] = 1
grid[start_point_x+2, start_point_y+3] = 1
grid[start_point_x+3, start_point_y+3] = 1
grid[start_point_x+4, start_point_y+3] = 1
grid[start_point_x+4, start_point_y+2] = 1
grid[start_point_x+4, start_point_y+1] = 1


# simulation
simulation = True
generation = 0

fig, ax = plt.subplots()

while simulation is True:
    display_grid(grid)
    plt.pause(0.2)

    generation += 1

    for i in range(X_SIZE):
        for j in range(Y_SIZE):
            counted_neighbours[i,j] = howManyAliveNeighbours(grid, i, j)

    for i in range(X_SIZE):
        for j in range(Y_SIZE):
            if (grid[i,j] == 1) & (counted_neighbours[i,j] < 2):
                grid[i,j] = 0
            elif (grid[i,j] == 1) & (counted_neighbours[i,j] in (2,3) ):
                grid[i,j] = 1
            elif (grid[i,j] == 1) & (counted_neighbours[i,j] > 3 ):
                grid[i,j] = 0
            elif (grid[i,j] == 0) & (counted_neighbours[i,j] == 3 ):
                grid[i,j] = 1

   

    if generation > 100: simulation = False
