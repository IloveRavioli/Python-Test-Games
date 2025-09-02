
import pygame,sys

#this is the initaial setup and allat
pygame.init()#initialises pygame functions
clock = pygame.time.Clock()

widthVar = 720
heightVar = 540
screenFrame = pygame.display.set_mode((widthVar,heightVar))#the python game window setup
pygame.display.set_caption("pong game #real")

#game rectangles 
BALLz = pygame.Rect(widthVar/2 - 15,heightVar/2 - 15,30,30)
Player = pygame.Rect(widthVar-20,heightVar-70,10,140)
Opposition = pygame.Rect(10,heightVar-70,10,140)
#the playe squares are to be 10 pixels away from the edges so 
#the opposition is on the left hand side whilst the player is on the right side

Background= pygame.Color('grey12')
GreyTrue=(200,200,200)
TRUERed=(255,0,0)

BallX = 7
BallY = 7

running= True
while running ==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False#may change later but this is used to end the loop of the game
            pygame.quit()
            sys.exit()        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:#checks if the player presses escape
                print("Escape key pressed! Exiting...")
                running=False#may change later but this is used to end the loop of the game
                pygame.quit()
                sys.exit()

    #Physics
    BALLz.x += BallX
    BALLz.y += BallY

    if BALLz.top <= 0 or BALLz.bottom >= heightVar:
        BallY *= -1
    if BALLz.left <= 0 or BALLz.right >= widthVar:
        BallX *= -1


    #Draw

    screenFrame.fill(Background)#Backround

    pygame.draw.aaline(screenFrame,GreyTrue,(widthVar/2,0),(widthVar/2,heightVar))    
    pygame.draw.rect(screenFrame,GreyTrue,Player)
    pygame.draw.rect(screenFrame,GreyTrue,Opposition)
    pygame.draw.ellipse(screenFrame,TRUERed,BALLz)
    

    pygame.display.flip()
    clock.tick(60)
        







