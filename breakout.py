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
        self.x -= self.speed
    
    def move_right(self):
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
# Create a Paddle instance
paddle = Paddle(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50, 100, 20, 5)

# Create a Ball instance
ball = Ball(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 10, 5, (0, 1))

# Create some Brick instances
bricks = [Brick(x, 50, 70, 20) for x in range(0, WINDOW_WIDTH, 75)]
# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: # A key has been pressed
            if event.key == pygame.K_LEFT: # The left arrow
                paddle.move_left()
            elif event.key == pygame.K_RIGHT: # The right arrow key
                paddle.move_right()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # The left arrow key is being held down
        if paddle.x > 0:
            paddle.move_left()
    if keys[pygame.K_RIGHT]:  # The right arrow key is being held down
        if paddle.x + paddle.w < WINDOW_WIDTH:
            paddle.move_right()



    
    #Update game state
    ball.move()

    # Check for collisions
    if ball.x - ball.radius < 0 or ball.x + ball.radius > WINDOW_WIDTH:
        # The ball has hit the left or right wall. Bounce it horizontally
        ball.direction = (-ball.direction[0], ball.direction[1])
    if  ball.y - ball.radius < 0:
        # The ball has hit the top wall. Bounce it vertically
        ball.direction = (ball.direction[0], -ball.direction[1])
    
    if ball.y - ball.radius <= paddle.y <= ball.y + ball.radius and paddle.x <= ball.x <= paddle.x + paddle.w:
        # The ball has hit the paddle. Calculate the hit position
        hit_pos = (ball.x - paddle.x) / paddle.w # This will be a number between 0 and 1

        # Calculate the new x direction. This will be between -1 and 1, with 0 in the middle of the paddle
        new_dx = 2 * hit_pos - 1

        # Bounce the ball. The y direction is always up, and the x direction is calculated above
        ball.direction = (new_dx, -abs(ball.direction[1]))
    
    for brick in bricks:
        if brick.y <= ball.y <= brick.y + brick.h and brick.x <= ball.x <= brick.x + brick.w:
            # The ball has hit a brick. Remove the brick and bounce the ball.
            bricks.remove(brick)
            ball.direction = (ball.direction[0], -ball.direction[1])
            break # only handle one brick collision per frame

    # Draw game state to window
    window.fill((0,0,0)) # Clear the window
    paddle.draw(window) # Draw the paddle
    ball.draw(window) # Draw the ball
    for brick in bricks:
        brick.draw(window)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)