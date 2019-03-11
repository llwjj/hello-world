# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 16:14:21 2019

@author: lwj
"""
import pygame
from pygame.locals import *
from random import randint
from sys import exit



from item.map import Map
from item.cat import Cat
from item.bullet import Bullet
from item.explosion import Explosion

from model.fly_bullet import FB

from library.pygamemain import PygameMain
from library.music import Music
from library.point import Point,getLinePos


screen_size = (800,600)
title = "Running!"
sound_path = "./resource/sound/background.ogg"
       
class AoBigCat(PygameMain):
    def __init__(self):
        super().__init__(screen_size,title)
        
        self.bg = Map()
        self.cat = Cat((450,320))
        self.bullets_group = pygame.sprite.Group()
        self.explosions_group = pygame.sprite.Group()
        
        self.bullet = Bullet((50,50))
        self.bullets_group.add(self.bullet)
        
        
        self.list_add(self.bg,0,'update')
        self.list_add(self.bg,0,'draw')
        self.list_add(self.cat,0,'update')
        self.list_add(self.cat,3,'draw')
        self.list_add(self.bullets_group,2,'update')
        self.list_add(self.bullets_group,2,'draw')
        self.list_add(self.explosions_group,1,'update')
        self.list_add(self.explosions_group,1,'draw')
        
        sound = pygame.mixer.Sound(sound_path)
        self.bgmusic = Music(sound)
        self.bgmusic.play()
            
    def produce(self):
        if not self.produce_init:
            self.produce_init = True
            
            self.second = -1
            self.old_ticks = -1
            self.line_pos =[]
            
            
        sc = self.ticks // 1000

        if sc != self.second:
            self.second = sc
            self.bullet.rotate(-30)
 
            if self.second %80 ==79:
                self.bgmusic.repaly()
                
            if self.second %2 == 1:

                pn = 5#randint(2,6)
                points = []
                for _ in range(pn):
                    p = Point( randint(0,800),randint(0,600))
                    points.append(p)
                num = 100#randint(21,51)
                self.line_pos += getLinePos(points,num)
#                points = [Point(0,300),Point(400,100),Point(800,300)]
                #self.bullets_group.add(FB(points))
                
            
            
        if self.ticks - self.old_ticks > 10:
            self.old_ticks = self.ticks
                   

            if len(self.line_pos)>0:
                self.explosions_group.add(Explosion(self.line_pos[0].pos))
                del self.line_pos[0]

       
#            
#            
#        if self.produce_n<2:self.produce_n+=1
#        else: self.produce_n=0
#        
#        if len(self.bullets_group)<512:
#            for _ in range(4):
#                self.bullets_group.add( Bullet( (800,randint(100,500)))  )
#                
#        collide = pygame.sprite.collide_rect_ratio(0.8)     
#        for bullet in self.bullets_group:
##            if pygame.sprite.collide_mask(self.cat,bullet):
#            if collide(self.cat,bullet):
#                self.explosions_group.add(bullet.boomb())

        
    def event_response(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            self.cat.jump()
        if keys[pygame.K_d]:
            self.cat.move()
        if keys[pygame.K_a]:
            self.cat.move(1)

if __name__ == '__main__':
    AoBigCat().run()
      
