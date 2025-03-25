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

        self.check_border(width, height)

        for ball in balls:
            self.check_collision(ball, width, height)

    def check_border(ball, width, height):
        if ball.x - ball.radius < 0 or ball.x + ball.radius > width:
            ball.speed_x *= -1
        if ball.y + ball.radius > height:
            ball.y = height - ball.radius
            if abs(ball.speed_y) >= 0.5:
                ball.speed_y *= -1
            else:
                ball.speed_y = 0

    def check_collision(self, other, width, height):
        if other != self:
            dx = other.x - self.x
            dy = other.y - self.y
            distance = math.sqrt(dx**2 + dy**2)

            if distance < self.radius + other.radius:
                nx = dx / distance
                ny = dy / distance

                self.speed_x, other.speed_x = other.speed_x, self.speed_x
                self.speed_y, other.speed_y = other.speed_y, self.speed_y

                overlap = self.radius + other.radius - distance
                self.x -= nx * (overlap / 2)
                self.y -= ny * (overlap / 2)
                other.x += nx * (overlap / 2)
                other.y += ny * (overlap / 2)

                other.check_border(width, height)
