import pygame, sys
import math
from pygame.locals import*
import random as rn
pygame.init()

BLUE = (0,0,255)
WHITE = (255,255,255)

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption('S-Triangle')

#INPUT takes a location loc = (x,y) pair of points and width
#RETURN 3 points of the equilateral triangle determined by loc and width
def triangle(loc,width):
    Z = math.sqrt(width**2-(width/2)**2)
    top = ((width/2),0)
    L = (0,Z)
    R = (Z,width)
DISPLAYSURF.fill(WHITE)

#Draws Triangle
#(triangle(loc,w)) is a tuple of tuples...)
def draw_triangle(loc, w):
    pygame.draw.polygon(DISPLAYSURF, BLUE , (triangle(loc,w)),1)


def s(loc,width):
    Z = math.sqrt(width**2-(width/2)**2)
    top = ((width/2),0)
    L = (0,Z)
    R = (Z,width)
    if width > 1:
        s(top, width/2)
        s(L, width/2)
        s(R, width/2)
    else:
        return 
s((0,0),440)
    
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()