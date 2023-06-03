import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
AZUL_CLARO = (0, 191, 255)


# Definir dimensiones de la ventana
ANCHO_VENTANA = 400
ALTO_VENTANA = 400

# Definir tamaño de los cuadrados
ANCHO_CUADRADO = 50
ALTO_CUADRADO = 50

# Crear ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Juego de Clics")

# Definir fuente
fuente = pygame.font.Font(None, 36)

# Función para mostrar mensaje
def mostrar_mensaje(texto):
    mensaje = fuente.render(texto, True, NEGRO)
    posicion_mensaje = mensaje.get_rect(center=(ANCHO_VENTANA/2, ALTO_VENTANA/2))
    ventana.blit(mensaje, posicion_mensaje)

# Función para dibujar cuadrados
def dibujar_cuadrados(cuadrados, bombas):
    for cuadrado in cuadrados:
        if cuadrado in bombas:
            pygame.draw.rect(ventana, NEGRO, cuadrado)
        else:
            pygame.draw.rect(ventana, AZUL_CLARO, cuadrado)

# Función para crear lista de cuadrados
def crear_cuadrados():
    cuadrados = []
    for fila in range(4):
        for columna in range(4):
            x = columna * ANCHO_CUADRADO
            y = fila * ALTO_CUADRADO
            cuadrado = pygame.Rect(x, y, ANCHO_CUADRADO, ALTO_CUADRADO)
            cuadrados.append(cuadrado)
    return cuadrados

# Función para actualizar ventana
def actualizar_ventana(cuadrados, bombas):
    ventana.fill(NEGRO)
    dibujar_cuadrados(cuadrados, bombas)
    pygame.display.update()


# Función principal del juego
def juego():
    cuadrados = crear_cuadrados()
    bombas = random.sample(cuadrados, 3)
    jugando = True
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            elif evento.type == pygame.MOUSEBUTTONUP:
                for cuadrado in cuadrados:
                    if cuadrado.collidepoint(evento.pos):
                        if cuadrado in bombas:
                            mostrar_mensaje("Perdiste!")
                            pygame.display.update()
                            pygame.time.delay(2000)
                            jugando = False
                            break
                        else:
                            cuadrados.remove(cuadrado)
                            if len(cuadrados) == 3:
                                mostrar_mensaje("Ganaste!")
                                pygame.display.update()
                                pygame.time.delay(2000)
                                jugando = False
                            else:
                                actualizar_ventana(cuadrados, bombas)
                                break

    # Salir del juego
    pygame.quit()


# Ejecutar juego
juego()
