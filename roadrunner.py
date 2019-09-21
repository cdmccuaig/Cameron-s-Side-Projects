import pygame
import random


pygame.init()

ScreenWidth = 500
ScreenHeight = 312

win = pygame.display.set_mode((ScreenWidth, ScreenHeight))

pygame.display.set_caption("Road Runner")


an_anvil = pygame.image.load('anvil.png')
walkRight = pygame.image.load('R.png')
walkLeft = pygame.image.load('L.png')
bg = pygame.image.load('bg.jpg')
game_over = pygame.image.load("gameover.jpg")

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.isJump = False
        self.jumpCount = 7
        self.left = False
        self.right = False
        self.hitbox = (self.x + 5, self.y, 50, 60)
        
    def draw(self, win):
        if self.left:
            win.blit(walkLeft, (self.x,self.y))
        elif self.right:
            win.blit(walkRight, (self.x,self.y)) 
        else:
            win.blit(walkRight, (self.x,self.y)) 
        self.hitbox = (self.x+5, self.y,50,60)
    
    def hit(self):
        win.blit(game_over, (0,0))
        pygame.display.update()
            
class projectile(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.hitbox = (self.x - 5, self.y,57,50)
    
    def draw(self, win):
        if self.y >= -64:
            win.blit(an_anvil, (self.x,self.y))
        self.hitbox = (self.x - 5, self.y,57,50)        
        
    def falling(self):
        self.y = self.y + self.vel
        if self.y > ScreenHeight:
            self.x = random.randrange(64,ScreenWidth-64)
            self.y = -25

def redrawGameWindow():
    win.blit(bg, (0,0))
    roadrunner.draw(win)
    anvil.draw(win)
    pygame.display.update()    

# mainloop
roadrunner = player(250, 250, 64, 64)
anvil = projectile(250,-64,64,64)
run = True
while run:
    pygame.time.delay(50)
    
    anvil.falling()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    if anvil.y - 10 < roadrunner.hitbox[1] + roadrunner.hitbox[3] \
       and anvil.y + 10 > roadrunner.hitbox[1]:
        if anvil.x + 10 > roadrunner.hitbox[0] and anvil.x - 10 \
           < roadrunner.hitbox[0] + roadrunner.hitbox[2]:
            roadrunner.hit()
            pygame.time.delay(5000)
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and roadrunner.x > roadrunner.vel:
        roadrunner.x -= roadrunner.vel 
        roadrunner.left = True
        roadrunner.right = False
    elif keys[pygame.K_RIGHT] and roadrunner.x < ScreenWidth - roadrunner.width \
         - roadrunner.vel:
        roadrunner.x += roadrunner.vel
        roadrunner.right = True
        roadrunner.left = False
        
    else:
        roadrunner.right = False
        roadrunner.left = False
        
    if not(roadrunner.isJump):
        if keys[pygame.K_SPACE]:
            roadrunner.isJump = True
            roadrunner.right = False
            roadrunner.left = False

    else:
        if roadrunner.jumpCount >= -7:
            neg = 1
            if roadrunner.jumpCount < 0:
                neg = -1
            roadrunner.y -= (roadrunner.jumpCount ** 2) * 0.5 * neg
            roadrunner.jumpCount -= 1
            
        else:
            roadrunner.isJump = False
            roadrunner.jumpCount = 7
           
    ## terminate game if escape is hit
    
    if keys[pygame.K_ESCAPE]:
        run = False
    
    
    redrawGameWindow()
    
        

pygame.quit()


