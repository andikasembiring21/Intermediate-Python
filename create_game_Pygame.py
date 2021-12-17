import pygame
pygame.init()
WIDTH = 300
HEIGHT = 200
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT),pygame.NOFRAME)
pygame.display.set_caption('My Game')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 225, 255)
SCREEN.fill(YELLOW)
pygame.display.flip()

is_running =True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running=False

pygame.quit()

"""
flag                     description

pygame.FULLSCREEN        window is fullscreen
pygame.RESIZABLE         window is resizeable
pygame.NOFRAME           window has no border or controls
pygame.DOUBLEBUF         use double buffer - recommended for HWSURFACE or OPENGL
pygame.HWSURFACE         window is hardware accelerated, only possible in combination with
FULLSCREEN
pygame.OPENGL            window is renderable by OpenGL
"""
