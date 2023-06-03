import numpy as np
import matplotlib.pyplot as plt

# Definimos la resolución de la imagen y el rango de valores para c
resolution = 500
x_min, x_max = -2, 1
y_min, y_max = -1.5, 1.5

# Creamos una cuadrícula de valores para c y z
x_vals = np.linspace(x_min, x_max, resolution)
y_vals = np.linspace(y_min, y_max, resolution)
xx, yy = np.meshgrid(x_vals, y_vals)
c = xx + 1j*yy
z = np.zeros_like(c)

# Iteramos la fórmula z = z^2 + c para cada punto c
for i in range(100):
    z = z**2 + c

# Calculamos una máscara booleana para separar los puntos dentro y fuera del conjunto de Mandelbrot
mask = np.abs(z) < 2

# Graficamos la máscara como una imagen en tonos de verde orientada verticalmente
fig = plt.figure(figsize=(6, 8))
plt.imshow(mask, cmap='Greens', aspect='auto', extent=[-2, 1, -1.5, 1.5])
plt.title('Conjunto de Mandelbrot')
plt.show()
