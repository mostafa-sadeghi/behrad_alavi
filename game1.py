import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

BlACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


display_surface.fill(BLUE)

pygame.draw.line(display_surface, RED, (0,0), (100, 100), 5)

pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2), 200, 0)
pygame.draw.circle(display_surface, MAGENTA, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2), 195, 5)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()