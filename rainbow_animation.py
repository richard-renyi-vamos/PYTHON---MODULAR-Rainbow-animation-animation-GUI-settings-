# rainbow_animation.py
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Rainbow colors
colors = [
    (148, 0, 211),  # Violet
    (75, 0, 130),   # Indigo
    (0, 0, 255),    # Blue
    (0, 255, 0),    # Green
    (255, 255, 0),  # Yellow
    (255, 127, 0),  # Orange
    (255, 0, 0)     # Red
]

def draw_rainbow():
    radius = 200
    position = (400, 300)  # Center of the screen

    for color in colors[::-1]:  # Draw from the outer to the inner circle
        pygame.draw.circle(screen, color, position, radius)
        radius -= 20  # Decrease radius for the next color

def main():
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # Fill screen with white
        draw_rainbow()
        pygame.display.flip()

        clock.tick(60)  # Limit to 60 frames per second

if __name__ == "__main__":
    main()
