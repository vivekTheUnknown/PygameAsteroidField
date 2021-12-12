import pygame, sys, random
from GameEntities import Player
from GameEntities import Bullet
from GameEntities import Enemies

pygame.init()
SCREEN_SIZE = width, height = 800, 600
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
BACKGROUND_FILL = 255, 255, 255
GAME_STATE = True
PLAYER_Y_AXIS_POS = Player.player_y_pos(height)
PLAYER_X_AXIS_POS = Player.player_x_pos(width)
PLAYER_RECT = pygame.Rect(PLAYER_X_AXIS_POS, PLAYER_Y_AXIS_POS, 60, 60)
PLAYER_SPEED = 10
BULLET1_ENTITY_LIST = []
BULLET2_ENTITY_LIST = []
ENEMY_ENTITY_LIST = []
CLOCK = pygame.time.Clock()
pygame.display.set_caption("ASTEROID FIELD!")

while GAME_STATE:
######################################################################################
    #INITALIZATION
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    
    SCREEN.fill(BACKGROUND_FILL)
    pygame.draw.rect(SCREEN, (100, 231, 79), PLAYER_RECT)
    input_keys = pygame.key.get_pressed()
    X_POS_VEL = input_keys[pygame.K_LEFT]
    X_NEG_VEL = input_keys[pygame.K_RIGHT]
    PLAYER_RECT.x += (X_NEG_VEL - X_POS_VEL) * PLAYER_SPEED
######################################################################################
    #BULLET_LOGIC
    if input_keys[pygame.K_SPACE]:
      bullet_rect_1 = Bullet().spawn_coordinates_set_1(PLAYER_RECT.x, PLAYER_Y_AXIS_POS)
      bullet_rect_2 = Bullet().spawn_coordinates_set_2(PLAYER_RECT.x, PLAYER_Y_AXIS_POS)

      if len(BULLET1_ENTITY_LIST) == 0:
          BULLET1_ENTITY_LIST.append(bullet_rect_1)
      else:
          if bullet_rect_1.y - BULLET1_ENTITY_LIST[-1].y >= 35:
              BULLET1_ENTITY_LIST.append(bullet_rect_1)

      if len(BULLET2_ENTITY_LIST) == 0:
          BULLET2_ENTITY_LIST.append(bullet_rect_2)
      else:
          if bullet_rect_2.y - BULLET2_ENTITY_LIST[-1].y >= 35:
              BULLET2_ENTITY_LIST.append(bullet_rect_2)
    
    for i in BULLET1_ENTITY_LIST:
        pygame.draw.rect(SCREEN, Bullet().BULLET_GRAPHICS, i) 
        i.y -= Bullet().BULLET_VEL
        if i.y < -25:
            BULLET1_ENTITY_LIST.remove(i)
    
    for j in BULLET2_ENTITY_LIST:
        pygame.draw.rect(SCREEN, Bullet().BULLET_GRAPHICS, j) 
        j.y -= Bullet().BULLET_VEL
        if j.y < -25:
            BULLET2_ENTITY_LIST.remove(j)

######################################################################################
    #ENEMY LOGIC
    ENEMY_RECT = Enemies.enemy_spawn(width)
    if len(ENEMY_ENTITY_LIST) == 0:
        ENEMY_ENTITY_LIST.append(ENEMY_RECT)
    else:
        if ENEMY_RECT.y - ENEMY_ENTITY_LIST[-1].y <= -50:
            ENEMY_ENTITY_LIST.append(ENEMY_RECT)
    for k in ENEMY_ENTITY_LIST:
        pygame.draw.rect(SCREEN, Enemies().ENEMY_GRAPHICS, k)
        k.y += Enemies().ENEMY_VEL
        if k.y > PLAYER_Y_AXIS_POS + 35:
            ENEMY_ENTITY_LIST.remove(k)
######################################################################################
    #COLLISION LOGIC
    for l in ENEMY_ENTITY_LIST:
        for m in BULLET1_ENTITY_LIST:
            if l.colliderect(m):
                ENEMY_ENTITY_LIST.remove(l)
                BULLET1_ENTITY_LIST.remove(m)
        
        for n in BULLET2_ENTITY_LIST:
            if l.colliderect(n):
                ENEMY_ENTITY_LIST.remove(l)
                BULLET2_ENTITY_LIST.remove(n)
    
    PLAYER_RECT.clamp_ip(pygame.display.get_surface().get_rect())
    pygame.display.flip()