import pygame, time, random

j = pygame.display.set_mode([1500, 500])
y1 = 100
x1 = 100
sky = -5
skx = 5
while True:
    j.fill([0, 0, 0])
    time.sleep(1 / 60)
    pygame.draw.rect(j,[0,100,255],[x1,y1,200,200])
    y1 += sky
    if y1 < 0:
        y1 = 0
        sky = -sky
    if y1 > 300:
        y1 = 300
        sky = -sky

    x1 += skx
    if x1 > 1500:
        x1 = -200
    pygame.display.flip()