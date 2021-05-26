import pygame,math,random
#from pygame import gfxdraw
pygame.init()
win = pygame.display.set_mode((800,600))
g = -10
dt = 0.01

class Ball:
    def __init__(self, Q0, l):
        self.Q0 = math.radians(Q0)         #math.radians(Q0)
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


b0 = Ball(50,300)
b1 = Ball(-30,300)
#Q0 = math.radians(50)
#l = 300


run = True
while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
         
    win.fill((0, 0, 0))
    #y = 500 - y_pos
    if abs(b0.Q0 - b1.Q0) <= (2*math.atan2(10, 300)):
        u0 = b0.w
        u1 = b1.w
        b0.w = u1
        b1.w = u0
    
    
    pygame.draw.line(win, (64, 64, 64), (400, 0), (b0.x, b0.y_pos), 5)
    pygame.draw.line(win, (64, 64, 64), (400, 0), (b1.x, b1.y_pos), 5)
    pygame.draw.circle(win, (255, 0, 0), (b0.x, b0.y_pos), 10)
    pygame.draw.circle(win, (255, 0, 0), (b1.x, b1.y_pos), 10)
    b0.mechanics()
    b1.mechanics()
        
        
    pygame.display.update()


pygame.quit()
