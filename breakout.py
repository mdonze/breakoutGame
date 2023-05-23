import pygame
import sys

# Initialize pygame
pygame.init()

# Setup some constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Setup the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Setup the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Update game state

    # Draw game state to window

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)