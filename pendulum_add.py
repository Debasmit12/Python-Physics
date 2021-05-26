import pygame,math,random
#from pygame import gfxdraw
pygame.init()
win = pygame.display.set_mode((800,600))
g = -10
dt = 0.01

class Ball:
    def __init__(self, Q0, l):
        self.Q0 = Q0          #math.radians(Q0)
        self.l = l
        self.w = 0
        self.a = (g/self.l)*math.sin(self.Q0)
        self.x = (self.l)*math.sin(self.Q0) + 400
        self.y_pos = (self.l)*math.cos(Q0)

    def mechanics(self):
        self.Q0 +=self.w*dt
        self.w +=self.a*dt
        self.a = (g/self.l)*math.sin(self.Q0)
        self.x =self.l*math.sin(self.Q0) + 400
        self.y_pos =self.l*math.cos(self.Q0)


b0 = [Ball(50,300)]

#Q0 = math.radians(50)
#l = 300


run = True
while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
         if event.type == pygame.MOUSEBUTTONDOWN:
             x,y = pygame.mouse.get_pos()
             Q0 = math.atan2((x-400), y)
             l = math.sqrt((y*y) + (x-400)*(x-400))
             b0.append(Ball(Q0,l))
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_d:
                 b0.pop()
             if event.key == pygame.K_ESCAPE:
                 run = False


    win.fill((0, 0, 0))
    #y = 500 - y_pos
    for b1 in b0:
        pygame.draw.line(win, (64, 64, 64), (400, 0), (b1.x, b1.y_pos), 5)
        pygame.draw.circle(win, (255, 0, 0), (b1.x, b1.y_pos), 10)
        b1.mechanics()
        
        
    pygame.display.update()


pygame.quit()
