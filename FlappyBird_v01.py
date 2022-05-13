import pygame

# Functions
def load_image(path, image_name, buffer):
    image = pygame.image.load(path).convert_alpha()
    buffer[image_name] = image
    print(f'IMAGE LOADER: Successfully loaded {image_name}')


## START READING CODE FROM HERE TO SEE THE START OF THE PROGRAM ##

# Pygame CONSTANTS
FPS = 60
WIDTH = 288
HEIGHT = 512
SIZE = (WIDTH, HEIGHT)
WINDOW = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()
pygame.init()

# Game CONSTANTS
GROUND_Y = HEIGHT*0.8

# Image CONSTANTS
ASSETS_FOLDER = 'C:\\Dev\\Myproject\\Assets' # Change only this Variable fo different path
BACKGROUND_PATH = ASSETS_FOLDER + '\\background.png'
PLAYER_PATH = ASSETS_FOLDER + '\\char.png'
BOTTOM_PATH = ASSETS_FOLDER + '\\bottom.png'

if __name__ == '__main__':


    # Load Images
    image_buffer = {}
    load_image(BACKGROUND_PATH, 'background', image_buffer)
    load_image(PLAYER_PATH, 'player', image_buffer)
    load_image(BOTTOM_PATH, 'bottom', image_buffer)

    # Player Values
    player_x = int(WIDTH/8)
    player_y = int((HEIGHT - image_buffer['player'].get_height())/2)

    # Main Window
    running = True


    while running:

        keys = pygame.key.get_pressed()

        # Have 60 FPS
        CLOCK.tick(FPS)

        # Render Stuff
        WINDOW.blit(image_buffer['background'], (0,0))
        WINDOW.blit(image_buffer['player'], (player_x, player_y))
        WINDOW.blit(image_buffer['bottom'], (0, GROUND_Y))

        # Constant Player Gravity
        player_y += 1

        # When Player touches Ground
        if player_y == int(GROUND_Y):
            print('END')

        # Player Movement
        if keys[pygame.K_UP]:
            player_y -= 4

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
