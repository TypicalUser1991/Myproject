import pygame
from pygame.locals import *
pygame.init()
width = 1000
height = 500
window = pygame.display.set_mode((width,height))
imagespath = "C:\\Users\\jcasi\\Downloads\\Game Demo Repository\\Assets"
bg_img = pygame.image.load(imagespath + "\\villagemarket.png")
bg_img2 = pygame.image.load(imagespath + "\\Shop.png")
bg_img = pygame.transform.scale(bg_img,(width,height))
bg_img2 = pygame.transform.scale(bg_img2,(width,height))

# Player
player_img = pygame.image.load(imagespath + "\\char.png ")
player_x = 0


i = 0





'''
What to Focus on?
- SlideShow (Camera Bug)
- Player Black image 
'''

# Window Constants
window.fill((0,0,0)) ## Sets the BG to Black
# window.blit(bg_img,(i,0)) ## Puts the Background Image to (0,0) 

def MoveBackground():
    for x in range(1000):
        window.blit(bg_img, (width+x,0))
        window.blit(bg_img2, (width-x,0))
        pygame.display.update()

running = True
coords = (0,1000)
while running:

    window.blit(bg_img, coords)
    
    player_rect = player_img.get_rect(topleft = (player_x, 215))
    
    window.blit(player_img, player_rect)

    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] == True:
        difference = 0.7
        width = width - difference
        coords = (width,0) 
    elif keys[pygame.K_a] == True:
        difference = 0.7
        width = width + difference
        coords = (width,0)
    
    
    for event in pygame.event.get():

        if event.type == QUIT:
            running = False

        if event.type == KEYUP and event.key == K_ESCAPE:
            running = False

pygame.quit()