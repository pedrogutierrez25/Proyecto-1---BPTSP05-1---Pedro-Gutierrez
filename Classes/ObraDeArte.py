#Clase de objeto "Obra de Arte" con ID, Titulo, Nombre del Artista, nacionalidad del artista, fecha de nacimiento del artista,
#  fecha de muerte, Tipo (classification), año de creación (objectDate) e Imagen de la obra.

class ObraArt:
   
    def __init__(self, data_dict):
        self.id = id 
        self.titulo = titulo 
        self.artista = artista 
        self.nacionalidad = nacionalidad 
        self.fecha_nacimiento = fecha_nacimiento 
        self.fecha_muerte = fecha_muerte 
        self.tipo = tipo 
        self.ano_creacion = anio_creacion 
        self.url_imagen = url_imagen 

#-----------------------------------------------------------------------------------------------------------------------

    def show_res(self):               #Metodo para mostrar detalles resumidos de cada obra cuando se muestran por lista
      
        print(f"==> ID: {self.id} | Título: {self.titulo} | Artista: {self.artista}")

#-----------------------------------------------------------------------------------------------------------------------
     
    def show(self):                   #Metodo para mostrar informacion completa de cada obra cuando se le llama por ID

        print("\n--- DETALLES DE LA OBRA ---")
        print(f"Título: {self.titulo}")
        print(f"Artista: {self.artista}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Biografía: {self.fecha_nacimiento} - {self.fecha_muerte}")
        print(f"Año de creación: {self.ano_creacion}")
        print(f"Tipo: {self.tipo}")
        print("--------------------------\n")