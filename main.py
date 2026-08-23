import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1080, 1080))
clock = pygame.time.Clock()

# Fixed point that the circle rotates around
cx, cy = 400, 300

# Orbit radius
orbit_radius = 150

# Circle's own radius
circle_radius = 25

angle = 0
angular_speed = 2  # degrees per frame

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Increase angle
    angle += angular_speed

    # Convert degrees to radians
    radians = math.radians(angle)

    # Calculate circle position
    x = cx + orbit_radius * math.cos(radians)
    y = cy + orbit_radius * math.sin(radians)

    screen.fill("black")

    # Draw the pivot
    pygame.draw.circle(screen, "white", (cx, cy), 5)

    # Draw the orbit (optional)
    pygame.draw.circle(screen, "gray", (cx, cy), orbit_radius, 1)

    # Draw the rotating circle
    pygame.draw.circle(screen, "red", (int(x), int(y)), circle_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
