import pygame
from src.player import Player
from src.platform import Platform
from src.utils import load_image

pygame.init()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Platformer")

# Set up the clock
clock = pygame.time.Clock()

# Load the background image
background = load_image("assets/images/background.png")

# Create the player
player = Player(50, 50)

# Create the platforms
platform1 = Platform(0, screen_height - 50)
platform2 = Platform(screen_width - 150, screen_height - 150)
platform3 = Platform(screen_width // 2 - 50, screen_height - 250)
platforms = pygame.sprite.Group(platform1, platform2, platform3)

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
            elif event.key == pygame.K_SPACE:
                player.jump()

    # Update game state
    player.update(platforms)

    # Draw the screen
    screen.blit(background, (0, 0))
    platforms.draw(screen)
    screen.blit(player.image, player.rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
