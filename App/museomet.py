"""                    Esta es la clase principal. Nucleo del programa
------------------------------------------------------------------------------------------"""

import requests          # Importacion de las librerias ncesarias para solicitudes de la API y manejo de archivos
from PIL import Image

from Classes.ObraDeArte import ObrArt           # Importacion de las clases para objetos de tipo "Obra de arte" y "departamento"
from Classes.Departamento import Departamento

from LocalData.menu import img_ascii, menu_inicio              # Importacion de la imagen ASCII para decorar y el menu inicial
#from LocalData.Nacionalidades import nacionalidades_list         # Importacion de la lista de nacionalidades




class museomet:
    
    def __init__(self,departamentos = []):           # Atributo de la clase principal
        self.departamentos = departamentos

#--------------------------------------------------------------------------------

    def start(self):

        print()
        print("Un momento... Cargando datos")
        print()

        while True:
            
            print(img_ascii)
            print(menu_inicio)
            Uchoice = input("Escriba su opción aqui---> ")

            if Uchoice == "1":
                print("a")
            elif Uchoice == "2":
                print("b")
            elif Uchoice == "3":
                print("c")
            elif Uchoice == "4":
                print("Gracias por visitar el catalogo, ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Solo se admiten números del 1 al 4")