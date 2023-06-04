import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
ANCHO_VENTANA = 800
ALTO_VENTANA = 400

# Definir colores
BLANCO = (255, 255, 255)
AZUL_CLARO = (0, 191, 255)
COLOR_CONFIG = (200, 200, 200)  # Color tenue para la ventana de configuraciones

# Calcular tamaño y separación de los cuadrados
TAMANO_CUADRADO = 80
ESPACIO_ENTRE_CUADRADOS = 20

# Definir dimensiones de la ventana de configuraciones
ANCHO_CONFIG = 200
ALTO_CONFIG = ALTO_VENTANA

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
    pygame.display.set_caption("GET THE DIMOND")

    # Crear cuadrados
    cuadrados = crear_cuadrados()

    # Definir número de bombas
    num_bombas = 1  # Valor predeterminado

    # Cargar imágenes
    imagen_bomba = pygame.image.load("imagesGTD/bomba.png")  # Ruta de la imagen de la bomba
    imagen_diamante = pygame.image.load("imagesGTD/diamante.png")  # Ruta de la imagen del diamante

    # Redimensionar imágenes para que se ajusten al tamaño de los cuadrados
    imagen_bomba = pygame.transform.scale(imagen_bomba, (TAMANO_CUADRADO, TAMANO_CUADRADO))
    imagen_diamante = pygame.transform.scale(imagen_diamante, (TAMANO_CUADRADO, TAMANO_CUADRADO))

    # Inicializar lista de imágenes a mostrar en cada cuadro
    mostrar_cuadrado = [False] * len(cuadrados)

    # Variables del juego
    jugando = True
    bomba_encontrada = False

    # Crear ventana de configuraciones
    config_rect = pygame.Rect(ANCHO_VENTANA - ANCHO_CONFIG, 0, ANCHO_CONFIG, ALTO_CONFIG)

    # Bucle principal del juego
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            elif evento.type == pygame.MOUSEBUTTONUP:
                if config_rect.collidepoint(evento.pos):
                    # Clic en la ventana de configuraciones
                    if evento.button == 1:
                        # Botón izquierdo del ratón
                        if evento.pos[0] > ANCHO_VENTANA - ANCHO_CONFIG + 20 and evento.pos[1] > 40 and evento.pos[1] < 80:
                            # Clic en el área de configuración de número de bombas
                            valor_nuevo = pygame_input_dialog("Configuración", "Ingrese el número de bombas:")
                            try:
                                num_bombas = int(valor_nuevo)
                                bombas = random.sample(cuadrados, num_bombas)
                            except ValueError:
                                pass
            else:
                for i, cuadrado in enumerate(cuadrados):
                    if cuadrado.collidepoint(evento.pos):
                        if cuadrado in bombas:
                            mostrar_cuadrado[i] = imagen_bomba
                            bomba_encontrada = True
                        else:
                            mostrar_cuadrado[i] = imagen_diamante

        ventana.fill(BLANCO)  # Rellenar ventana con color blanco

        # Dibujar cuadrados y mostrar las imágenes correspondientes
        for i, cuadrado in enumerate(cuadrados):
            pygame.draw.rect(ventana, AZUL_CLARO, cuadrado)
            if mostrar_cuadrado[i]:
                ventana.blit(mostrar_cuadrado[i], cuadrado.topleft)

        # Dibujar ventana de configuraciones
        pygame.draw.rect(ventana, COLOR_CONFIG, config_rect)

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

# Función para mostrar un cuadro de diálogo de entrada
def pygame_input_dialog(titulo, mensaje):
    valor = ""
    entrada_activa = True

    while entrada_activa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return valor
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    entrada_activa = False
                elif event.key == pygame.K_BACKSPACE:
                    valor = valor[:-1]
                else:
                    valor += event.unicode

        ventana.fill(BLANCO)
        fuente = pygame.font.Font(None, 36)
        texto_titulo = fuente.render(titulo, True, (0, 0, 0))
        texto_titulo_rect = texto_titulo.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2 - 50))
        ventana.blit(texto_titulo, texto_titulo_rect)

        texto_mensaje = fuente.render(mensaje, True, (0, 0, 0))
        texto_mensaje_rect = texto_mensaje.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))
        ventana.blit(texto_mensaje, texto_mensaje_rect)

        texto_valor = fuente.render(valor, True, (0, 0, 0))
        texto_valor_rect = texto_valor.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 50))
        ventana.blit(texto_valor, texto_valor_rect)

        pygame.display.update()

    return valor

# Ejecutar juego
juego()
