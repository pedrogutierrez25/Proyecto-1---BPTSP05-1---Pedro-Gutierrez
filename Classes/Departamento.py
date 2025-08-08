#Clase de objeto "departamentos" con ID y nombre

class Departamento:
    
    def __init__(self, id_dpto, nombre):                 #Atributos de los objetos de tipo departamento
        self.id = id_dpto
        self.nombre = nombre

    def show(self):
        print(f"ID: {self.id} - {self.nombre}")          #Metodo para imrpimir info sobre un depatamento
