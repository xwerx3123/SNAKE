import pygame
import time
import random
from pyexpat.errors import messages


pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)



szerokosc = 1200
wysokosc = 600

screen = pygame.display.set_mode((szerokosc,wysokosc))
pygame.display.set_caption('Zaliczenie')

snake_blok = 10
snake_speed = 15

clock = pygame.time.Clock()

styl_czcionki = pygame.font.SysFont('comicsans', 30)

def our_snake(snake_blok, snake_list):
        for x in snake_list:
            pygame.draw.rect(screen, black, (x[0], x[1], snake_blok, snake_blok))

