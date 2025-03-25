import pygame
import random
import math

class Ball:
    def __init__(self, x, y, speed_x, speed_y, radius, color):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
        self.color = color
        self.gravity = 0.7
        self.friction = 0.99

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self, width, height, balls):
        self.speed_y += self.gravity

        self.x += self.speed_x
        self.y += self.speed_y

        self.speed_x *= self.friction
        self.speed_y *= self.friction

        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.speed_x *= -1
        if self.y + self.radius > height:
            self.y = height - self.radius
            if abs(self.speed_y) >= 0.5:
                self.speed_y *= -1
            else:
                self.speed_y = 0
