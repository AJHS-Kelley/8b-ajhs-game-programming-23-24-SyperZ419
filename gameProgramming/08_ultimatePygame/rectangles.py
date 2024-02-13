import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
testFont = pygame.font.Font('img/ultimatePygame/font/Pixeltype.ttf', 50)

skySurface = pygame.image.load("img/ultimatePygame/graphics/Sky.png").convert()
groundSurface = pygame.image.load("img/ultimatePygame/graphics/ground.png").convert()
textSurface = testFont.render("My Game", False, "Black")

snailSurface = pygame.image.load("img/ultimatePygame/graphics/snail/snail1.png").convert_alpha()
snailXpos = 800

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    screen.blit(skySurface,(0,0))
    screen.blit(groundSurface,(0,300))
    screen.blit(textSurface,(300,50))
    snailXpos -= 4
    if snailXpos < -100:
        snailXpos = 800
    screen.blit(snailSurface,(snailXpos,250))
    
    pygame.display.update()
    clock.tick(60)