import pygame
import random

from pygame._sdl2 import Window, Renderer, Texture

pygame.init()

# --------------------------------------------------
# Simulation settings
# --------------------------------------------------

SIM_WIDTH = 800
SIM_HEIGHT = 600

screen = pygame.display.set_mode(
    (SIM_WIDTH, SIM_HEIGHT),
    pygame.RESIZABLE
)

pygame.display.set_caption("Simulation")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 24)
title_font = pygame.font.Font(None, 32)

# Physical simulation space
WORLD_WIDTH = 1000
WORLD_HEIGHT = 1000


# --------------------------------------------------
# Helper functions
# --------------------------------------------------

def random_position():
    """Generate a random physical position."""
    return (
        random.uniform(0, WORLD_WIDTH),
        random.uniform(0, WORLD_HEIGHT)
    )


def world_to_screen(position, width, height):
    """Convert physical coordinates to screen coordinates."""
    x, y = position

    screen_x = x / WORLD_WIDTH * width
    screen_y = y / WORLD_HEIGHT * height

    return int(screen_x), int(screen_y)


# --------------------------------------------------
# Body class
# --------------------------------------------------

class Body:
    def __init__(self, name, position, mass, velocity, radius, color):
        self.name = name
        self.position = position
        self.mass = mass
        self.velocity = velocity
        self.radius = radius
        self.color = color

    def update(self):
        # Dummy movement for now
        self.position = random_position()

    def draw(self, screen, width, height):
        screen_position = world_to_screen(
            self.position,
            width,
            height
        )

        # Body
        pygame.draw.circle(
            screen,
            self.color,
            screen_position,
            self.radius
        )

        # Name
        text = font.render(
            self.name,
            True,
            "white"
        )

        text_rect = text.get_rect(
            center=(
                screen_position[0],
                screen_position[1] - self.radius - 15
            )
        )

        padding = 4

        box_rect = text_rect.inflate(
            padding * 2,
            padding * 2
        )

        pygame.draw.rect(
            screen,
            "black",
            box_rect,
            border_radius=4
        )

        pygame.draw.rect(
            screen,
            "white",
            box_rect,
            width=1,
            border_radius=4
        )

        screen.blit(text, text_rect)


# --------------------------------------------------
# Create bodies
# --------------------------------------------------

sun = Body(
    name="Sun",
    position=(500, 500),
    mass=1.989e30,
    velocity=(0, 0),
    radius=25,
    color="yellow"
)

MIN_PLANETS = 3
MAX_PLANETS = 10

number_of_planets = random.randint(
    MIN_PLANETS,
    MAX_PLANETS
)

bodies = [sun]

for i in range(number_of_planets):
    planet = Body(
        name=f"Planet {i + 1}",
        position=random_position(),
        mass=random.uniform(1e23, 1e25),
        velocity=(0, 0),
        radius=random.randint(5, 15),
        color="blue"
    )

    bodies.append(planet)


# --------------------------------------------------
# Analytics window
# --------------------------------------------------

analytics_window = Window(
    "Analytics",
    size=(500, 600)
)

analytics_renderer = Renderer(
    analytics_window
)


# --------------------------------------------------
# Main loop
# --------------------------------------------------

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # ----------------------------------------------
    # Update simulation
    # ----------------------------------------------

    for body in bodies:
        if body != sun:
            body.update()


    # ----------------------------------------------
    # Draw simulation
    # ----------------------------------------------

    width, height = screen.get_size()

    screen.fill("black")

    for body in bodies:
        body.draw(
            screen,
            width,
            height
        )

    pygame.display.flip()

    # --------------------------------------------------
    # Analytics window
    # --------------------------------------------------

    analytics_window = Window(
        "Analytics",
        size=(500, 600)
    )

    analytics_renderer = Renderer(analytics_window)

    # --------------------------------------------------
    # Main loop
    # --------------------------------------------------

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ----------------------------------------------
        # Update simulation
        # ----------------------------------------------

        for body in bodies:
            if body != sun:
                body.update()

        # ----------------------------------------------
        # Draw simulation
        # ----------------------------------------------

        width, height = screen.get_size()

        screen.fill("black")

        for body in bodies:
            body.draw(screen, width, height)

        pygame.display.flip()

        # ----------------------------------------------
        # Draw analytics
        # ----------------------------------------------

        analytics_renderer.draw_color = (
            20, 20, 20, 255
        )

        analytics_renderer.clear()

        y = 20

        # Title
        title = font.render(
            "SIMULATION ANALYTICS",
            True,
            "white"
        )

        title_texture = Texture.from_surface(
            analytics_renderer,
            title
        )

        title_texture.draw(
            dstrect=(
                20,
                y,
                title.get_width(),
                title.get_height()
            )
        )

        y += 50

        # Body information
        for body in bodies:
            name_text = font.render(
                body.name,
                True,
                body.color
            )

            name_texture = Texture.from_surface(
                analytics_renderer,
                name_text
            )

            name_texture.draw(
                dstrect=(
                    20,
                    y,
                    name_text.get_width(),
                    name_text.get_height()
                )
            )

            y += 25

            position_text = font.render(
                f"Position: "
                f"({body.position[0]:.2f}, "
                f"{body.position[1]:.2f})",
                True,
                "white"
            )

            position_texture = Texture.from_surface(
                analytics_renderer,
                position_text
            )

            position_texture.draw(
                dstrect=(
                    35,
                    y,
                    position_text.get_width(),
                    position_text.get_height()
                )
            )

            y += 25

            mass_text = font.render(
                f"Mass: {body.mass:.3e}",
                True,
                "white"
            )

            mass_texture = Texture.from_surface(
                analytics_renderer,
                mass_text
            )

            mass_texture.draw(
                dstrect=(
                    35,
                    y,
                    mass_text.get_width(),
                    mass_text.get_height()
                )
            )

            y += 40

        analytics_renderer.present()

        clock.tick(10)

    pygame.quit()