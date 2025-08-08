"""               Esta es la clase principal donde el programa es ejecutado
------------------------------------------------------------------------------------------"""

import requests          # Importacion de las librerias ncesarias para solicitudes de la API y manejo de archivos
from PIL import Image

from Classes.ObraDeArte import ObrArt           # Importacion de las clases para objetos de tipo "Obra de arte" y "departamento"
from Classes.Departamento import Departamento




class museomet:
    
    def __init__(self,departamentos = []):           # Atributo de la clase principal
        self.departamentos = departamentos

#--------------------------------------------------------------------------------

    def start(self):

        print()
        print("Un momento... Cargando datos")
        print()

        while True:
            
            print("¡Hola! Bienvenido al Museo Metropolitano de Arte de Nueva York")
            print("Este es un catalogo digital de obras de arte")
            print()
            print()
            print()
            
            Uchoice = input(" ¡Hola! Bienvenido al Museo Metropolitano de Arte de Nueva York \n")

