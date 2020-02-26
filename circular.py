import pygame

pygame.init()
width  = 400
height = 400
screen = pygame.display.set_mode((width, height))
surf1 = pygame.Surface((width,height))
surf1.fill((0,255,0))
pygame.draw.circle(surf1, (0,0,0), (200,200), 5)
screen.blit(surf1, (0,0))
exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()
pygame.quit()