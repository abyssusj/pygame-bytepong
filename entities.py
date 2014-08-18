# -*- coding: utf-8 -*-
import pygame

class EntityObj(object):

    def __init__(self,x,y,h,w):
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        #collisions.append(self)

class PhysicalObj(EntityObj):

    def __init__(self, x,y,h,w):
        super(PhysicalObj, self).__init__(x,y,h,w) # imports init from parent class
        self.can_move = True
        self.can_collide = True
        self.rect = pygame.Rect(x,y,h,w)


class ScreenHUD(PhysicalObj):
    def __init__(self, screen,x,y,h,w,c):
        super(ScreenHUD, self).__init__(x,y,h,w) # imports init from parent class
        self.screen = screen
        self.colour = c
        self.wall_width = self.width
        # self.hud_rect = (self.x, self.y,self.height,self.width)
        self.wall_top = (self.x, self.y,self.height,self.wall_width)
        self.wall_bottom =  (0,self.height-11,self.height,self.wall_width)
        self.wall_left = (self.x, 0,self.height,self.wall_width)
       # self.wall_right =

        self.walls_all = []


    def update(self):
        self.wall_top = (self.x, self.y,self.height,self.wall_width)
        self.wall_bottom =  (0,self.height-11,self.height,self.wall_width)
        self.wall_left = (self.x, 0,self.wall_width,self.height)
        self.wall_right = (self.height-2, 0,self.wall_width,self.height)
        self.walls_all = (self.wall_top, self.wall_bottom, self.wall_left, self.wall_right)


    def draw(self):
        self.update()
        #pygame.draw.rect(self.screen, self.colour, self.hud_rect, 2)
        pygame.draw.rect(self.screen, self.colour, self.wall_top, 2)
        pygame.draw.rect(self.screen, self.colour, self.wall_bottom, 2)
        pygame.draw.rect(self.screen, self.colour, self.wall_left, 2)
        pygame.draw.rect(self.screen, self.colour, self.wall_right, 2)

class Player(PhysicalObj):
    '''Creates a moveable player object and draws to screen'''
    def __init__(self, screen,x,y,h,w,c):
        super(Player, self).__init__(x,y,h,w) # imports init from parent class
        self.screen = screen
        self.colour = c
        self.player_rect = (self.x, self.y,self.height,self.width)

    def move(self, mx):
        if self.can_move:
            self.x += mx

    def update(self):
        self.player_rect = (self.x, self.y,self.height,self.width)

    def draw(self):
        self.update()
        pygame.draw.rect(self.screen, self.colour, self.player_rect, 2)


class NPCBall(PhysicalObj):
    '''Creates a moveable player object and draws to screen'''
    def __init__(self, screen,x,y,h,w,c):
        super(NPCBall, self).__init__(x,y,h,w)
        self.screen = screen
        self.colour = c
        self.ball_rect = pygame.Rect(self.x, self.y,self.height,self.width)

    def move(self, mx, my, d, player,screen_hud):
        if self.can_move:
            self.direction = d

            if self.direction:
                    self.y += 2
                    self.rect[1] += 2

            elif not self.direction:
                    self.y -= 2
                    self.rect[1] -= 2

            if self.rect.colliderect(player.player_rect):
                print 'ball collided with player'
                self.direction = not self.direction
                return self.direction

            if self.rect.colliderect(screen_hud.wall_top):
                print 'ball collided with top wall'
                self.direction = not self.direction
                return self.direction

            if self.rect.colliderect(screen_hud.wall_left):
                print 'ball collided with left wall'
                self.direction = not self.direction
                return self.direction

            if self.rect.colliderect(screen_hud.wall_right):
                print 'ball collided with right wall'
                self.direction = not self.direction
                return self.direction


            if self.rect.colliderect(screen_hud.wall_bottom):
                print 'game over'
                self.direction = self.direction
                return self.direction




    def update(self):
        self.ball_rect = pygame.Rect(self.x, self.y,self.height,self.width)

    def draw(self):
        self.update()
        pygame.draw.circle(self.screen, self.colour, (self.x, self.y), self.height/2, 2)







