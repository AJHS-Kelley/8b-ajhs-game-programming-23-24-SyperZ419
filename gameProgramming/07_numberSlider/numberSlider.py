# Number Slider, Xavier Oliver, based on a project by Al Sweigart, v0.0 

import sys, random, pygame
# sys module provides access to system resources (i.e. Operating System Commands)

from pygame.locals import *
# Allows us to call functions from pygame using just the function name instead of module.function()

# Constants for Game Board
BOARDWIDTH = 4 # Columns
BOARDHEIGHT = 4 # Rows
TILESIZE = 80 # Measured in Pixels
WINDOWWIDTH = 640 # Pixels
WINDOWHEIGHT = 480 # Pixels
FPS = 30
BLANK = None
