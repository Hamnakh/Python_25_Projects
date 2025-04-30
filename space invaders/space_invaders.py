import pygame
import random
import math
import os

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Helper function to load image safely
def load_image(file, fallback_color=(255, 0, 0), size=(64, 64)):
    if os.path.exists(file):
        return pygame.image.load(file)
    else:
        print(f"Error: '{file}' not found. Using fallback.")
        surface = pygame.Surface(size)
        surface.fill(fallback_color)
        return surface

# Load images (use fallback if not found)
icon = load_image('spaceship.png', (0, 255, 0), (32, 32))
pygame.display.set_icon(icon)

player_img = load_image('player.png', (0, 0, 255))
enemy_img = load_image('enemy.png', (255, 0, 0))
bullet_img = load_image('bullet.png', (255, 255, 0), (8, 20))

# Player variables
player_x = 370
player_y = 480
player_x_change = 0

# Enemy variables
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)
enemy_x_change = 4
enemy_y_change = 40

# Bullet variables
bullet_x = 0
bullet_y = 480
bullet_y_change = 10
bullet_state = "ready"  # ready = bullet off screen, fire = bullet moving

# Functions to draw game objects
def draw_player(x, y):
    screen.blit(player_img, (x, y))

def draw_enemy(x, y):
    screen.blit(enemy_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.hypot(enemy_x - bullet_x, enemy_y - bullet_y)
    return distance < 27

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill screen with black

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            elif event.key == pygame.K_RIGHT:
                player_x_change = 5
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)

        # Key release
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_x_change = 0

    # Update player position
    player_x += player_x_change
    player_x = max(0, min(player_x, SCREEN_WIDTH - 64))

    # Update enemy position
    enemy_x += enemy_x_change
    if enemy_x <= 0 or enemy_x >= SCREEN_WIDTH - 64:
        enemy_x_change *= -1
        enemy_y += enemy_y_change

    # Update bullet position
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = "ready"

    # Collision check
    if is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
        bullet_y = 480
        bullet_state = "ready"
        enemy_x = random.randint(0, 736)
        enemy_y = random.randint(50, 150)

    # Draw game objects
    draw_player(player_x, player_y)
    draw_enemy(enemy_x, enemy_y)
    pygame.display.update()
