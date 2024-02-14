import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
testFont = pygame.font.Font(None, 50)

skySurface = pygame.image.load("img/ultimatePygame/Sky.jpg")
groundSurface = pygame.image.load("img/ultimatePygame/Ground.jpg")
textSurface = testFont.render("My game", False, "Green")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    screen.blit(skySurface,(0,0))
    screen.blit(groundSurface,(0,300))
    screen.blit(textSurface,(300,50))
    
    pygame.display.update()
    clock.tick(60)