import pygame
from pygame.locals import *
import sys 
import random
from Cuadros import CuadradoPrincipal , dibujar_cuadrado

background_image = pygame.image.load("IMAGENES/MAGIC PUZZLE.png")

size = width, height = 900, 900
movimientos = 0  

def main():
    pygame.init()
    screen = pygame.display.set_mode((900,900))
    background_image = pygame.image.load("IMAGENES/MAGIC PUZZLE.png")
    background_rect = background_image.get_rect()
    running = True
    while running:
        screen.blit(background_image,background_rect)
        pygame.display.flip()

        global movimientos 

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                main_game_loop()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimientos += 1
            elif event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()
    sys.exit()


def show_win(screen):
    font = pygame.font.Font(None,100)
    game_win_text = font.render("Ganaste", True, (255,0,0))
    text_rect = game_win_text.get_rect(center=(width // 2, height // 2))
    screen.blit = (game_win_text,text_rect)
    pygame.display.flip

def main_game_loop():
    global movimientos
    
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("SONIDOS/fondosonic.mp3")
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(1)

    size = width, height = 1500, 900
    screen = pygame.display.set_mode(size)
    background_image = pygame.image.load("IMAGENES/Fondo.jpg")
    background_rect = background_image.get_rect()
    pygame.display.set_caption("MAGIC PUZZLE")

    cuadrado = CuadradoPrincipal(100, 100, 300, 300, 3, 3)

    running = True
    while running:
        screen.blit(background_image, background_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cuadrado.mover_izquierda()
                elif event.key == pygame.K_RIGHT:
                    cuadrado.mover_derecha()
                elif event.key == pygame.K_UP:
                    cuadrado.mover_arriba()
                elif event.key == pygame.K_DOWN:
                    cuadrado.mover_abajo()

        dibujar_cuadrado(screen, cuadrado)

        font = pygame.font.SysFont(None, 30)
        texto = font.render(f"Movimientos: {cuadrado.movimientos}", True, (0, 0, 0))
        screen.blit(texto, (20,20))

        if cuadrado.imagenes[:-1] == sorted(cuadrado.imagenes[:-1]):
            font_win = pygame.font.SysFont(None, 100)
            texto_win = font_win.render("Ganaste!", True, (255, 0, 0))
            screen.blit(texto_win, (width // 2 - texto_win.get_width() // 2, height // 2 - texto_win.get_height() // 2))

        pygame.display.flip()

    pygame.quit()
    sys.exit()
main_game_loop()
