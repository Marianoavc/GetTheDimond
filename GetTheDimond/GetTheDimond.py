import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
ANCHO_VENTANA = 400
ALTO_VENTANA = 400

# Definir colores
BLANCO = (255, 255, 255)
AZUL_CLARO = (0, 191, 255)

# Cargar imágenes
imagen_bomba = pygame.image.load("GetTheDimond/images/bomba.png")  # Ruta de la imagen de la bomba
imagen_diamante = pygame.image.load("GetTheDimond/images/diamante.png")  # Ruta de la imagen del diamante

# Calcular tamaño y separación de los cuadrados
TAMANO_CUADRADO = 80
ESPACIO_ENTRE_CUADRADOS = 20

# Función para crear lista de cuadrados
def crear_cuadrados():
    cuadrados = []
    for fila in range(4):
        for columna in range(4):
            x = columna * (TAMANO_CUADRADO + ESPACIO_ENTRE_CUADRADOS)
            y = fila * (TAMANO_CUADRADO + ESPACIO_ENTRE_CUADRADOS)
            cuadrados.append(pygame.Rect(x, y, TAMANO_CUADRADO, TAMANO_CUADRADO))
    return cuadrados

# Función principal del juego
def juego():
    # Crear ventana
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Juego de Clics")

    # Crear cuadrados
    cuadrados = crear_cuadrados()

    # Colocar bombas en cuadrados aleatorios
    bombas = random.sample(cuadrados, 3)

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
                for i, cuadrado in enumerate(cuadrados):
                    if cuadrado.collidepoint(evento.pos):
                        if cuadrado in bombas:
                            # Mostrar imagen de la bomba en el cuadrado
                            mostrar_imagenes[i] = imagen_bomba
                            bomba_encontrada = True
                        else:
                            # Mostrar imagen del diamante en el cuadrado
                            mostrar_imagenes[i] = imagen_diamante

        ventana.fill(BLANCO)  # Rellenar ventana con color blanco

        # Dibujar los cuadrados y mostrar las imágenes correspondientes
        for cuadrado, imagen in zip(cuadrados, mostrar_imagenes):
            pygame.draw.rect(ventana, AZUL_CLARO, cuadrado)
            if imagen:
                ventana.blit(imagen, cuadrado.topleft)

        pygame.display.update()  # Actualizar ventana

        # Verificar si se encontró una bomba
        if bomba_encontrada:
            # Mostrar mensaje de "perdiste"
            fuente = pygame.font.Font(None, 36)
            texto = fuente.render("¡Perdiste!", True, (255, 0, 0))
            texto_rect = texto.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))
            ventana.blit(texto, texto_rect)
            pygame.display.update()

            # Pausar el juego durante 3 segundos
            pygame.time.delay(3000)
            jugando = False

    # Salir del juego
    pygame.quit()


# Ejecutar juego
juego()
