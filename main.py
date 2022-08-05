from configparser import RawConfigParser
import pygame
import os
import time


gameIcon = pygame.image.load('Assets/spaceship_red.png')
pygame.display.set_icon(gameIcon)


pygame.font.init()
pygame.mixer.init()
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Outerspace",)
vol = 1
eff = 1
red = (200, 0, 0)
green = (0, 200, 0)
grey = (128, 128, 128)
bright_grey = (192, 192, 192)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
jblkacolor = (0, 0, 26)
silver = (191, 191, 191)
red = (255, 77, 77)
yo = (0, 230, 134)
BLUE = (0,0,255)




bfireball = []
rfireball = []
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

barredhp = pygame.Rect(25,25,150,10)
barbluehp = pygame.Rect(700,25,150,10)




HEALTH_FONT = pygame.font.Font('fonts/airstrike.ttf', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
RVEL = 5
BVEL = 5



SUPER_VEL = 12
FIREBALL_VEL = 6
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 100,80
BALL_WIDTH, BALL_HEIGHT  = 110, 90
super_rrate = 0
super_brate = 0


YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
SBLUEHIT = pygame.USEREVENT + 3
SREDHIT = pygame.USEREVENT + 4
SLOWTIMERR = pygame.USEREVENT + 5
SLOWTIMERB = pygame.USEREVENT + 6
slowtimerr1 = pygame.USEREVENT + 7
slowtimerb1 = pygame.USEREVENT + 8
medcdr = pygame.USEREVENT + 24
medcdb = pygame.USEREVENT + 25


RED_FIREBALL = pygame.image.load(os.path.join('Assets', 'redfireball/redfireball.png'))
danr = pygame.transform.scale(RED_FIREBALL,(BALL_HEIGHT,BALL_WIDTH))
BLUE_FIREBALL = pygame.image.load(os.path.join('Assets', 'bluefireball/bluefireball.png'))
danb = pygame.transform.scale(BLUE_FIREBALL,(BALL_HEIGHT,BALL_WIDTH))

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space2.png')), (WIDTH, HEIGHT))

INFOBG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'bg.png')), (WIDTH, HEIGHT))

BARWIDTH, BARHEIGHT = 200,200

#blue bar things
bsbar0 = pygame.image.load('Assets/bluefireball/superbar0.png')
bsbar25 = pygame.image.load('Assets/bluefireball/superbar25.png')
bsbar50 = pygame.image.load('Assets/bluefireball/superbar50.png')
bsbar75 = pygame.image.load('Assets/bluefireball/superbar75.png')
bsbar100 = pygame.image.load('Assets/bluefireball/superbar100.png')

#red bar things
rsbar0 = pygame.image.load('Assets/redfireball/superbar0.png')
rsbar25 = pygame.image.load('Assets/redfireball/superbar25.png')
rsbar50 = pygame.image.load('Assets/redfireball/superbar50.png')
rsbar75 = pygame.image.load('Assets/redfireball/superbar75.png')
rsbar100 = pygame.image.load('Assets/redfireball/superbar100.png')

# red transform things
rsbar0 = pygame.transform.scale(rsbar0,(BARWIDTH, BARHEIGHT))
rsbar25 = pygame.transform.scale(rsbar25,(BARWIDTH, BARHEIGHT))
rsbar50 = pygame.transform.scale(rsbar50,(BARWIDTH, BARHEIGHT))
rsbar75 = pygame.transform.scale(rsbar75,(BARWIDTH, BARHEIGHT))
rsbar100 = pygame.transform.scale(rsbar100,(BARWIDTH, BARHEIGHT))

#blue transform things
bsbar0 = pygame.transform.scale(bsbar0,(BARWIDTH, BARHEIGHT))
bsbar25 = pygame.transform.scale(bsbar25,(BARWIDTH, BARHEIGHT))
bsbar50 = pygame.transform.scale(bsbar50,(BARWIDTH, BARHEIGHT))
bsbar75 = pygame.transform.scale(bsbar75,(BARWIDTH, BARHEIGHT))
bsbar100 = pygame.transform.scale(bsbar100,(BARWIDTH, BARHEIGHT))


aqua = (128, 255, 255)
icy = (0,0,0)
def draw_window(red, yellow, rfire, bfire, red_slowness, blue_slowness, medcharger, medchargeb, red_bullets, yellow_bullets, blue_hitbox, red_hitbox, red_health, yellow_health):
    global SUPER_VAL
    

    
    yhp = yellow_health 
    rhp = red_health
    rslow = red_slowness 
    bslow = blue_slowness
    rslbar = pygame.Rect(25,50,rslow,10)
    bslbar =pygame.Rect(700,50,bslow,10)
    greenredhp = pygame.Rect(25,25,yhp,10)
    greenbluehp = pygame.Rect(700,25,rhp,10)
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN, jblkacolor, BORDER)
    pygame.draw.rect(WIN, RED, barredhp)
    pygame.draw.rect(WIN, GREEN, greenredhp)
    pygame.draw.rect(WIN, RED, barbluehp)
    pygame.draw.rect(WIN, GREEN, greenbluehp)
    pygame.draw.rect(WIN, aqua, rslbar)
    pygame.draw.rect(WIN, aqua, bslbar)

 
                           

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    if super_rrate == 0:
        WIN.blit(rsbar0,(25,450))
      
    if super_rrate == 25:
        WIN.blit(rsbar25,(25,450))
      
    if super_rrate == 50:
        WIN.blit(rsbar50,(25,450))
       
    if super_rrate == 75:
        WIN.blit(rsbar75,(25,450))
        
    if super_rrate == 100:
        WIN.blit(rsbar100,(25,450))
      

    if super_brate == 0:
        WIN.blit(bsbar0,(650,450))
       
    if super_brate == 25:
        WIN.blit(bsbar25,(650,450))
     
    if super_brate == 50:
        WIN.blit(bsbar50,(650,450))
    
    if super_brate == 75:
        WIN.blit(bsbar75,(650,450))
      
    if super_brate == 100:
        WIN.blit(bsbar100,(650,450))
      
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, BLUE, bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    
    for hitbox_S in red_hitbox:
        pygame.draw.rect(WIN, icy, hitbox_S)
        WIN.blit(danr,(rfire.x,rfire.y))

    for hitbox_S in blue_hitbox:
        pygame.draw.rect(WIN, icy, hitbox_S)
        WIN.blit(danb,(bfire.x,bfire.y))


        
    
        
    
    
        
        






    pygame.display.update()




def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - RVEL > 0:  # LEFT
        yellow.x -= RVEL
    if keys_pressed[pygame.K_d] and yellow.x + RVEL + yellow.width < BORDER.x:  # RIGHT
        yellow.x += RVEL
    if keys_pressed[pygame.K_w] and yellow.y - RVEL > 0:  # UP
        yellow.y -= RVEL
    if keys_pressed[pygame.K_s] and yellow.y + RVEL + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += RVEL
   
def handle_fireball_movement(rfire,bfire):
    rfire.x += SUPER_VEL
    rfire.x += SUPER_VEL



def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_KP_4] and red.x - BVEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= BVEL
    if keys_pressed[pygame.K_KP_6] and red.x + BVEL + red.width < WIDTH:  # RIGHT
        red.x += BVEL
    if keys_pressed[pygame.K_KP_8] and red.y - BVEL > 0:  # UP
        red.y -= BVEL
    if keys_pressed[pygame.K_KP_5] and red.y + BVEL + red.height < HEIGHT - 15:  # DOWN
        red.y += BVEL


def handle_bullets(yellow_bullets, red_bullets, red_hitbox, blue_hitbox, yellow, red,rfire,bfire):
    global SUPER_VAL
   
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
    
    for hitbox_S in blue_hitbox:
        hitbox_S.x -= SUPER_VEL
        bfire.x = hitbox_S.x - 15
        bfire.y = hitbox_S.y - 45

        if yellow.colliderect(hitbox_S):
            pygame.event.post(pygame.event.Event(SBLUEHIT)) 
            blue_hitbox.remove(hitbox_S)
        elif hitbox_S.x < 0:
            blue_hitbox.remove(hitbox_S)
        pygame.display.flip()

    for hitbox_S in red_hitbox:
        hitbox_S.x += SUPER_VEL
        rfire.x = hitbox_S.x - 15
        rfire.y = hitbox_S.y - 45
        if red.colliderect(hitbox_S):
            pygame.event.post(pygame.event.Event(SREDHIT)) 
            red_hitbox.remove(hitbox_S)
        elif hitbox_S.x > WIDTH:
            red_hitbox.remove(hitbox_S)
        pygame.display.flip()
    
    for f in bfireball:
        f.x += 1
        


jblkacolor2 = (179, 255, 223)            

def draw_winner(text):
    global super_brate
    global super_rrate
    super_rrate = 0
    super_brate = 0
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.fill(jblkacolor)
    largeText = pygame.font.Font("fonts/airstrike.ttf",70,bold=True)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/2.5))
    WIN.blit(TextSurf, TextRect)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        button("Restart",150,450,150,50,red,jblkacolor,main)
        button("Menu",550,450,150,50,red,jblkacolor,game_intro)
        pygame.display.update()
        clock.tick(15)
    



def text_objects(text, font):
    textSurface = font.render(text, True, jblkacolor2)
    return textSurface, textSurface.get_rect()

def text_objects1(text, font):
    textSurface = font.render(text, True, silver)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(WIN, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(WIN, ic, (x, y, w, h)) 

    smallText = pygame.font.Font("fonts/DIMITRI.ttf", 30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    WIN.blit(textSurf, textRect)


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():
    global pause
    pygame.mixer.music.pause()
    WIN.fill(jblkacolor)
    largeText = pygame.font.Font("fonts/airstrike.ttf", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((WIDTH/2.0), (HEIGHT/3))
    WIN.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
                    unpause()

        button("Continue", 150, 450, 150, 50, red, jblkacolor, unpause)
        button("Menu", 550, 450, 150, 50, red, jblkacolor, game_intro)
        button("Restart", 350, 450, 150, 50, red, jblkacolor, main)

        pygame.display.update()
        clock.tick(15)


def text(text,x,y,color,size,font):
    largeText = pygame.font.SysFont(font,size,bold=True)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = ((WIDTH//x),(HEIGHT//y))
    WIN.blit(TextSurf, TextRect)

def chooserV():
    global vol
    global eff
    if vol == 1:
        volume1()
    if vol == 0:
        on2()

def on3():
    global eff
    eff = 0
    
 
    info = True
    while info:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        WIN.fill(jblkacolor)
        color = (255,0,0)
        pygame.draw.rect(WIN, jblkacolor2, pygame.Rect(260, 10, 4, 700))
        largeText = pygame.font.Font("fonts/airstrike.ttf",30,bold=True)
        TextSurf, TextRect = text_objects("Music", largeText)
        TextRect.center = ((WIDTH/1.5),(HEIGHT/14))
        WIN.blit(TextSurf, TextRect)
        largeText = pygame.font.SysFont("verdana",20,bold=True)
        TextSurf, TextRect = text_objects("• Music And Sound Effects Toggle:-", largeText)
        TextRect.center = ((WIDTH//1.80),(HEIGHT/7))
        WIN.blit(TextSurf, TextRect)
        text("Music:-",2.45,3,jblkacolor,35,"verdana")
        text("Sound Effects :-",1.969,1.869,jblkacolor,35,"verdana")
        
        

      


        

        button("Exit", 10, 230, 250, 115, red, jblkacolor, game_intro)
        button("Gamerules!", 10, 10, 250, 115, red, jblkacolor, info2)
        button("Volume", 10, 120, 250, 115, red, jblkacolor, chooserV)
        if vol == 0:
            button("off", 469, 169, 69, 69, jblkacolor, jblkacolor, volume1)
        if vol == 1:
            button("on", 469, 169, 69, 69, red, jblkacolor, on2)
        if eff == 0:
            button("off", 630, 285, 69, 69, jblkacolor, jblkacolor, volume2)
        if eff == 1:
            button("on", 630, 285, 69, 69, red, jblkacolor, on3)
        pygame.display.update()
        clock.tick(15)

def on2():
    global vol
    vol = 0
    
    
   
    info = True
    while info:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        WIN.fill(jblkacolor)
        color = (255,0,0)
        pygame.draw.rect(WIN, jblkacolor2, pygame.Rect(260, 10, 4, 700))
        largeText = pygame.font.Font("fonts/airstrike.ttf",30,bold=True)
        TextSurf, TextRect = text_objects("Music", largeText)
        TextRect.center = ((WIDTH/1.5),(HEIGHT/14))
        WIN.blit(TextSurf, TextRect)
        largeText = pygame.font.SysFont("verdana",20,bold=True)
        TextSurf, TextRect = text_objects("• Music And Sound Effects Toggle:-", largeText)
        TextRect.center = ((WIDTH//1.80),(HEIGHT/7))
        WIN.blit(TextSurf, TextRect)
        text("Music:-",2.45,3,jblkacolor,35,"verdana")
        text("Sound Effects :-",1.969,1.869,jblkacolor,35,"verdana")
        
        

      


        

        button("Exit", 10, 230, 250, 115, red, jblkacolor, game_intro)
        button("Gamerules!", 10, 10, 250, 115, red, jblkacolor, info2)
        button("Volume", 10, 120, 250, 115, red, jblkacolor, chooserV)
        if vol == 0:
            button("off", 469, 169, 69, 69, jblkacolor, jblkacolor, volume1) 
        if vol == 1:
            button("on", 469, 169, 69, 69, red, jblkacolor, on2)
        if eff == 0:
            button("off", 630, 285, 69, 69, jblkacolor, jblkacolor, volume2)
        if eff == 1:
            button("on", 630, 285, 69, 69, red, jblkacolor, on3)
        pygame.display.update()
        clock.tick(15)



def volume2():
    global eff
    eff = 1
    info = True
    while info:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        WIN.fill(jblkacolor)
        color = (255,0,0)
        pygame.draw.rect(WIN, jblkacolor2, pygame.Rect(260, 10, 4, 700))
        largeText = pygame.font.Font("fonts/airstrike.ttf",30,bold=True)
        TextSurf, TextRect = text_objects("Music", largeText)
        TextRect.center = ((WIDTH/1.5),(HEIGHT/14))
        WIN.blit(TextSurf, TextRect)
        largeText = pygame.font.SysFont("verdana",20,bold=True)
        TextSurf, TextRect = text_objects("• Music And Sound Effects Toggle:-", largeText)
        TextRect.center = ((WIDTH//1.80),(HEIGHT/7))
        WIN.blit(TextSurf, TextRect)
        text("Music:-",2.45,3,jblkacolor,35,"verdana")
        text("Sound Effects :-",1.969,1.869,jblkacolor,35,"verdana")
        
        

      


        
        
        button("Exit", 10, 230, 250, 115, red, jblkacolor, game_intro)
        button("Gamerules!", 10, 10, 250, 115, red, jblkacolor, info2)
        button("Volume", 10, 120, 250, 115, red, jblkacolor, chooserV)
        if vol == 0:
            button("off", 469, 169, 69, 69, jblkacolor, jblkacolor, volume1)
        if vol == 1:
            button("on", 469, 169, 69, 69, red, jblkacolor, on2)
        if eff == 1:
            button("on", 630, 285, 69, 69, red, jblkacolor, on3)
        if eff == 0:
            button("off", 630, 285, 69, 69, jblkacolor, jblkacolor, volume2)
        pygame.display.update()
        clock.tick(15)

def volume1():
    global vol
    vol = 1
    
 
    info = True
    while info:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        WIN.fill(jblkacolor)
        color = (255,0,0)
        pygame.draw.rect(WIN, jblkacolor2, pygame.Rect(260, 10, 4, 700))
        largeText = pygame.font.Font("fonts/airstrike.ttf",30,bold=True)
        TextSurf, TextRect = text_objects("Music", largeText)
        TextRect.center = ((WIDTH/1.5),(HEIGHT/14))
        WIN.blit(TextSurf, TextRect)
        largeText = pygame.font.SysFont("verdana",20,bold=True)
        TextSurf, TextRect = text_objects("• Music And Sound Effects Toggle:-", largeText)
        TextRect.center = ((WIDTH//1.80),(HEIGHT/7))
        WIN.blit(TextSurf, TextRect)
        text("Music:-",2.45,3,jblkacolor,35,"verdana")
        text("Sound Effects :-",1.969,1.869,jblkacolor,35,"verdana")
        
        

      


        
        
        button("Exit", 10, 230, 250, 115, red, jblkacolor, game_intro)
        button("Gamerules!", 10, 10, 250, 115, red, jblkacolor, info2)
        button("Volume", 10, 120, 250, 115, red, jblkacolor, chooserV)
        if vol == 0:
            button("off", 469, 169, 69, 69, jblkacolor, jblkacolor, volume1)
        if vol == 1:
            button("on", 469, 169, 69, 69, red, jblkacolor, on2)
        if eff == 1:
            button("on", 630, 285, 69, 69, red, jblkacolor, on3)
        if eff == 0:
            button("off", 630, 285, 69, 69, jblkacolor, jblkacolor, volume2)
        pygame.display.update()
        clock.tick(15)



def info2(): 
    info = True
    while info:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        WIN.fill(jblkacolor)
        color = (255,0,0)
        pygame.draw.rect(WIN, jblkacolor2, pygame.Rect(260, 10, 4, 700))
        largeText = pygame.font.Font("fonts/airstrike.ttf",30,bold=True)
        TextSurf, TextRect = text_objects("Controls", largeText)
        TextRect.center = ((WIDTH/1.5),(HEIGHT/14))
        WIN.blit(TextSurf, TextRect)
        largeText = pygame.font.SysFont("verdana",20,bold=True)
        TextSurf, TextRect = text_objects("• Player 1:-", largeText)
        TextRect.center = ((WIDTH/2.65),(HEIGHT/7))
        WIN.blit(TextSurf, TextRect)
        largeText = pygame.font.SysFont("verdana",15,bold=True)
        TextSurf, TextRect = text_objects1("# To Move The First Ship Use W,A,S,D ", largeText)
        TextRect.center = ((WIDTH/1.95),(HEIGHT/5))
        WIN.blit(TextSurf, TextRect)
        text("# Use Q Key To Shoot",2.300,4,jblkacolor2,15,"verdana")
        largeText = pygame.font.SysFont("verdana",20,bold=True)
        TextSurf, TextRect = text_objects("• Player 2:-", largeText)
        TextRect.center = ((WIDTH/2.65),(HEIGHT/3.2))
        WIN.blit(TextSurf, TextRect)
        text("# To Move The Second Ship KP 8,4,5,6 Keys ",1.85,2.7,jblkacolor2,15,"verdana")
        text("# Use Right KP (keypad) 7 to Shoot ",1.98,2.4,jblkacolor2,15,"verdana")
        largeText = pygame.font.Font("fonts/airstrike.ttf",30,bold=True)
        TextSurf, TextRect = text_objects("Gameplay", largeText)
        TextRect.center = ((WIDTH/1.50),(HEIGHT/1.9))
        WIN.blit(TextSurf, TextRect)
        largeText = pygame.font.SysFont("verdana",20,bold=True)
        TextSurf, TextRect = text_objects("• Attacking:-", largeText)
        TextRect.center = ((WIDTH/2.59),(HEIGHT/1.7))
        WIN.blit(TextSurf, TextRect)
        text("actived only once when the super bar goes to 100%",1.730,1.45,jblkacolor2,15,"verdana")
        text("#Super: Supers are special attacks they can be",1.820,1.55,jblkacolor2,15,"verdana")
        text("#Charging Super: You Can Charge Your Super",1.835,1.37,jblkacolor2,15,"verdana")
        text("By Hitting The Enemy 4 Times With Normal Bullets.",1.750,1.30,jblkacolor2,15,"verdana")
        largeText = pygame.font.SysFont("verdana",20,bold=True)
        TextSurf, TextRect = text_objects("• Super:-", largeText)
        TextRect.center = ((WIDTH/2.73),(HEIGHT/1.2))
        WIN.blit(TextSurf, TextRect)
        text("#P1 use E to use super and P2 use KP 9",1.950,1.14,jblkacolor2,15,"verdana")
        text("#When someone hits you with their super you get a cooldown of 4 seconds.",1.580,1.10,jblkacolor2,13,"verdana")
      


        


      
        button("Exit", 10, 230, 250, 115, red, jblkacolor, game_intro)
        button("Game rules!", 10, 10, 250, 115, red, jblkacolor, info2)
        button("Volume", 10, 120, 250, 115, red, jblkacolor, chooserV)
        pygame.display.update()
        clock.tick(15)

def info(): 
    info = True
    while info:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        WIN.fill(jblkacolor)
        color = (255,0,0)
        pygame.draw.rect(WIN, jblkacolor2, pygame.Rect(260, 10, 4, 700))
        largeText = pygame.font.Font("fonts/airstrike.ttf",30,bold=True)
        TextSurf, TextRect = text_objects("Controls", largeText)
        TextRect.center = ((WIDTH/1.5),(HEIGHT/14))
        WIN.blit(TextSurf, TextRect)
        largeText = pygame.font.SysFont("verdana",20,bold=True)
        TextSurf, TextRect = text_objects("• Player 1:-", largeText)
        TextRect.center = ((WIDTH/2.65),(HEIGHT/7))
        WIN.blit(TextSurf, TextRect)
        largeText = pygame.font.SysFont("verdana",15,bold=True)
        TextSurf, TextRect = text_objects1("# To Move The First Ship Use W,A,S,D ", largeText)
        TextRect.center = ((WIDTH/1.95),(HEIGHT/5))
        WIN.blit(TextSurf, TextRect)
        text("# Use Q Key To Shoot",2.300,4,jblkacolor2,15,"verdana")
        largeText = pygame.font.SysFont("verdana",20,bold=True)
        TextSurf, TextRect = text_objects("• Player 2:-", largeText)
        TextRect.center = ((WIDTH/2.65),(HEIGHT/3.2))
        WIN.blit(TextSurf, TextRect)
        text("# To Move The Second Ship Use KP 8,4,5,6 ",1.85,2.7,jblkacolor2,15,"verdana")
        text("# Use Right KP (keypad) 7 to Shoot ",1.98,2.4,jblkacolor2,15,"verdana")
        largeText = pygame.font.Font("fonts/airstrike.ttf",30,bold=True)
        TextSurf, TextRect = text_objects("Gameplay", largeText)
        TextRect.center = ((WIDTH/1.50),(HEIGHT/1.9))
        WIN.blit(TextSurf, TextRect)
        largeText = pygame.font.SysFont("verdana",20,bold=True)
        TextSurf, TextRect = text_objects("• Attacking:-", largeText)
        TextRect.center = ((WIDTH/2.59),(HEIGHT/1.7))
        WIN.blit(TextSurf, TextRect) 
        text("actived only once when the super bar goes to 100%",1.730,1.45,jblkacolor2,15,"verdana")
        text("#Super: Supers are special attacks they can be",1.820,1.55,jblkacolor2,15,"verdana")
        text("#Charging Super: You Can Charge Your Super",1.835,1.37,jblkacolor2,15,"verdana")
        text("By Hitting The Enemy 4 Times With Normal Bullets.",1.750,1.30,jblkacolor2,15,"verdana")
        largeText = pygame.font.SysFont("verdana",20,bold=True)
        TextSurf, TextRect = text_objects("• Super:-", largeText)
        TextRect.center = ((WIDTH/2.73),(HEIGHT/1.2))
        WIN.blit(TextSurf, TextRect)
        text("#P1 use E to use super and P2 use KP 9",1.950,1.14,jblkacolor2,15,"verdana")
        text("#When someone hits you with their super you get a cooldown of 4 seconds.",1.580,1.10,jblkacolor2,13,"verdana")



        
      


        


       
        button("Exit", 10, 230, 250, 115, red, jblkacolor, game_intro)
        button("Game rules!", 10, 10, 250, 115, red, jblkacolor, info2)
        button("Volume", 10, 120, 250, 115, red, jblkacolor, chooserV)
        pygame.display.update()
        clock.tick(15)

      


def exit_sure():
    sure = True
    while sure:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        WIN.fill(BLACK)
        largeText = pygame.font.Font("fonts/airstrike.ttf",40,bold=True)
        TextSurf, TextRect = text_objects("Are You Sure You Wanna Exit?", largeText)
        TextRect.center = ((WIDTH/2),(HEIGHT/2.5))
        WIN.blit(TextSurf, TextRect)
        button("Yes",210,450,100,50,red,bright_red,quitgame)
        button("No",550,450,100,50,red,bright_red,game_intro)
        pygame.display.update()
        clock.tick(15)


    

def game_intro():
    global super_brate
    global super_rrate
    mp3_path = 'Sound/open-space.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_path)
    if vol == 0:
        pygame.mixer.music.pause()
    if vol == 1:
        pygame.mixer.music.play()


    super_rrate = 0
    super_brate = 0
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        WIN.blit(SPACE,(0,0))
        largeText = pygame.font.Font("fonts/airstrike.ttf",45,bold=True)
        TextSurf, TextRect = text_objects("× OuterSpace", largeText)
        TextRect.center = ((WIDTH/5),(HEIGHT/12))
        WIN.blit(TextSurf, TextRect)
        largeText1 = pygame.font.SysFont("verdana",20)
        TextSurf, TextRect = text_objects1(" By Hakashi Katake & Jayden...", largeText1)
        TextRect.center = ((WIDTH/4.5),(HEIGHT/7))
        WIN.blit(TextSurf, TextRect)
        color = (48, 141, 70)
        



        
       
        
        
        
        button("Go!", 350, 200, 225, 55, red, jblkacolor, main)
        button("Options",350, 300, 225, 55, red, jblkacolor, info)
        button("Exit", 350, 400, 225, 55, red, jblkacolor, exit_sure)
        

        pygame.display.update()
        clock.tick(15)



def quitgame():
    pygame.quit()
    quit()




    


t1 = 0
def main():
    gamemusic = 'Sound/gamemusic.mp3'
    if vol == 0:
        pygame.mixer.music.pause()
    if vol == 1:
        pygame.mixer.music.load(gamemusic)
        pygame.mixer.music.play(-1) 
    if eff == 1:
        sou = 1
        BULLET_HIT_SOUND = pygame.mixer.Sound('Sound/playerhit.wav')
        BULLET_FIRE_SOUND = pygame.mixer.Sound('Sound/playershot.wav')    
    if eff == 0:
        sou = 0

    
    global pause
    global super_brate
    global super_rrate
    global BVEL
    global RVEL

    blue_slowness = 0
    red_slowness = 0
    super_rrate = 0
    super_brate = 0

    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    rfire = pygame.Rect(yellow.x, yellow.y,BALL_WIDTH,BALL_HEIGHT)
    bfire = pygame.Rect(red.x - 180 + red.width, red.y + red.height//2 - 45,BALL_WIDTH,BALL_HEIGHT)

    blue_ball = pygame.Rect(700, 300, BALL_WIDTH, BALL_HEIGHT)
    red_ball = pygame.Rect(100, 300, BALL_WIDTH, BALL_HEIGHT)
    xrball, yrball = yellow.x, yellow.y
    xbball, ybball = red.x, red.y

    red_bullets = []
    yellow_bullets = []
    red_hitbox = []
    blue_hitbox = []
    blue_super = []
    red_super = []
    red_health = 150
    yellow_health = 150
    MAX_SUPER = 2
    medcharger = 0
    medchargeb = 0

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                
               

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    if sou == 1:
                        BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_KP_7 and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                    red.x, red.y + red.height//2 - 2, 10,5)
                    red_bullets.append(bullet)
                    if sou == 1:
                        BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_KP_9 and len(blue_hitbox) < MAX_SUPER:
                    if super_brate >= 100:
                        hitbox_S = pygame.Rect(
                        red.x - 30, red.y + red.height//2 - 2, 30,15)
                        blue_hitbox.append(hitbox_S)
                        super_brate = 0
                        if sou == 1:
                            BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_e and len(red_hitbox) < MAX_SUPER:
                    if super_rrate >= 100:
                        hitbox_S = pygame.Rect(
                        yellow.x + yellow.width - 35, yellow.y + yellow.height//2 + 3, 30, 15)
                        red_hitbox.append(hitbox_S)
                        super_rrate = 0
                        if sou == 1:
                            BULLET_FIRE_SOUND.play()

                
                        
                    
                    


  
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()
           
            if event.type == RED_HIT:
                red_health -= 15
                if super_rrate < 76:
                    super_rrate += 25
                if sou == 1:
                    BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 15
                if super_brate < 76:
                    super_brate += 25
                if sou == 1:    
                    BULLET_HIT_SOUND.play()
            if event.type == SREDHIT:
                BVEL = 2
                blue_slowness = 100
                pygame.time.set_timer(SLOWTIMERR, 4000)
                pygame.time.set_timer(slowtimerr1, 125)

                red_health -= 45
                if super_rrate < 76:
                    super_rrate += 25
                if sou == 1:
                    BULLET_HIT_SOUND.play()

            if event.type == SBLUEHIT:
                RVEL = 2
                red_slowness = 100
                pygame.time.set_timer(SLOWTIMERB, 4000)
                pygame.time.set_timer(slowtimerb1, 125)
    
                
                yellow_health -= 45
                DE = 2
                if super_brate < 76:
                    super_brate += 25
                if sou == 1:    
                    BULLET_HIT_SOUND.play()

            if event.type == SLOWTIMERR:   
                BVEL = 5

            if event.type == SLOWTIMERB:
                RVEL = 5    

            if event.type == slowtimerb1:
                if red_slowness > 0:
                    red_slowness -= 3.125
                    

            if event.type == slowtimerr1:
                if blue_slowness > 0:
                    blue_slowness -= 3.125
                   
            
            
        
           

        winner_text = ""
        if red_health <= 0:
            winner_text = "Red Wins!"

        if yellow_health <= 0:
            winner_text = "Blue Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break
        
        if run == False:
            return
        else:
            keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, red_hitbox, blue_hitbox, yellow, red,rfire,bfire)

       

        draw_window(red, yellow, rfire, bfire, red_slowness, blue_slowness, medcharger, medchargeb, red_bullets, yellow_bullets, blue_hitbox, red_hitbox,
                    red_health, yellow_health)


    
game_intro()
main()


if __name__ == "__main__":
    main()
