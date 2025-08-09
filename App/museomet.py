"""                    Esta es la clase principal. Nucleo del programa
------------------------------------------------------------------------------------------"""

import requests          # Importacion de las librerias ncesarias para solicitudes de la API y manejo de archivos
from PIL import Image

from Classes.ObraDeArte import ObrArt           # Importacion de las clases para objetos de tipo "Obra de arte" y "departamento"
from Classes.Departamento import Departamento

from LocalData.menu import img_ascii, menu_inicio              # Importacion de la imagen ASCII para decorar y el menu inicial
#from LocalData.Nacionalidades import nacionalidades_list         # Importacion de la lista de nacionalidades




class museomet:
    
    def __init__(self,departamentos = []):           # Atributo de la clase principal y lista a llenar con los departamentos del museo
        self.departamentos = departamentos

#--------------------------------------------------------------------------------

    UrlBaseApi = "https://collectionapi.metmuseum.org/public/collection/v1"       # URL base de la API del museo


    def get_from_api(self, endpoint):                                          # Metodo basico para solicitar datos a la API segun el endpoint que se le introduzca
        try:                                                                     # Usa la sentancia try-except para evitar errores de conexion y demas.
             respuesta = requests.get(f"{self.UrlBaseApi}/{endpoint}")            # Guarda los datos como un JSON en "respuesta"
             return respuesta.json()   
        except requests.exceptions.RequestException as errorcode:
            print(f" Error {errorcode} con la API") 
            return None

#  --------------------------------------------------------------------------
    
    def cargar_departamentos(self):                                                    # Metodo que guarda los departamentos como un diccionario desde la solicitud, para luego cederle los parametros a cada objeto 
        dptos_data = self.get_from_api("departments")                                     #  -->         de tipo "Departamento" que se guardaran en la lista de departamentos
        if dptos_data and 'departments' in dptos_data:
            for dep in dptos_data['departments']:
                departamento = Departamento(dep['departmentId'], dep['displayName'])       # instanciar departamentos
                self.departamentos.append(departamento)
        else:
            print("No se pudieron cargar los departamentos")    
    
# ------------------------------------------------------------------------------------------

    def buscar_obras_por_departamento(self):
        print("Estos son los departamentos disponibles:")
        for dep in self.departamentos:
            dep.show() 
                                                         #Ahora para mostrar las obras por departmaneto se llama a la API luego de pedir el ID del departamento
         
        Udepchoice = int(input("Ingrese el ID del departamento que desee consultar (solo numeros) --->"))
     
        try:
            obra_dept = self.get_from_api(f"objects?departmentIds={Udepchoice}")
            if (obra_dept is None) or (obra_dept.get("objectIDs") is None):         # El metodo .get() evita errores si la clave "objectIDs" no existe 
                print("No se encontraron obras en este departamento")
                return
         
            for obra_id in obra_dept['objectIDs'][:25]:
                detalles_obra = self.get_from_api(f"objects/{obra_id}")
                if detalles_obra:
                     obra_obj = ObrArt(detalles_obra.get('objectID', 'N/A'),           
                                   detalles_obra.get('title', 'Sin título'),
                                   detalles_obra.get('artistDisplayName', 'Artista desconocido'),
                                   detalles_obra.get('artistNationality', 'N/A'),
                                   detalles_obra.get('artistBeginDate', 'N/A'),
                                   detalles_obra.get('artistEndDate', 'N/A'),
                                   detalles_obra.get('classification', 'N/A'),
                                   detalles_obra.get('objectDate', 'N/A'),
                                   detalles_obra.get('primaryImageSmall', ''))   # Con .get se evitan errores si llega a faltar algun atributo a la hora de instanciar
                     obra_obj.show_res()  # Muestra detalles resumidos de la obra    
                     print()
     
        except ValueError:
            print("ID de departamento inválido. Por favor, ingrese un número")
        except requests.exceptions.RequestException as errorcode:
            print(f"Error {errorcode} al buscar obras por departamento")
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------    
    
    def buscar_obras_autor(self):
       
       print("¿Viste algun autor que te llamara la atencion?")
       nombre_autor = input(" Escribe aquí su nombre para ver sus obras ---> ")
 
       print(f"Buscando obras de '{nombre_autor}', por favor espere...")

       autor = self.get_from_api(f"search?artistOrCulture=true&q={nombre_autor}")
       if (autor is None) or (autor.get("objectIDs") is None):
            print("No se encontraron obras para ese autor")
            return

       for obj_id in autor["objectIDs"][:25]: 
            detalles_obra = self._api_get(f"objects/{obj_id}")
            if detalles_obra:
                obra_obj = ObrArt(detalles_obra.get('objectID', 'N/A'),           
                                   detalles_obra.get('title', 'Sin título'),
                                   detalles_obra.get('artistDisplayName', 'Artista desconocido'),
                                   detalles_obra.get('artistNationality', 'N/A'),
                                   detalles_obra.get('artistBeginDate', 'N/A'),
                                   detalles_obra.get('artistEndDate', 'N/A'),
                                   detalles_obra.get('classification', 'N/A'),
                                   detalles_obra.get('objectDate', 'N/A'),
                                   detalles_obra.get('primaryImageSmall', ''))   # Con .get se evitan errores si llega a faltar algun atributo a la hora de instanciar
                obra_obj.show_res()  # Muestra detalles resumidos de la obra igual que mas arriba 
                print()

#-----------------------------------------------------------------------------------------------------------------------------------------                
    
    def ver_detalles_obra(self):
        
        try:
            print("Ingrese el ID de la obra de su interés para ver sus detalles: ")
            id_obra = int(input("Escriba el ID aquí ---> "))
            detalles_obra = self.get_from_api(f"objects/{id_obra}")
            
            if (detalles_obra==None) or ('objectID' not in detalles_obra):
                print(f"No se encontró una obra con el ID {id_obra}")
                return

            obra_obj = ObrArt(detalles_obra.get('objectID', 'N/A'),           
                                   detalles_obra.get('title', 'Sin título'),
                                   detalles_obra.get('artistDisplayName', 'Artista desconocido'),
                                   detalles_obra.get('artistNationality', 'N/A'),
                                   detalles_obra.get('artistBeginDate', 'N/A'),
                                   detalles_obra.get('artistEndDate', 'N/A'),
                                   detalles_obra.get('classification', 'N/A'),
                                   detalles_obra.get('objectDate', 'N/A'),
                                   detalles_obra.get('primaryImageSmall', ''))   # Con .get se evitan errores si llega a faltar algun atributo a la hora de instanciar
            obra_obj.show_res()  # Muestra detalles resumidos de la obra igual que mas arriba 
            print()

            ver_imagen = int(input("""¿Desea ver la imagen de la obra?
                                   --(1) Sí
                                   --(2) No 
                                   Escriba su opción aquí ---> """))
            if ver_imagen == 1:
                self.mostrar_imagen(obra_obj.url_imagen)
            elif ver_imagen != 1 and ver_imagen != 2:
                print("Opción inválida. Solo se admiten enteros del 1 al 2")
        
        except ValueError:
            print("Error: Debe ingresar un ID numérico")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def start(self):            # Metodo principal. Inicia la aplicacion y muestra el menu principal para luego ir llamando a los otros metodos

        print()
        print("Un momento... Cargando datos")
        print()
        print(img_ascii)
       
        while True:
            
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
                print()
                print("Opción inválida. Solo se admiten números enteros del 1 al 4")
                print()