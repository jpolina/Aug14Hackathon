## Pygame Base 
##
# @author UnloadingGnat, test
# @date 14/08/2020

#

## Pygame setup
import pygame
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hackathon")

## MODEL - Data use in system
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Loop until the user clicks the close button.
done = False
c = 10
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
pos = 500

x= 500
y= 200

## Main Program Loop
while not done:
    ## CONTROL
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        print(event)
    # Game logic
    pos = pos - 5
    ## VIEW
    # Clear screen
    screen.fill(BLUE)

    # Draw

    pygame.draw.ellipse(screen,WHITE,[x,y,100,100])


    # Update Screen
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit
pygame.quit()
