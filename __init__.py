# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Project: Byte Invaders
Concept: Pong game with a twist

Author: abyssus dot <nospamkkty> j at gmail dot com

Status: incomplete
Todo: just about everything

USEFUL INFO

info http://www.pasteur.fr/formation/infobio/python/ch19s04.html

How to use Super()
http://blog.timvalenta.com/2009/02/understanding-pythons-super/

RGB Pallete
http://www.colorschemer.com/online.html
'''
# standard imports
import pygame
import os
import sys
import time
import random

# custom imports
from entities import *


class GetColours:

    def __init__(self):
        self.yellow = (240,240,0)
        self.orange = (240,120,0)
        self.red = (204,0,0)
        self.green = (0,204,0)
        self.lime_green = (133,255,10)
        self.purple = (133,10,255)
        self.blue = (0,0,204)
        self.darkBlue = (0,0,128)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.pink = (255,200,200)

if __name__ == "__main__":

    pygame.init()

    # lets create the game window
    screenwh = [432, 423] # sets game screens dimensions
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # makes screen open in middle
    pygame.display.set_caption('Byte me') # sets title of screen
    screen = pygame.display.set_mode((screenwh[0], screenwh[1]))
    screenwh_x_mid = screenwh[0] / 2
    screenwh_y_mid = screenwh[1] / 2
    colours = GetColours()

    all_objects = []

    clock = pygame.time.Clock()

    screen_hud = ScreenHUD(screen, 0,0,screenwh[0],1,colours.orange)

    player = Player(screen, screenwh_x_mid-20,screenwh[1]-20,40,10,colours.blue)

    ball = NPCBall(screen, screenwh_x_mid-10, 50, 10, 0,colours.green)
    ball.direction = True
    # is the game running?
    game_on = True

while game_on is True:

    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              pygame.quit(); sys.exit();

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move(-2)
        for o in all_objects:
            print o

    elif keys[pygame.K_RIGHT]:
        player.move(2)

    # game speed
    msElapsed = clock.tick(60)
    screen.fill(colours.black)

    screen_hud.draw()
    player.draw()
    ball.draw()
    ball.move(0, -1, ball.direction, player,screen_hud)

    pygame.display.update()