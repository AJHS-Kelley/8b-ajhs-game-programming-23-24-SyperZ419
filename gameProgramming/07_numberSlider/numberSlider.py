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
FPS = 30 # This is a maximum value! Won't make a slow computer run faster.
BLANK = None

# Color Values in (R, G, B) format
# 0 = No Value, 255 = Max Value
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

# BOARD DESIGN SETUP
BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20 # pixels

