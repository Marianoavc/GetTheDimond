import pygame
import random
from pygame.locals import *

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

# Definir colores
NEGRO = (0, 0, 0)
AZUL_CLARO = (0, 191, 255)

# Calcular tamaño y separación de los cuadrados
TAMANO_CUADRADO = 80
ESPACIO_ENTRE_CUADRADOS = 20

# Función para crear lista de cuadrados
def crear_cuadrados():
    cuadrados = []
    for fila in range(5):
        for columna in range(5):
            x = columna * (TAMANO_CUADRADO + ESPACIO_ENTRE_CUADRADOS) + 20
            y = fila * (TAMANO_CUADRADO + ESPACIO_ENTRE_CUADRADOS) + 100
            cuadrados.append(pygame.Rect(x, y, TAMANO_CUADRADO, TAMANO_CUADRADO))
    return cuadrados

#variables constantes
cartera = 100
numBombas = 3
montoApuesta = 0

#actualizan debe estar en el loop
enJuego = 0
multiplicador = 1

# Función para retirarse del juego
def retirarse():
    global enJuego
    enJuego = 0
    # Otras acciones relacionadas con retirarse del juego
    # ...

# Función para realizar una apuesta
def apostar():
    global enJuego
    enJuego = 1
    # Otras acciones relacionadas con realizar una apuesta
    # ...

# Función principal del juego
def juego():
    # Crear ventana
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("GET THE DIMOND")

    # Crear cuadrados
    cuadrados = crear_cuadrados()

    # Colocar bombas en cuadrados aleatorios
    bombas = random.sample(cuadrados, numBombas)

    # Cargar imágenes
    imagen_bomba = pygame.image.load("imagesGTD/bomba.png")  # Ruta de la imagen de la bomba
    imagen_diamante = pygame.image.load("imagesGTD/diamante.png")  # Ruta de la imagen del diamante

    # Redimensionar imágenes para que se ajusten al tamaño de los cuadrados
    imagen_bomba = pygame.transform.scale(imagen_bomba, (TAMANO_CUADRADO, TAMANO_CUADRADO))
    imagen_diamante = pygame.transform.scale(imagen_diamante, (TAMANO_CUADRADO, TAMANO_CUADRADO))

    # Inicializar lista de imágenes a mostrar en cada cuadro
    mostrar_imagenes = [None] * len(cuadrados)

    # Variables del juego
    jugando = True
    bomba_encontrada = False

    # Bucle principal del juego
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            elif evento.type == pygame.MOUSEBUTTONUP:
                if boton_retirarse.collidepoint(evento.pos):
                    retirarse()  # Llamar a la función 'retirarse' al hacer clic en el botón "Retirarse"
                elif boton_apostar.collidepoint(evento.pos):
                    apostar()  # Llamar a la función 'apostar' al hacer clic en el botón "Apostar"
                else:
                    for i, cuadrado in enumerate(cuadrados):
                        if cuadrado.collidepoint(evento.pos):
                            if cuadrado in bombas:
                                # Mostrar imagen de la bomba en el cuadrado
                                mostrar_imagenes[i] = imagen_bomba
                                bomba_encontrada = True
                            else:
                                # Mostrar imagen del diamante en el cuadrado
                                mostrar_imagenes[i] = imagen_diamante

        ventana.fill(NEGRO)  # Rellenar ventana con color negro

        # Dibujar cuadrados y mostrar las imágenes correspondientes
        for cuadrado, imagen in zip(cuadrados, mostrar_imagenes):
            pygame.draw.rect(ventana, AZUL_CLARO, cuadrado)
            if imagen:
                ventana.blit(imagen, cuadrado.topleft)

        # Dibujar botones
        boton_retirarse = pygame.Rect(ANCHO_VENTANA - 250, ALTO_VENTANA - 150, 100, 40)  # Botón "Retirarse"
        boton_apostar = pygame.Rect(ANCHO_VENTANA - 140, ALTO_VENTANA - 150, 100, 40)  # Botón "Apostar"

        pygame.draw.rect(ventana, (0, 255, 0), boton_retirarse)  # Botón "Retirarse" en color verde
        pygame.draw.rect(ventana, (255, 0, 0), boton_apostar)  # Botón "Apostar" en color rojo

        fuente = pygame.font.Font(None, 20)  # Fuente para el texto de los botones
        texto_retirarse = fuente.render("Retirarse", True, (255, 255, 255))  # Texto para el botón "Retirarse"
        texto_apostar = fuente.render("Apostar", True, (255, 255, 255))  # Texto para el botón "Apostar"

        ventana.blit(texto_retirarse, (boton_retirarse.x + 10, boton_retirarse.y + 10))  # Mostrar el texto del botón "Retirarse"
        ventana.blit(texto_apostar, (boton_apostar.x + 10, boton_apostar.y + 10))  # Mostrar el texto del botón "Apostar"

        pygame.display.update()  # Actualizar ventana

        # Verificar si se encontró una bomba
        if bomba_encontrada:
            # Mostrar mensaje de "perdiste"
            fuente = pygame.font.Font(None, 36)
            texto = fuente.render("¡Perdiste!", True, (255, 0, 0))
            texto_rect = texto.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))
            ventana.blit(texto, texto_rect)
            pygame.display.update()

            # Pausar el juego durante 1 segundo
            pygame.time.delay(1000)
            jugando = False

    # Salir del juego
    pygame.quit()

# Ejecutar juego
juego()
