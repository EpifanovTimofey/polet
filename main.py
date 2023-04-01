import pygame, time, random

j = pygame.display.set_mode([1500, 500])
y1 = 100
while True:
    j.fill([0, 0, 0])
    time.sleep(1 / 60)
    pygame.draw.rect(j,[0,100,255],[100,y1,200,200])
    y1 -= 1
    pygame.display.flip()