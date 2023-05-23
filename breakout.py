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

# Define classes (game objects)
class Paddle:
    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed

    def move_left(self):
        self.x += self.speed

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(self.x, self.y, self.w, self.h))

class Ball:
    def __init__(self, x, y, radius, speed, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.direction = direction # A tuple(dx, dy)
    
    def move(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), self.radius)

class Brick:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(self.x, self.y, self.w, self.h))

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