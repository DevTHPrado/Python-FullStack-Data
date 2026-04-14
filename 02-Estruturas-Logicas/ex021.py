#Faça um programa em Python que abra e reproduza o audio de arquivo MP3

# Para salvar um mp3, entre em y2mate no google e coloque o link do video la
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

# Guanabara ensinou assim, porem não funcionou no meu!
# Pesquisei no ChatGPT e faltou um input

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()