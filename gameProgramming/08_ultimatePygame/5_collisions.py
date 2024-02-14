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
#snailXpos = 800
snailRect = snailSurface.get_rect(midbottom = (600,300))

playerSurface = pygame.image.load('img/ultimatePygame/graphics/Player/player_walk_1.png').convert_alpha()
playerRect = playerSurface.get_rect(bottomright = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    screen.blit(skySurface,(0,0))
    screen.blit(groundSurface,(0,300))
    screen.blit(textSurface,(300,50))

    snailRect.x -= 4
    if snailRect.right <= 0:
        snailRect.left = 800
    screen.blit(snailSurface,snailRect)
    playerRect.left 
    screen.blit(playerSurface,playerRect)

    if playerRect.colliderect(snailRect):
        print("collision")

    mousePos = pygame.mouse.get_pos
    if playerRect.collidepoint(mousePos):
        
    pygame.display.update()
    clock.tick(60)