# pygame is for games!
import pygame

# initialize all necessary methods/functions/variables by calling pygame.init()
pygame.init()

# width and height of screen
WIDTH = 1000
HEIGHT = 900

# set display-mode in screen variable
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# fonts
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 50)

# timer-clock for fps
timer = pygame.time.Clock()
fps = 60

# setup: game variables and images
# required is the main game loop which is essential for all games

run = True
while(run):
    timer.tick(fps)
    screen.fill('dark gray')
    
    # start event handling for keyboard input
    for event in pygame.event.get():
        # check if window closed
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
    
pygame.quit()
            

