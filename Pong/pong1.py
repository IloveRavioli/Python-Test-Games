
import pygame,sys

#this is the initaial setup and allat
pygame.init()#initialises pygame functions
clock = pygame.time.Clock()

widthVar = 720
heightVar = 540
screenFrame = pygame.display.set_mode((widthVar,heightVar))#the python game window setup
pygame.display.set_caption("pong game #real")

running= True
while running ==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False#may change later but this is used to end the loop of the game
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Escape key pressed! Exiting...")
                running=False#may change later but this is used to end the loop of the game
                pygame.quit()
                sys.exit()
    pygame.display.flip()
    clock.tick(60)
        







