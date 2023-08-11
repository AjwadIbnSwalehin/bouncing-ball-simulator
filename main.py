import pygame
import sys


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ball = pygame.image.load("ball.png")
        self.rect = self.ball.get_rect()
        self.rect.x = 370  # Original x position of the ball
        self.rect.y = 100  # Original y position of the ball
        self.move_left = False  # Becomes True when the left arrow is held
        self.move_right = False  # Becomes True when the right arrow is held
        self.gravity = 0.01
        self.y_velocity = 0
        self.x_velocity = 1  # How many pixels the ball will move left/right
        self.energy_loss = 0.95  # Ball loses energy every time it bounces

    def draw(self, screen):
        screen.blit(self.ball, self.rect)

    def movement(self):
        if self.move_left:
            if self.rect.x <= 0:
                self.rect.x == 0  # (Left Boundary)
            else:
                self.rect.x -= self.x_velocity

        if self.move_right:
            if self.rect.x >= 736:
                self.rect.x == 736  # (Right Boundary)
            else:
                self.rect.x += self.x_velocity

    def vertical(self):
        self.rect.y += self.y_velocity
        self.y_velocity += self.gravity
        if self.rect.y >= 536 and self.y_velocity > 0:  # Ground position
            self.distance_moved = 0
            self.rect.y = 536  # Ball bouncing
            # Makes it so that the ball stops bouncing after a while
            if self.y_velocity < 0.6 and self.y_velocity > 0:
                self.y_velocity = 0
            else:
                # Velocity becomes negative to switch direction
                self.y_velocity = -self.y_velocity * self.energy_loss


# Initialize pygame
pygame.init()

width, height = 800, 600
backgroundColor = 255, 255, 255
screen = pygame.display.set_mode((width, height))

ball = Ball()

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball.move_left = True
            elif event.key == pygame.K_RIGHT:
                ball.move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ball.move_left = False
            elif event.key == pygame.K_RIGHT:
                ball.move_right = False

    # Update ball position
    ball.movement()
    ball.vertical()

    # Draw on the screen
    screen.fill(backgroundColor)
    ball.draw(screen)
    pygame.display.flip()
