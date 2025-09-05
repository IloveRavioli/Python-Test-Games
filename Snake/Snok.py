import pygame,sys

pygame.init()

run=True

while run==True:
    
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run=False
            pygame.quit()