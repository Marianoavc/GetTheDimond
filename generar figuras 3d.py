import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import math

def ModeladoPrisma(alto,ladosprisma,longL):
    #primer parametro es el punto inicial , el segundo el final y el 
    # tercero el numero de punto que se ubicaran entre el primer y segundo
    theta = np.linspace(0, 2*np.pi, ladosprisma+1)

    z = np.linspace(0, alto, 2)
    
    #cambia los valores de arreglo entregado a 1 y lo retorna

    r = np.ones_like(theta) * longL

    # Crear la figura y el eje 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Crear la superficie del Prisma
    ax.plot_surface(r*np.cos(theta), r*np.sin(theta), z[:,np.newaxis],alpha=0.5)
    # Dibuja el prisma en alambre2
    #ax.plot_wireframe(r*np.cos(theta), r*np.sin(theta), z[:,np.newaxis])

    # Añadir etiquetas de los ejes
    ax.set_title('Prisma 3D')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-longL, longL])
    ax.set_ylim([-longL, longL])
    ax.set_zlim([-0, alto])

    # Mostrar el gráfico
    plt.show()

def ModeladoCUBO(LB):
    # Crear los vértices del cubo en funcion de una plano tridimensional
    #  donde cada arreglo de 3 valores representa la hubicacion en (x,y,z)
    v = np.array([
        [0, 0, 0],
        [LB, 0, 0],
        [LB, LB, 0],
        [0, LB, 0],
        [0, 0, LB],
        [LB, 0, LB],
        [LB, LB, LB],
        [0, LB, LB],
    ])

    # Crear una lista de triángulos para la pirámide donde cada numero [0,1,2,3,4,5,6,7]
    #  representan los vertices ingresado para ser especificos en el mismo orden que fueron ingresado
    triangulos = [
        [0, 1, 2],
        [0, 2, 3],

        [0, 1, 4],
        [1, 4, 5],

        [0, 4, 7],
        [0, 3, 7],

        [3, 6, 7],
        [2, 3, 6],

        [1, 5, 6],
        [1, 2, 6],

        [4, 5, 6],
        [4, 6, 7]
    ]

    # Crear una figura y un conjunto de ejes 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Añadir etiquetas de los ejes
    ax.set_title('CUBO 3D')
    ax.set_xlabel('Plano X')
    ax.set_ylabel('Plano Y')
    ax.set_zlabel('Plano Z')
    ax.set_xlim([-0, LB])
    ax.set_ylim([-0, LB])
    ax.set_zlim([-0, LB])

    # Dibujar la pirámide utilizando plot_trisurf
    ax.plot_trisurf(v[:,0], v[:,1], triangulos, v[:,2], cmap='inferno')

    # Mostrar el gráfico
    plt.show()

def ModeladoPiramide(lados,LB,altura):
    if lados<=2:
        print('no se puedes crear una piramide con el primer parametro menor a 3')
    elif lados==3:
        # Crear los vértices de la pirámide en funcion de una plano tridimensional 
        # donde cada arreglo de 3 valores representa la hubicacion en (x,y,z)
        v = np.array([
            [0, 0, 0],
            [(LB*(math.sqrt(6)-math.sqrt(2)))//4, (LB*(math.sqrt(6)+math.sqrt(2)))//4, 0],
            [(LB*(math.sqrt(6)+math.sqrt(2)))//4, (LB*(math.sqrt(6)-math.sqrt(2)))//4, 0],
            [(LB*(math.sqrt(6)))//6, (LB*(math.sqrt(6)))//6, altura]
        ])

        # Crear una lista de triángulos para la pirámide donde cada numero [0,1,2,3] 
        # representan los vertices ingresado para ser especificos en el mismo orden que fueron ingresado
        triangulos = [
            [0, 1, 2],
            [0, 2, 3],
            [1, 2, 3],
            [0, 1, 3]
        ]

        # Crear una figura y un conjunto de ejes 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Dibujar la pirámide utilizando plot_trisurf
        ax.plot_trisurf(v[:,0], v[:,1], triangulos, v[:,2], cmap='viridis')
        # Mostrar el gráfico
        plt.show()

    elif lados==4:
        # Crear los vértices de la pirámide en funcion de una plano tridimensional 
        # donde cada arreglo de 3 valores representa la hubicacion en (x,y,z)
        v = np.array([
            [0, 0, 0],
            [LB, 0, 0],
            [LB, LB, 0],
            [0, LB, 0],
            [LB//2, LB//2, altura]
        ])

        # Crear una lista de triángulos para la pirámide donde cada numero [0,1,2,3,4] 
        # representan los vertices ingresado para ser especificos en el mismo orden que fueron ingresado
        triangulos = [
            [0, 1, 2],
            [0, 2, 3],
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4]
        ]

        # Crear una figura y un conjunto de ejes 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
            # Añadir etiquetas de los ejes
        ax.set_title('PIRAMIDE 3D')
        ax.set_xlabel('Plano X')
        ax.set_ylabel('Plano Y')
        ax.set_zlabel('Plano Z')
        ax.set_xlim([-0, LB])
        ax.set_ylim([-0, LB])
        ax.set_zlim([-0, altura])

        # Dibujar la pirámide utilizando plot_trisurf
        ax.plot_trisurf(v[:,0], v[:,1], triangulos, v[:,2], cmap='viridis')

        # Mostrar el gráfico
        plt.show()

def ModeladoCilindro(alto,radio,segmentos):
    #primer parametro es el punto inicial , el segundo el final y el 
    # tercero el numero de punto que se ubicaran entre el primer y segundo
    theta = np.linspace(0, 2*np.pi, segmentos)
    z = np.linspace(0, alto, 2)
    
    #cambia los valores de arreglo entregado a 1 y lo retorna
    r = np.ones_like(theta) * radio

    # Crear la figura y el eje 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Crear la superficie del cilindro
    #a diferencia de los otros metodos no se usa como base o referencia los segmentos creados 
    #tanto para el area o el lado tranversal como las bases del cilindro
    ax.plot_surface(r*np.cos(theta), r*np.sin(theta), z[:,np.newaxis], alpha=0.5)

    # Dibuja el cilinddro en alambre
    #ax.plot_wireframe(r*np.cos(theta), r*np.sin(theta), z[:,np.newaxis])

    # Añadir etiquetas de los ejes
    ax.set_title('Cilindro 3D')
    ax.set_xlabel('Plano X')
    ax.set_ylabel('Plano Y')
    ax.set_zlabel('Plano Z')
    ax.set_xlim([-radio, radio])
    ax.set_ylim([-radio, radio])
    ax.set_zlim([-0, altura])
    # Mostrar el gráfico
    plt.show()

def ModeladoEsfera(radio):
    # Crea los datos para una esfera
    # primer parametro es el punto inicial , el segundo el final y el tercero
    # el numero de punto que se ubicaran entre el primer y segundo
    r=radio+1
    phi = np.linspace(0, np.pi, 120)
    theta = np.linspace(0, 2*np.pi, 60)

    # el metodo se encarga de crear una malla de 2 dimensiones en la cual usa 
    # los puntos del primer como el segundo arreglo y asi crear una malla bidibimentsional 
    # a paratir de dos unidimesionales

    phi, theta = np.meshgrid(phi, theta)

    x = np.sin(phi) * np.cos(theta) * r
    y = np.sin(phi) * np.sin(theta) * r
    z = np.cos(phi) * r

    # Crea una figura y un subplot 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')

    # Dibuja la esfera en alambre
    #ax.plot_wireframe(x, y, z)

    # Configura los límites de los ejes
    # Añadir etiquetas de los ejes
    ax.set_title('Esfera 3D')
    ax.set_xlabel('Plano X')
    ax.set_ylabel('Plano Y')
    ax.set_zlabel('Plano Z')
    ax.set_xlim([-radio, radio])
    ax.set_ylim([-radio, radio])
    ax.set_zlim([-radio, radio])

        # Muestra la figura
    plt.show()

def ModeladoCONO(r, h):

    n = 1000
    theta = np.linspace(0, 2*np.pi, n+1)[:-1]
    x = np.cos(theta)*r
    y = np.sin(theta)*r
    z = np.zeros(n)

    # Definir los vértices del cono
    vertices = np.vstack((np.vstack((x, y, z)).T, np.array([0, 0, h])))

    # Definir las caras que imularan el lado del cono
    faces = []
    for i in range(n):
        faces.append([i, (i+1)%n, n])
    faces = np.array(faces)

    # Crear la figura y los ejes 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Dibujar el cono
    cono = Poly3DCollection(vertices[faces], alpha=0.5, facecolor='g')
    ax.add_collection(cono)

    # Ajustar los límites de los ejes
    ax.set_title('CONO 3D')
    ax.set_xlabel('Plano X')
    ax.set_ylabel('Plano Y')
    ax.set_zlabel('Plano Z')
    ax.set_xlim(-r, r)
    ax.set_ylim(-r, r)
    ax.set_zlim(0, h)

    # Mostrar la figura
    plt.show()






# Mostramos el menú y leemos la opción elegida por el usuario
while True:
    print("Modelado 3D en Python")
    print("1. Modelar Piramide")
    print("2. Modelar Prisma")
    print("3. Modelar Cubo")
    print("4. Modelar Cilindro")
    print("5. Modelar Esfera")
    print("6. Modelar Cono")
    print("0. Salir")
    opcion = input("Elige una opción: ")

    # Ejecutamos la función correspondiente
    if opcion == "1":
        Num_lados=int(input('Ingrese el numero de lados de la Base de la piramide: '))
        LongL=float(input('longitud de los lados de la base: '))
        altura=float(input('Ingrese la altura de la piramide: '))
        print('Construyendo Puramide......')
        ModeladoPiramide(Num_lados,LongL,altura)
    elif opcion == "2":
        Num_lados=int(input('Ingrese el numero de lados de la Base del Prisma: '))
        LongL=float(input('longitud de los lados de la base: '))
        altura=float(input('Ingrese la altura del Prisma: '))
        print('Construyendo Prisma......')
        ModeladoPrisma(altura,Num_lados,LongL)
    elif opcion == "3":
        LongL=float(input('longitud de los lados del cubo: '))
        print('Construyendo Cubo......')
        ModeladoCUBO(LongL)
    elif opcion == "4":
        radio=float(input('Ingrese el Radio del Cilindro: '))
        altura=float(input('Ingrese la altura del Cilindro: '))
        print('Construyendo Cilindro......')
        ModeladoCilindro(altura,radio,segmentos=1000)
    elif opcion == "5":
        radio=float(input('lRadio de la Esfera: '))
        print('Construyendo esfera......')
        ModeladoEsfera(radio)
    elif opcion == "6":
        radio=float(input('Radio de la base del cono: '))
        altura=float(input('Altura del cono: '))
        ModeladoCONO(radio,altura)
    elif opcion == "0":
        break
    else:
        print("Opción inválida")