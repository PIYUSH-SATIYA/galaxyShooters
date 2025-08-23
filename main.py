import pygame
from pygame.locals import *

def main():
    # Define fps
    clock = pygame.time.Clock()
    fps = 50

    screenWidth = 600
    screenHeight = 800

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('Galaxy Shooter')

    # Background Image
    bg = pygame.image.load('assets/images/background.png')

    def draw_bg():
        screen.blit(bg, (0, 0))

    run = True
    while run:
        clock.tick(fps)
        draw_bg()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
