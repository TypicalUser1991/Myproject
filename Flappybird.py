import pygame
import random
import sys
from pygame.locals import *

fps = 60
width = 1000
height = 1000

window = pygame.display.set_mode((width, height))
ground_y = height*0.8
player = 'C:\\Users\\jcasi\Downloads\\Game Demo Repository\\Assets\\jet.png'
background = 'C:\\Users\\jcasi\Downloads\\Game Demo Repository\\Assets\\nightsky.png'
cloud = 'C:\\Users\\jcasi\Downloads\\Game Demo Repository\\Assets\\cloud.png'
game_images = {}
game_sounds = {}

if __name__ == "__main__":
    pygame.init()
    fps_clock = pygame.time.Clock()
    pygame.display.set_caption('Jet Flying')
    game_images['bottom'] = pygame.image.load('C:\\Users\\jcasi\Downloads\\Game Demo Repository\\Assets\\bottom.png').convert_alpha()
    game_images['cloud'] = pygame.image.load('C:\\Users\\jcasi\Downloads\\Game Demo Repository\\Assets\\cloud.png').convert_alpha()
    game_images['background'] = pygame.image.load(background).convert_alpha()
    game_images['player'] = pygame.image.load(player).convert_alpha()


    while True:
        drawWindow()
        mainGame()


def drawWindow():
    player_x = int(screen_width/8)
    player_y = int((screen_height - game_images['player'].get_height())/2)
    bottom_x=0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                screen.blit(game_images['background'],(0,0))    
                screen.blit(game_images['player'],(player_x,player_y))
                screen.blit(game_images['bottom'],(bottom_x,ground_y))
                pygame.display.update()
                fps_clock.tick(fps)


