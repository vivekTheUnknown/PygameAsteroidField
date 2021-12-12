import pygame
import random

class Player:
    @staticmethod
    def player_y_pos(screen_height):
        return screen_height - 150
    
    @staticmethod
    def player_x_pos(screen_width):
        return (screen_width/2)

class Bullet:
    BULLET_VEL = 1
    BULLET_GRAPHICS = 121, 25, 221

    @staticmethod
    def spawn_coordinates_set_1(player_x, player_y):
        return pygame.Rect(player_x, player_y, 10, 10)
    
    @staticmethod
    def spawn_coordinates_set_2(player_x, player_y):
        return pygame.Rect(player_x + 50, player_y, 10, 10)

class Enemies:
    ENEMY_GRAPHICS = 122,0,98
    ENEMY_VEL = 1

    @staticmethod
    def enemy_spawn(screen_width):
        return pygame.Rect(random.randint(0, screen_width - 35), -35, 35, 35)