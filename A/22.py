import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica02.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
