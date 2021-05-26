import pygame 
from pygame import gfxdraw
pygame.init()
win = pygame.display.set_mode((800,600))

'''def draw_circle(surface, x1, y1, radius, color):
    gfxdraw.aacircle(surface, x1, y1, radius, color)
    gfxdraw.filled_circle(surface, x1, y1, radius, color)'''

x = 20
y = 300
y_pos = 500 - y
vy = 63.2
vx = 30
dt = 0.01
g = -10
'''x += vx*dt
y_pos += vy*dt
vy += g*dt'''
run = True
while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False

    #keys = pygame.key.get_pressed()

    '''if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel'''
    
    #win.fill((0, 0, 0))
    pygame.draw.circle(win, (255, 0, 0), (x, y), 1)
    pygame.display.update()
    if x >= 790:
        vx *= -1
    if x <= 10:
        vx *= -1
    if y >= 590:
        vy *= -1
    if y <= 10:
        vy *= -1
    x += vx*dt
    y_pos += vy*dt
    vy += g*dt
    y = 500 - y_pos

    #if x > 800:
        #run = False   


pygame.quit()
