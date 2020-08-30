
'''
/////////////////////////////////////////////
//    PONTIFICIA UNIVERSIDAD JAVERIANA     //
//                                         //
//  Carlos Daniel Cadena Cahvarro          //
//  Procesamiento de imagenes y vision     //
//  TALLER #2                              //
/////////////////////////////////////////////
'''

import cv2
import random
import numpy as np
import os
import math
from matplotlib import pyplot as plt

class imageShape:

    def __init__(self, width, height):          # Constructor
        self.width = width                      # Ancho de la imagen
        self.height = height                    # Alto de la imagen
        self.centro = (int(float(self.width/2)), int(float(self.height/2)))    # Centro de la imagen

    def generateShape (self):                        # Metodo generateShape
        size = (self.height, self.width, 3)          # Tamaño de la imagen
        self.image_black = np.zeros(size, np.uint8)  # Imagen con fondo negro
        self.shape_x = random.randint(0, 3)          # Número aleatorio entre 0 y 3
        self.x = 1                                   # Bandera x

        # Triangulo
        if self.shape_x == 0:                               # Condicion de Triangulo
            lado = min(self.width, self.height)/2           # Magnitud de los lados
            altura = math.sqrt(lado**2+(lado/2)**2)         # Altura del triangulo

            start1 = int(float(self.width/2-lado/2))        # Coordenada en x de inicio
            start2 = int(float(self.height/2 + altura/2))   # Coordenada en y de inicio
            start_f = (start1, start2)                      # Coordenada de inicio para la primera linea (_)
            end1 = int(float(self.width/2+lado/2))          # Coordenada en x final
            end2 = int(float(self.height/2+altura/2))       # Coordenada en y final
            end_f = (end1, end2)                            # Coordenada final para la primera linea (_)

            start3 = int(float(self.width/2))               # Coordenada en x de inicio
            start4 = int(float(self.height/2- altura/2))    # Coordenada en y de inicio
            start_f1 = (start3, start4)                     # Coordenada de inicio para la segunda linea (\)
            end_f1 = (end1, end2)                           # Coordenada final para la segunda linea (\)

            start_f2 = (start3, start4)                     # Coordenada de inicio para la tercera linea (/)
            end_f2 = (start1, start2)                       # Coordenada final para la tercera linea (/)

            pts = np.array([[start_f], [end_f], [start_f1], [end_f1], [start_f2], [end_f2]])   # Matriz de coordenadas
            self.shape = cv2.drawContours(self.image_black, [pts], 0, (246, 176, 0), -1)       # Dibujo del Triangulo
            cv2.imwrite("Triangle.png", self.shape)         # Almacenar imagen Triangle

        # Cuadrado
        elif self.shape_x == 1:
            lado = int(float(min(self.width, self.height)/2))   # Magnitud de los lados

            start_1 = int(float(self.width/2-lado/2))           # Coordenada x de inicio
            start_2 = int(float(self.height/2-lado/2))          # Coordenada en y de inicio
            start_p = (start_1, start_2)                        # Coordenada de inicio
            end_1 = int(float(lado+start_1))                    # Coordenada x final
            end_2 = int(float(lado+start_2))                    # Coordenada y final
            end_p = (end_1, end_2)                              # Coordenada final

            self.shape = cv2.rectangle(self.image_black, (start_p), (end_p), (246, 176, 0), -1) # Dibujar un Cuadrado
            M = cv2.getRotationMatrix2D(self.centro, 45, 1)     # Rotar el dibujo
            self.shape = cv2.warpAffine(self.shape, M, (self.width, self.height))
            cv2.imwrite("Square.png", self.shape)               # Almacenar imagen Square

        # Rectangulo
        elif self.shape_x == 2:
            lado_horizontal = int(float(self.width/2))     # Magnitud del ancho
            lado_vertical = int(float(self.height/2))      # Magnitud del alto

            start_1 = int(float(self.width/4))             # Coordenada x de inicio
            start_2 = int(float(self.height/4))            # Coordenada en y de inicio
            start_p = (start_1, start_2)                   # Coordenada de inicio
            end_1 = int(float(lado_horizontal*1.5))        # Coordenada x final
            end_2 = int(float(lado_vertical*1.5))          # Coordenada y final
            end_p = (end_1, end_2)                         # Coordenada final

            self.shape = cv2.rectangle(self.image_black, (start_p), (end_p), (246, 176, 0), -1) # Dibujar un Rectangulo
            cv2.imwrite("Rectangle.png", self.shape)       # Almacenar imagen Rectangle

        # Circulo
        else:
            radio = int(float(min(self.width, self.height)/4))  # Radio
            self.shape = cv2.circle(self.image_black, self.centro, radio, (246, 176, 0), -1)  # Dibujar un Circulo
            cv2.imwrite("Circle.png", self.shape)           # Almacenar imagen Rectangle

        self.x = 0

    def showShape(self):                                    # Metodo showShape
        if self.x == 0:                                     # Condicion para Visualizar imagen
            cv2.imshow("Imagen Disponible", self.shape)     # Mostrar imagen
            cv2.waitKey(5000)                               # Esperar 5s
            cv2.destroyAllWindows()                         # Destruye las ventanas creadas
        else:
            cv2.imshow(self.image_black)                    # Mostrar imagen en negro
            cv2.waitKey(5000)                               # Esperar 5s
            cv2.destroyAllWindows()                         # Destruye las ventanas creadas

    def getShape(self):                                     # Metodo getShape
        cv2.imshow("Imagen Final", self.shape)              # Mostrar imagen final
        cv2.waitKey(0)                                      # Esperar
        cv2.destroyAllWindows()                             # Destruye las ventanas creadas
        self.y = self.shape_x                               # Variable de tipo de figura

        if self.y == 0:                         # Condicion para nombre de la figura (Triangle)
            print('Image = Triangle')           # Imprimir Traingle
        elif self.y == 1:                       # Condicion para nombre de la figura (Square)
            print('Image = Square')             # Imprimir Square
        elif self.y == 2:                       # Condicion para nombre de la figura (Rectangle)
            print('Image = Rectangle')          # Imprimir Rectangle
        else:                                   # Condicion para nombre de la figura (Circle)
            print('Image = Circle')             # Imprimir Circle

    def whatShape(self, path):                  # Metodo whatShape
        self.shape = cv2.imread(path, 1)        # Leer imagen
        im_gray = cv2.cvtColor(self.shape, cv2.COLOR_BGR2GRAY)     # Convertir imagen de BGR a escala de grises
        ret, thresh = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)  # Umbralizacion con OTSU
        contornos, jerarquía = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Encontrar contornos
        # Contornos externos y vertices

        for c in contornos:
            epsilon = 0.01*cv2.arcLength(c, True)                   # Calcula perimetro de contorno o long. de curva
            approx = cv2.approxPolyDP(c, epsilon, True)             # Aprximar la curva
            x, y, w, h = cv2.boundingRect(approx)                   # Rectangulo delimitador

            if len(approx) == 3:                                    # Condicion para clasificar Triangulo
                print('La figura corresponde a un Triangulo')       # Imprimir "Triangulo"
            elif len(approx) >= 5:                                  # Condicion para clasificar Circulo
                print('La figura corresponde a un Circulo')         # Imprimir "Circulo"
            elif len(approx) == 4:                                  # Condicion para clasificar Cuadrado y Rectangulo
                aspect_ratio = float(w)/h                           # Relacion de aspecto de la figura
                if aspect_ratio == 1:                               # Condicion Cuadrado
                    print('La figura corresponde a un Cuadrado')    # Imprimir "Cuadrado"
                else:                                               # Condicion Rectangulo
                    print('La figura corresponde a un Rectangulo')  # Imprimir "Rectangulo"
            else:                                                   # Condicion para otro caso
                print('La figura corresponde a un nada')            # Imprimir "Nada"

