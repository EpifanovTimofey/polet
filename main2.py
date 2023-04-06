import pygame, time, random

j = pygame.display.set_mode([1500, 500])
y1 = 100
x1 = 100
sky = -5
skx = 5
r = pygame.Rect(100,100,200,200)
pygame.draw.rect(j,[0,100,255],r)
while True:
    j.fill([0, 0, 0])
    time.sleep(1 / 60)
    pygame.draw.rect(j, [0, 100, 255], r)
    r.x += skx
    r.y += sky
    if r.x > 1500:
        r.right = 0
    pygame.display.flip()
    if r.top < 0:
        r.top = 0
        sky = -sky
    if r.bottom > 500:
        r.bottom = 500
        sky = -sky
