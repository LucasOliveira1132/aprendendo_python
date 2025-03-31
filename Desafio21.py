import pygame 
print('='*53)
pygame.init()
pygame.mixer.music.load('desafio21.mp3.mpeg')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()
print('Caso Queria Cancelar a Musica Pressione a Tecla ENTER')
input()
#Tocando Mp3