import sys
import pygame

#
# Little piece of black magic to ensure no lag
# occurs when playing sound. Must be done before
# pygame.init
#
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()

movement = [1, 1]
speed = 1
background_colour = pygame.Color("black")
mrbing = pygame.image.load("mrbing.png")
ding = pygame.mixer.Sound("ding.wav")

size = width, height = 300, 200
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mr Bing is Great")

location = mrbing.get_rect()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    location = location.move([speed * distance for distance in movement])
    if location.left < 0 or location.right > width:
        ding.play()
        movement[0] = -movement[0]
    if location.top < 0 or location.bottom > height:
        ding.play()
        movement[1] = -movement[1]

    screen.fill(background_colour)
    screen.blit(mrbing, location)
    pygame.display.flip()
    clock.tick(60)
