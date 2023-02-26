import pygame

#initializing pygame

pygame.init()

#creating gaming window
screen= pygame.display.set_mode((800,600))

#logo and title
pygame.display.set_caption("Space Invaders")
icon= pygame.image.load("C:/Users/nilas/Downloads/spaceship.png")
pygame.display.set_icon(icon)

#adding image 
playerimg= pygame.image.load("C:/Users/nilas/Downloads/icons8-space-fighter-50.png")
playerX= 370
playerY=480

def player():
    screen.blit(playerimg,(playerX,playerY))

#game loop
running=True
while running:
    #background colour
    screen.fill((128,0,43))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False
            
    #Calling the function        
    player()
    pygame.display.update()
    
        