import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all elaments
    # update everything
    pygame.display.update()