import pygame
import os
from pygame.locals import *
import random

class CuadradoPrincipal:
    def __init__(self, x, y, ancho, alto, filas, columnas):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.filas = filas
        self.columnas = columnas
        self.tamano_celda = ancho // columnas
        self.columna_vacia = columnas - 1  
        self.imagenes = []
        self.movimientos = 0
        self.cargar_imagenes()
        
    def cargar_imagenes(self):
        carpeta_imagenes = "numeros" 
        nombres_archivos = os.listdir(carpeta_imagenes)
        random.shuffle(nombres_archivos)  
        for nombre_archivo in nombres_archivos[:8]: 
            if nombre_archivo.endswith((".jpg", ".png")):
                ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)
                imagen = pygame.image.load(ruta_imagen)
                imagen = pygame.transform.scale(imagen, (self.tamano_celda, self.tamano_celda))
                self.imagenes.append(imagen)

        self.imagenes.insert(self.columna_vacia, pygame.Surface((self.tamano_celda, self.tamano_celda)))

    def mover_izquierda(self):
        fila, columna = self.obtener_posicion_vacia()
        if columna > 0:
            self.intercambiar_imagenes(fila, columna, fila, columna - 1)
            self.movimientos += 1
    
    def mover_derecha(self):
        fila, columna = self.obtener_posicion_vacia()
        if columna < self.columnas - 1:
            self.intercambiar_imagenes(fila, columna, fila, columna + 1)
            self.movimientos += 1

    def mover_arriba(self):
        fila, columna = self.obtener_posicion_vacia()
        if fila > 0:
            self.intercambiar_imagenes(fila, columna, fila - 1, columna)
            self.movimientos += 1

    def mover_abajo(self):
        fila, columna = self.obtener_posicion_vacia()
        if fila < self.filas - 1:
            self.intercambiar_imagenes(fila, columna, fila + 1, columna)
            self.movimientos += 1

    def obtener_posicion_vacia(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if self.imagenes[fila][columna] is None:
                    return fila, columna

    def intercambiar_imagenes(self, fila1, columna1, fila2, columna2):
        self.imagenes[fila1][columna1], self.imagenes[fila2][columna2] = self.imagenes[fila2][columna2], self.imagenes[fila1][columna1]

def dibujar_cuadrado(screen, cuadrado):
    pygame.draw.rect(screen, (255, 255, 255), (cuadrado.x, cuadrado.y, cuadrado.ancho, cuadrado.alto))


    for fila in range(cuadrado.filas + 1):
        y = cuadrado.y + fila * cuadrado.tamano_celda
        pygame.draw.line(screen, (150, 150, 150), (cuadrado.x, y), (cuadrado.x + cuadrado.ancho, y), 1)
    for columna in range(cuadrado.columnas + 1):
        x = cuadrado.x + columna * cuadrado.tamano_celda
        pygame.draw.line(screen, (150, 150, 150), (x, cuadrado.y), (x, cuadrado.y + cuadrado.alto), 1)


    for i, imagen in enumerate(cuadrado.imagenes):
        if i != cuadrado.columna_vacia:
            x = cuadrado.x + i * cuadrado.tamano_celda
            y = cuadrado.y
            screen.blit(imagen, (x, y))