# Final Project, Xavier Oliver, v0.0
import sys, random, pygame

resolution = 0 # 0 = Low, 1 = High

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080

pygame.init()
titleFont = pygame.font.Font("font/IMFellEnglish-Italic.ttf", 50)
difficulty = int(input("Please choose a difficulty. Enter 1 for Normal. Enter 2 for Hard.\n"))

if difficulty == 1:
    pygame.display.set_caption('Generic RPG - Normal Mode')
else:
    pygame.display.set_caption('Generic RPG - Hard Mode')

titleBackground = pygame.image.load("img/finalProject/backgrounds/backgrounds/2.png")
textSurface = titleFont.render("Generic RPG", False, "Black")
screen = pygame.display.set_mode((x, y))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(titleBackground,(0,0))

    pygame.display.update()
    clock.tick(60)