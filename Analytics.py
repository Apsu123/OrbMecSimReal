import pygame

pygame.init()

# Analytics window size
WIDTH = 500
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation Analytics")

clock = pygame.time.Clock()

# Fonts
title_font = pygame.font.Font(None, 40)
heading_font = pygame.font.Font(None, 28)
font = pygame.font.Font(None, 24)


def draw_text(text, x, y, font, color="white"):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # Title
    draw_text(
        "Simulation Analytics",
        20,
        20,
        title_font
    )

    # General information
    draw_text(
        "GENERAL",
        20,
        90,
        heading_font
    )

    draw_text(
        "Bodies: 5",
        30,
        130,
        font
    )

    draw_text(
        "Simulation time: 124.5 s",
        30,
        160,
        font
    )

    draw_text(
        "Time step: 0.1 s",
        30,
        190,
        font
    )

    # Sun information
    draw_text(
        "SUN",
        20,
        250,
        heading_font
    )

    draw_text(
        "Mass: 1.989e30 kg",
        30,
        290,
        font
    )

    draw_text(
        "Position: (500, 500)",
        30,
        320,
        font
    )

    draw_text(
        "Velocity: (0, 0)",
        30,
        350,
        font
    )

    # Planet information
    draw_text(
        "PLANET 1",
        20,
        410,
        heading_font
    )

    draw_text(
        "Mass: 5.972e24 kg",
        30,
        450,
        font
    )

    draw_text(
        "Position: (732, 284)",
        30,
        480,
        font
    )

    draw_text(
        "Velocity: (12.4, -4.7)",
        30,
        510,
        font
    )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()