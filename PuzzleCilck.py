import time
from threading import Thread
import _thread

import pygame


# Define some colors
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BROWN = (165, 42, 42)

list = [0,1,2,3,4,5,6,7,8]
current_list = [2,6,5,1,8,3,0,7,4]
OG_List = [2,6,5,1,8,3,0,7,4]
current_blank = current_list[8]
OG_Blank = current_list[8]

# Defining possible movements
plus_one = 0,1,3,4,6,7
minus_one = 1,2,4,5,7,8
plus_three = 0,1,2,3,4,5
minus_three = 3,4,5,6,7,8

# Defining the coordinates
one = (50, 50)
two = (150, 50)
three = (250, 50)
four = (50, 150)
five = (150, 150)
six = (250, 150)
seven = (50, 250)
eight = (150, 250)
nine = (250, 250)

# Defining the piece and where variables
piece = 9
where=9

# Number of movements
movements = 0


# -----------------------------------------------------------------------
# Pre Game
# initialized the game engine
pygame.init()

# Import whole image preview
WholeParrot = pygame.image.load("WholeParrot.png")
WholeFlower = pygame.image.load("WholeFlower.png")
WholeFlower = pygame.transform.scale(WholeFlower, (300, 300))
WholeParrot = pygame.transform.scale(WholeParrot, (300, 300))


# Initialize font
myfont = pygame.font.SysFont("Times New Roman", 15)

# Creating Window
size = (500, 500)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
pygame.display.update()


def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface , textSurface.get_rect()

def game_intro(WholePicture, pic_Choosen):
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(WHITE)
        mouse = pygame.mouse.get_pos()

        if 150 + 100 > mouse[0] > 150 and 400 + 50 > mouse[1] > 400:
            pygame.draw.rect(screen, GREEN, (150, 400, 100, 50))
            return pic_Choosen, WholePicture
        else:
            pygame.draw.rect(screen, RED, (150, 400, 100, 50))

        if 365 + 75 > mouse[0] > 365 and 125 + 50 > mouse[1] > 125:
            pygame.draw.rect(screen, GREEN, (365, 125, 75, 50))
            WholePicture = WholeParrot
            pic_Choosen =2
        else:
            pygame.draw.rect(screen, RED, (365, 125, 75, 50))

        if 365 + 75 > mouse[0] > 365 and 225 + 50 > mouse[1] > 225:
            pygame.draw.rect(screen, GREEN, (365, 225, 75, 50))
            WholePicture = WholeFlower
            pic_Choosen =1
        else:
            pygame.draw.rect(screen, RED, (365, 225, 75, 50))


        textSurf, textRect = text_objects("---------->", myfont)
        textRect.center = ((350 + (100 / 2)), (125 + (50 / 2)))
        screen.blit(textSurf, textRect)

        textSurf, textRect = text_objects("<----------", myfont)
        textRect.center = ((350 + (100 / 2)), (225 + (50 / 2)))
        screen.blit(textSurf, textRect)

        textSurf, textRect = text_objects("Start the game", myfont)
        textRect.center = ((150 + (100 / 2)), (400 + (50 / 2)))
        screen.blit(textSurf, textRect)
        screen.blit(WholePicture, (50, 50))


        pygame.display.update()

WholePicture = WholeFlower

pic_Choosen, WholePicture = game_intro(WholePicture, pic_Choosen =1)

# -----------------------------------------------------------------------
# Methods

def check_Whole_Image():
    mouse = pygame.mouse.get_pos()
    while 275 + 125 > mouse[0] > 275 and 400 + 50 > mouse[1] > 400:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        mouse = pygame.mouse.get_pos()
        screen.blit(WholePicture, (50, 50))
        pygame.draw.rect(screen, GREEN, (275, 400, 125, 50))
        textSurf, textRect = text_objects("Back to game", myfont)
        textRect.center = ((290 + (100 / 2)), (400 + (50 / 2)))
        screen.blit(textSurf, textRect)
        pygame.display.update()

def reset(movements, current_list, current_blank):
    mouse = pygame.mouse.get_pos()
    if 375+70 >mouse[0]>375 and 200+50> mouse[1]>200:
        movements = 0
        current_list = [2,6,5,1,8,3,0,7,4]
        current_blank = OG_Blank

        showImages(screen, current_list, BROWN, flowers)


    return movements, current_list, current_blank



def drawSquare(screen, BROWN):
    # First row
    pygame.draw.rect(screen, BROWN, [50, 50, 100, 100], 2)
    pygame.draw.rect(screen, BROWN, [150, 50, 100, 100], 2)
    pygame.draw.rect(screen, BROWN, [250, 50, 100, 100], 2)

    # Second row
    pygame.draw.rect(screen, BROWN, [50, 150, 100, 100], 2)
    pygame.draw.rect(screen, BROWN, [150, 150, 100, 100], 2)
    pygame.draw.rect(screen, BROWN, [250, 150, 100, 100], 2)

    # Third row
    pygame.draw.rect(screen, BROWN, [50, 250, 100, 100], 2)
    pygame.draw.rect(screen, BROWN, [150, 250, 100, 100], 2)
    pygame.draw.rect(screen, BROWN, [250, 250, 100, 100], 2)


def set_Images(screen, pic_Choosen):
    # Import Images
    # fuck = input("what the fuch u want")
    # fuck = int(fuck)
    if pic_Choosen ==1:
        flower0 = pygame.image.load("Flower#0.png")
        flower1 = pygame.image.load("Flower#1.png")
        flower2 = pygame.image.load("Flower#2.png")
        flower3 = pygame.image.load("Flower#3.png")
        flower4 = pygame.image.load("Flower#4.png")
        flower5 = pygame.image.load("Flower#5.png")
        flower6 = pygame.image.load("Flower#6.png")
        flower7 = pygame.image.load("Flower#7.png")
        flower8 = pygame.image.load("Blank.png")
    elif pic_Choosen ==2:
        flower0 = pygame.image.load("Parrot#0.png")
        flower1 = pygame.image.load("Parrot#1.png")
        flower2 = pygame.image.load("Parrot#2.png")
        flower3 = pygame.image.load("Parrot#3.png")
        flower4 = pygame.image.load("Parrot#4.png")
        flower5 = pygame.image.load("Parrot#5.png")
        flower6 = pygame.image.load("Parrot#6.png")
        flower7 = pygame.image.load("Parrot#7.png")
        flower8 = pygame.image.load("Blank.png")

    flower0 = pygame.transform.scale(flower0, (100, 100))
    flower1 = pygame.transform.scale(flower1, (100, 100))
    flower2 = pygame.transform.scale(flower2, (100, 100))
    flower3 = pygame.transform.scale(flower3, (100, 100))
    flower4 = pygame.transform.scale(flower4, (100, 100))
    flower5 = pygame.transform.scale(flower5, (100, 100))
    flower6 = pygame.transform.scale(flower6, (100, 100))
    flower7 = pygame.transform.scale(flower7, (100, 100))
    flower8 = pygame.transform.scale(flower8, (100, 100))


    flowers = [flower0, flower1, flower2, flower3, flower4, flower5, flower6, flower7, flower8]

    return flowers

def showImages(screen,current_list, BROWN, flowers):
    screen.fill(WHITE)

    screen.blit(flowers[current_list[0]], one)

    screen.blit(flowers[current_list[1]], two)

    screen.blit(flowers[current_list[2]], three)

    screen.blit(flowers[current_list[3]], four)

    screen.blit(flowers[current_list[4]], five)

    screen.blit(flowers[current_list[5]], six)

    screen.blit(flowers[current_list[6]], seven)

    screen.blit(flowers[current_list[7]], eight)

    screen.blit(flowers[current_list[8]], nine)


    pygame.draw.rect(screen, BROWN, (80, 400, 75, 50))
    textSurf, textRect = text_objects("Moves: " +(str(movements)), myfont)
    textRect.center = ((65 + (100 / 2)), (400 + (50 / 2)))
    screen.blit(textSurf, textRect)

    textSurf, textRect = text_objects("Reset", myfont)
    textRect.center = ((360 + (100 / 2)), (200 + (50 / 2)))
    pygame.draw.rect(screen, RED, (375, 200, 70, 50))
    screen.blit(textSurf, textRect)

    textSurf, textRect = text_objects("Show Whole Image", myfont)
    textRect.center = ((290 + (100 / 2)), (400 + (50 / 2)))
    pygame.draw.rect(screen, RED, (275, 400, 125, 50))
    screen.blit(textSurf, textRect)

    drawSquare(screen, BROWN)
    pygame.display.update()


# Set up method
def setUp():


    # Set screen
    screen.fill(WHITE)

    flowers = set_Images(screen, pic_Choosen)
    showImages(screen, current_list, BROWN, flowers)
    pygame.display.update()

    return screen, flowers


# Start the Set-Up
screen, flowers = setUp()

def get_Coord(posX, posY):
    if posY<150:
        if posX<150:
            pos = 0
            return pos
        elif posX>150 and posX<250:
            pos = 1
            return pos
        elif posX>250 and posX<350:
            pos = 2
            return pos
    elif posY<250 and posY>150:
        if posX<150:
            pos = 3
            return pos
        elif posX>150 and posX<250:
            pos = 4
            return pos
        elif posX>250 and posX<350:
            pos = 5
            return pos
    elif posY<350 and posY>250:
        if posX<150:
            pos = 6
            return pos
        elif posX>150 and posX<250:
            pos = 7
            return pos
        elif posX>250 and posX<350:
            pos = 8
            return pos
    return 9


#----------------------------------------------------------------------------
# Getting the input from user and calling the methods above
start = time.time()
while True:
    for event in pygame.event.get():
        check_Whole_Image()
        movements, current_list, current_blank = reset(movements, current_list, current_blank)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pieceX, pieceY = event.pos
            piece = int(get_Coord(pieceX, pieceY))

        elif event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
            whereX, whereY = event.pos
            where = int(get_Coord(whereX, whereY))

        elif event.type == pygame.QUIT:
            quit()


    if piece in plus_one and piece + 1 == where and where == current_blank :
        movements += 1
        current_list[piece], current_list[where] = current_list[where], current_list[piece]
        current_blank = piece
        #showImages(screen, current_list, BROWN, flowers)

    if piece in minus_one and piece - 1 == where and where == current_blank:
        movements += 1
        current_list[piece], current_list[where] = current_list[where], current_list[piece]
        current_blank = piece
        #showImages(screen, current_list, BROWN, flowers)

    if piece in plus_three and piece + 3 == where and where == current_blank:
        movements += 1
        current_list[piece], current_list[where] = current_list[where], current_list[piece]
        current_blank = piece
        #showImages(screen, current_list, BROWN, flowers)

    if piece in minus_three and piece - 3 == where and where == current_blank:
        movements += 1
        current_list[piece], current_list[where] = current_list[where], current_list[piece]
        current_blank = piece
    showImages(screen, current_list, BROWN, flowers)
