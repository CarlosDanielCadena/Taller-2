
'''
/////////////////////////////////////////////
//    PONTIFICIA UNIVERSIDAD JAVERIANA     //
//                                         //
//  Carlos Daniel Cadena Cahvarro          //
//  Procesamiento de imagenes y vision     //
//  TALLER #2                              //
/////////////////////////////////////////////
'''

from imageShape import *         # Importar

if __name__ == "__main__":       # Main
    widht = int(input("Por favor ingrese el ancho de la imagen: "))
    height = int(input("Por favor ingrese el alto de la imagen: "))  # Ingreso de la ruta de la imagen
    imagen = imageShape(widht, height)
    imagen.generateShape()
    imagen.showShape()
    imagen.getShape()
    image = input("Por favor ingrese el nombre de la imagen (Triangle, Square, Rectangle, Circle) con el png: ")  # Ingreso de la ruta de la imagen
    imagen.whatShape(image)
