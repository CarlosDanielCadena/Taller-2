
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
    x, y = imagen.getShape()
    tp = imagen.whatShape(x)
    if y == tp:
        print('La clasificación realizada es correcta')
    else:
        print('La clasificación realizada es incorrecta')
