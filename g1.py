import pygame
from pygame.locals import *
from random import randint
def colisao(c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def direct(k):

    if k  == K_UP:
        d = 0
    if k == K_DOWN:
        d = 1
    if k == K_RIGHT:
       d = 3
    if k == K_LEFT:
        d = 2
    return (d)



score = 0
up = 0
down = 1
left = 2
right = 3
start = 0
x = 500
y = 400
pygame.init()
screen = pygame.display.set_mode((520,400))
pygame.display.set_caption("Snakepy")
run = True
background_img = pygame.image.load('background.bmp').convert()
game_over = pygame.image.load('gameover.bmp').convert()
start_img = pygame.image.load('start_scr.bmp').convert()
font_name = pygame.font.match_font('System',3)
font  = pygame.font.Font(font_name, 30)

snake = [(260,200),
         (270,200),
         (280,200)]
skin = pygame.Surface((10,10))
skin.fill((15,107,21))
food = pygame.Surface((10,10))
p_food = (((randint(30,500))//10)*10,(((randint(30,380)//10)*10)))
food.fill((255,0,0))

clock = pygame.time.Clock()
k = 1
pygame.event.wait()
screen.blit(start_img, [0, 0])
while run:

    clock.tick(20)
    score_surface = font.render('SCORE:  %d' %score, True, (233, 233, 233))
    if k == 1:
        pygame.event.clear()
        screen.blit(start_img, [0, 0])
        pygame.display.flip()
        pygame.time.wait(500)
        pygame.event.wait()
        dir = left
        k = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == KEYDOWN:
            dir = direct(event.key)





    if dir == up:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    elif dir == down:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    elif dir == left:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    elif dir == right:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    elif dir == 8:
        screen.fill((0,0,0))
        screen.blit(game_over, [0,0])
        pygame.display.flip()
        pygame.time.wait(8000)
        print('GAME OVER')


    for i in range(len(snake)-1,0,-1):
        snake[i] = (snake[i-1][0],snake[i-1][1])

    screen.blit(background_img, [0,0])

    if snake[0][0] >= x  or snake[0][1] > y:
        dir = 8
    if  snake[0][0] <= 10  or snake[0][1] >= y:
        dir = 8
    if snake[0][0] >= x or snake[0][1] <= 10:
        dir = 8
    if snake[0][0] <= 10  or snake[0][1] <= 10:
        dir = 8
    if snake[0][0] <= x and snake[0][1] == y-20:
        dir = 8

    screen.blit(food,p_food)

    if colisao(snake[0], p_food):
        p_food = (((randint(30,490))//10)*10,(((randint(30,370)//10)*10)))
        score = score + 1
        snake.append((0,0))
    #BORDAS
    pygame.draw.rect(screen, (32, 32, 32), ((0, 0), (520, 400)), 25)
    pygame.draw.rect(screen, (153, 153, 0), ((0, 0), (520, 400)), 5)
    screen.blit(score_surface,[30,30])

    for i in range(len(snake)):
         if i > 4:
            if snake[0] == snake[i]:
                dir = 8





    for pos in snake:
        #print(pos)
        screen.blit(skin, pos)
    pygame.display.update()