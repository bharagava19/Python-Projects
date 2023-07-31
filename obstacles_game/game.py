import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Character dimensions
CHARACTER_WIDTH = 50
CHARACTER_HEIGHT = 50

# Obstacle dimensions
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodger Game")

# Character
character_img = pygame.Surface((CHARACTER_WIDTH, CHARACTER_HEIGHT))
character_img.fill(RED)
character_rect = character_img.get_rect()
character_rect.centerx = SCREEN_WIDTH // 2
character_rect.bottom = SCREEN_HEIGHT - 10

# Obstacles
obstacles = []
obstacle_speed = 5

def create_obstacle():
    obstacle_img = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
    obstacle_img.fill(RED)
    obstacle_rect = obstacle_img.get_rect()
    obstacle_rect.x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
    obstacle_rect.y = -OBSTACLE_HEIGHT
    return obstacle_rect

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the character with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character_rect.left > 0:
        character_rect.x -= 5
    if keys[pygame.K_RIGHT] and character_rect.right < SCREEN_WIDTH:
        character_rect.x += 5

    # Create new obstacles
    if random.random() < 0.05:
        obstacles.append(create_obstacle())

    # Move obstacles
    for obstacle in obstacles:
        obstacle.y += obstacle_speed
        if obstacle.y > SCREEN_HEIGHT:
            obstacles.remove(obstacle)

    # Check for collisions
    for obstacle in obstacles:
        if character_rect.colliderect(obstacle):
            running = False

    # Draw everything on the screen
    screen.fill(WHITE)
    screen.blit(character_img, character_rect)
    for obstacle in obstacles:
        screen.blit(character_img, obstacle)
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

pygame.quit()
