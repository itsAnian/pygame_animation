import pygame
import imageio.v2 as imageio
import os
from ball import Ball
import random

pygame.init()

WIDTH, HEIGHT = 1080/2, 1920/2
FPS = 60
SECONDS = 7

BLACK = (0,0,0)

balls = []
num_balls = 30

frames = []
frame_count = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def create_tmp_folder():
    folder_name = "tmp"
    os.makedirs(folder_name, exist_ok=True)

def save_frame(frame_count):
    filename = f"./tmp/frame_{frame_count:03d}.png"
    pygame.image.save(screen, filename)
    frames.append(filename)
    return (frame_count + 1)

def create_video():
    video_writer = imageio.get_writer("animation.mp4", fps=FPS)
    for frame in frames:
        img = imageio.imread(frame)
        video_writer.append_data(img)
    video_writer.close()

def create_balls(balls, num_balls):
    for _ in range(num_balls):
        x = random.randint(50, int(WIDTH-50))
        y = random.randint(50, int(HEIGHT-50))
        speed_x = random.randint(-5, 5)
        speed_y = random.randint(-5, 5)
        radius = 20
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        balls.append(Ball(x, y, speed_x, speed_y, radius, color))

running = True

create_tmp_folder()
create_balls(balls, num_balls)

while running and frame_count < FPS*SECONDS:
    screen.fill(BLACK)

    for ball in balls:
        ball.move(WIDTH, HEIGHT, balls)
        ball.draw(screen)

    frame_count = save_frame(frame_count)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

create_video()
