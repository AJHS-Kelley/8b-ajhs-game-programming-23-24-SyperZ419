import pygame

# Almost done, get it finished please! 

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
testFont = pygame.font.Font('img/ultimatePygame/font/Pixeltype.ttf', 50)

skySurface = pygame.image.load("img/ultimatePygame/graphics/Sky.png").convert()
groundSurface = pygame.image.load("img/ultimatePygame/graphics/ground.png").convert()

scoreSurface = testFont.render("My Game", False, (64,64,64))
scoreRect = scoreSurface.get_rect(center = (400,50))

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
        # if event.type == pygame.MOUSEMOTION:
        #     if playerRect.collidepoint(event.pos):
        #         print("collision")
    
    screen.blit(skySurface,(0,0))
    screen.blit(groundSurface,(0,300))
    pygame.draw.rect(screen, "#c0e8ec", scoreRect)
    pygame.draw.rect(screen, "#c0e8ec", scoreRect, 10)
    #pygame.draw.ellipse(screen, "Brown", pygame.Rect(50,200,100,100))
    #pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(),10)  
    screen.blit(scoreSurface,scoreRect)

    snailRect.x -= 4
    if snailRect.right <= 0:
        snailRect.left = 800
    screen.blit(snailSurface,snailRect)
    playerRect.left 
    screen.blit(playerSurface,playerRect)

    #if playerRect.colliderect(snailRect):
        #print("collision")

    #mousePos = pygame.mouse.get_pos
    #if playerRect.collidepoint(mousePos):
        #print(pygame.mouse.get_pressed())
    
    pygame.display.update()
    clock.tick(60)