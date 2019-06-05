#Pong

import pygame
import random

pygame.init()
pygame.font.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
size = (600, 400)
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont('trebuchetms', 15)
pygame.display.set_caption("Pong")
carryOn = True
clock = pygame.time.Clock()

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
LEFT = False
RIGHT = True
ball_position = [1,0]
ball_velocity = [1,0]
scoreLeft = 0
scoreRight = 0
paddle1_position = 0
paddle2_position = 0
paddle1_velocity = 0
paddle2_velocity = 0

def spawn_ball(direction):
    global ball_position, ball_velocity, RIGHT, LEFT
    x_val = 1 #random.randrange(1,3)
    y_val = 1 #random.randrange(1,3)
    ball_position[0] = WIDTH/2
    ball_position[1] = HEIGHT/2
    positions = [-10,-9,-8,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10]
    if direction == RIGHT:
        ball_velocity[0] = random.randrange(3, 8) * x_val
        ball_velocity[1] = positions[random.randrange(0, 9)] * y_val
    else:
        ball_velocity[0] = random.randrange(-8,-3) * x_val
        ball_velocity[1] = positions[random.randrange(0,9)] * y_val

def new_game():
    global RIGHT, LEFT  # these are numbers
    spawn_ball(RIGHT)

def drawLogic(screen):
    screen.fill(BLACK)
    global scoreRight, scoreLeft, paddle1_position, paddle2_position ,paddle1_velocity, paddle2_velocity, ball_position, ball_velocity, LEFT, RIGHT
    pygame.draw.circle(screen, WHITE, [int(ball_position[0]), int(ball_position[1])], 20, 0)

    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    #keep ball on the screen
    if ball_position[1] < 20:
        ball_velocity[1] *= -1
    elif ball_position[1] > 380:
        ball_velocity[1] *= -1
    if ball_position[0] < 8:
        if ball_position[1] > paddle1_position and ball_position[1] < paddle1_position + PAD_HEIGHT:
            ball_velocity[0] = -1 * ball_velocity[0]
            ball_velocity[0] += ball_velocity[0] * 0.5
        else:
            spawn_ball(RIGHT)
            scoreRight += 1
    elif ball_position[0] > 592:
        if ball_position[1] > paddle2_position and ball_position[1] < paddle2_position + PAD_HEIGHT:
            ball_velocity[0] = -1 * ball_velocity[0]
            ball_velocity[0] += ball_velocity[0] * 0.5
        else:
            spawn_ball(LEFT)
            scoreLeft += 1
    if paddle1_position + paddle1_velocity < 325 and paddle1_position + paddle1_velocity > -5:
        paddle1_position += paddle1_velocity
    if paddle2_position + paddle2_velocity < 325 and paddle2_position + paddle2_velocity > -5:
        paddle2_position += paddle2_velocity
    pygame.draw.line(screen, WHITE, [WIDTH/2, 0], [WIDTH/2, HEIGHT], 1)
    pygame.draw.line(screen, WHITE, [PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(screen, WHITE, [WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(screen, WHITE, [0, paddle1_position], [0, paddle1_position + PAD_HEIGHT], 15)
    pygame.draw.line(screen, WHITE, [600, paddle2_position], [600, paddle2_position + PAD_HEIGHT], 15)
    textsurface = myfont.render('Left score: ' + str(scoreLeft), False, WHITE)
    textsurface1 = myfont.render('Right score: ' + str(scoreRight), False, WHITE)
    screen.blit(textsurface, (30, 20))
    screen.blit(textsurface1, (330, 20))

def keydown(event):
    global paddle1_velocity, paddle2_velocity
    if event.key == pygame.K_DOWN:
        paddle2_velocity += 5
    if event.key == pygame.K_s:
        paddle1_velocity += 5
    if event.key == pygame.K_UP:
        paddle2_velocity += -5
    if event.key == pygame.K_w:
        paddle1_velocity += -5


def keyup(event):
    global paddle1_velocity, paddle2_velocity
    if event.key == pygame.K_DOWN:
        paddle2_velocity = 0
    if event.key == pygame.K_s:
        paddle1_velocity = 0
    if event.key == pygame.K_UP:
        paddle2_velocity = 0
    if event.key == pygame.K_w:
        paddle1_velocity = 0


while carryOn:
    clock.tick(60)
    drawLogic(screen)
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keydown(event)
        if event.type == pygame.KEYUP:
            keyup(event)
        # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False

    pygame.display.flip()



