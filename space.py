import pygame
pygame.init()
width=750
height=650
a=pygame.display.set_mode((width,height))
pygame.display.set_caption("space rush")

exit_game=False
game_over=False
x=100
y=350
vx=0
laserx = x + 1
lasery = y - 55
lx=0
ly=0
vy=0
FPS=60
clock=pygame.time.Clock()
def bg(file):
    c=pygame.image.load(file)
    c=pygame.transform.scale(c,(width,height))
    a.blit(c,(0,0))

def obs(file,x,y):
    c=pygame.image.load(file)
    a.blit(c,(x,y))

while not exit_game:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()

        if events.type==pygame.KEYDOWN:
            if events.key==pygame.K_RIGHT:
                vx=20
                vy=0
            if events.key==pygame.K_LEFT:
                vx=-20
                vy=0
            if events.key==pygame.K_UP:
                vy=-20
                vx=0
            if events.key==pygame.K_DOWN:
                vy=20
                vx=0
            if events.key==pygame.K_SPACE:
                ly-=20
                lx=0
       #elif events.type==pygame.KEYUP:
        #    vx=0
         #   vy=0


    x+=vx
    y+=vy
    laserx+=lx
    lasery+=ly

    if lasery<y-400:
        lasery=y-55
        laserx=x+1
        lx=0
        ly=0


    bullety='C:/Users/lenovo/Desktop/space/lasery.png'
    back='C:/Users/lenovo/Desktop/space/back.png'
    ship='C:/Users/lenovo/Desktop/space/ship.png'
    bg(back)
    obs(ship,x,y)
    obs(bullety,laserx,lasery)
    clock.tick(FPS)
    pygame.display.update()

