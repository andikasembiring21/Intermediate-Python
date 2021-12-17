import pygame
successes,failures =pygame.init()
print("{0} successes and {1} failures".format(successes,failures))

screen = pygame.display.set_mode((720,480))
clock =pygame.time.Clock()
fps =100
BLACK=(0,0,255)
WHITE=(0,255,0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((32,32))
        self.image.fill(WHITE)
        self.rect=self.image.get_rect()
        self.velocity=[0,0]

    def update(self):
        self.rect.move_ip(*self.velocity)
        
player=Player()
running=True
while running:
    dt=clock.tick(fps)/1000

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running =False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.velocity[1]=-200*dt
            elif event.key == pygame.K_s:
                player.velocity[1]=200*dt
            elif event.key == pygame.K_a:
                player.velocity[0]=-200*dt
            elif event.key == pygame.K_d:
                player.velocity[0]=200*dt
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.velocity[1]=0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                player.velocity[0]=0
                
    player.update()
    screen.blit(player.image,player.rect)
    pygame.display.update()
    
print("exited")
quit()


"""
rect =pygame.Rect((0,0),(32,32))
image=pygame.Surface((32,32))
image.fill(WHITE)
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rect.move_ip(0,-2)
            elif event.key == pygame.K_s:
                rect.move_ip(0,2)
            elif event.key == pygame.K_a:
                rect.move_ip(-2,0)
            elif event.key == pygame.K_d:
                rect.move_ip(2,0)
                
    screen.fill(BLACK)
    screen.blit(image,rect)
    pygame.display.update()
"""
