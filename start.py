# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Project: Byte Pong
Concept: Pong game

Author: abyssus dot <nospamkkty> j at gmail dot com

Status: in progress
Todo: lots of things

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



class GameState:

    def __init__(self):
        self.playing = True

if __name__ == "__main__":
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()

    sfx_plop = pygame.mixer.Sound(os.path.join('assets/sounds/plop.ogg'))  #load sound
    sfx_beep = pygame.mixer.Sound(os.path.join('assets/sounds/beep.ogg'))  #load sound
    pygame.mixer.music.load(os.path.join('assets/sounds/nuttypc2.ogg') )#load music
    pygame.mixer.music.play(-1)

    sfx = [sfx_plop, sfx_beep]

    # lets create the game window
    screenwh = [432, 423] # sets game screens dimensions
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # makes screen open in middle
    pygame.display.set_caption('Byte Pong') # sets title of screen
    screen = pygame.display.set_mode((screenwh[0], screenwh[1]))
    screenwh_x_mid = screenwh[0] / 2
    screenwh_y_mid = screenwh[1] / 2
    colours = GetColours()

    clock = pygame.time.Clock()

    screen_hud = ScreenHUD(screen, 0,0,screenwh[0],1,colours.orange)

    player = Player(screen, screenwh_x_mid-20,screenwh[1]-20,40,10,colours.blue)

    ball = NPCBall(screen, screenwh_x_mid-10, 50, 10, 0,colours.green,sfx)
    ball.direction = True

    font=pygame.font.Font('assets/fonts/ArcadeClassic.ttf',30)

    # is the game running?
    game_on = True


while game_on:

    # check for quit events
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
              pygame.quit(); sys.exit();

    if player.state is 'menu':

        screen.fill(colours.black)
        screen.fill(colours.black)
        txt1 = 'Byte Pong'
        txt2 = 'Press    SPACE    to  start'
        menutxt1 = font.render(txt1, 1, colours.green)
        menutxt2 = font.render(txt2, 1, colours.green)
        screen.blit(menutxt1, (screenwh[0]/3, screenwh[1]/3))
        screen.blit(menutxt2, (screenwh[0]/8, screenwh[1]/2))
        pygame.display.update()


        if keys[pygame.K_SPACE]:
            player.state = 'play'



    if player.state is 'game_over':
        screen.fill(colours.black)
        txt1 = 'Game   Over'
        txt2 = 'Press    SPACE    to  start'
        menutxt1 = font.render(txt1, 1, colours.green)
        menutxt2 = font.render(txt2, 1, colours.green)
        screen.blit(menutxt1, (screenwh[0]/3, screenwh[1]/3))
        screen.blit(menutxt2, (screenwh[0]/8, screenwh[1]/2))
        pygame.display.update()


        if keys[pygame.K_SPACE]:
            ball = NPCBall(screen, screenwh_x_mid-10, 50, 10, 0,colours.green,sfx)
            ball.direction = True
            player.state = 'play'


    if player.state is 'play':
        if keys[pygame.K_LEFT]:
            if player.x >= 4:
                player.move(-2)

        elif keys[pygame.K_RIGHT]:
            if player.x <= screenwh[1]-(player.width+27):
                player.move(2)


        # game speed
        msElapsed = clock.tick(240)
        screen.fill(colours.black)

        screen_hud.draw()
        player.draw()
        ball.move(ball.x, ball.y, ball.direction, player,screen_hud)
        ball.update()

    pygame.display.update()

