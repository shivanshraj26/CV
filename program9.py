import cv2
import numpy as np
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption("River with Moving Boat, Sun, and Clouds")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define constants
BOAT_BASE_COLOR = BROWN
BOAT_SAIL_COLOR = RED
SUN_COLOR = YELLOW
CLOUD_COLOR = WHITE

# Boat dimensions
BOAT_WIDTH = 120
BOAT_HEIGHT = 60

# Boat position and speed
boat_x = WIDTH // 2
boat_y = HEIGHT // 2 + 30
boat_speed = 5

# Function to draw the boat
def draw_boat(surface, x, y):
    # Draw boat base (trapezium)
    boat_base_points = [(x, y), (x + BOAT_WIDTH, y), (x + BOAT_WIDTH + BOAT_HEIGHT // 4, y + BOAT_HEIGHT),
                        (x - BOAT_HEIGHT // 4, y + BOAT_HEIGHT)]
    pygame.draw.polygon(surface, BOAT_BASE_COLOR, boat_base_points)
    # Draw boat sail (triangle)
    sail_center_x = x + BOAT_WIDTH // 2
    sail_top_y = y - BOAT_HEIGHT - 10
    sail_top_point = (sail_center_x, sail_top_y)
    sail_left_point = (x + BOAT_WIDTH // 3 - 15, y - BOAT_HEIGHT // 3)
    sail_right_point = (x + BOAT_WIDTH // 3 * 2 + 15, y - BOAT_HEIGHT // 3)
    pygame.draw.polygon(surface, BOAT_SAIL_COLOR, [sail_top_point, sail_left_point, sail_right_point])
    # Draw black rod between triangle and trapezium
    rod_width = 6
    rod_height = BOAT_HEIGHT // 3
    rod_x = x + BOAT_WIDTH // 2 - rod_width // 2
    rod_y = y - BOAT_HEIGHT // 3
    pygame.draw.rect(surface, BLACK, (rod_x, rod_y, rod_width, rod_height))

# Function to draw the sun
def draw_sun(surface, x, y):
    pygame.draw.circle(surface, SUN_COLOR, (x, y), 50)

# Function to draw static clouds
def draw_static_clouds(surface):
    cloud_positions = [(100, 150), (300, 100), (500, 200), (700, 150)]
    for position in cloud_positions:
        cloud_x, cloud_y = position
        pygame.draw.circle(surface, CLOUD_COLOR, (cloud_x, cloud_y), 30)
        pygame.draw.circle(surface, CLOUD_COLOR, (cloud_x + 40, cloud_y), 30)
        pygame.draw.circle(surface, CLOUD_COLOR, (cloud_x + 80, cloud_y), 30)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the boat horizontally
    boat_x += boat_speed
    if boat_x > WIDTH:
        boat_x = -BOAT_WIDTH

    # Draw sky
    screen.fill((135, 206, 235))

    # Draw sun
    draw_sun(screen, 100, 100)

    # Draw river
    pygame.draw.rect(screen, BLUE, (0, HEIGHT // 2 + 50, WIDTH, HEIGHT // 2 - 50))

    # Draw boat
    draw_boat(screen, boat_x, boat_y)

    # Draw static clouds
    draw_static_clouds(screen)

    # Convert Pygame surface to numpy array
    frame = pygame.surfarray.array3d(screen)

    # Transpose and flip horizontally
    frame = np.transpose(frame, axes=(1, 0, 2))
    frame = np.fliplr(frame)

    # Convert RGB to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Display frame using OpenCV
    cv2.imshow("River Scene", frame)
    cv2.waitKey(30)

    # Cap the frame rate
    pygame.time.Clock().tick(30)