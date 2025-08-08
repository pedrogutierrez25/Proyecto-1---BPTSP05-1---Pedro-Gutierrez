from App.museomet import museomet

def main():
      MuseoApp = museomet()
      MuseoApp.start()

main()


"""                                                                 Por: Pedro Gutierrez    BPTSP05-1
-----------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------

                                     PROYECTO #1 ----- DOCSTRING
                                     ---------------------------

    El siguiente programa de consola funge como un pequeno catalogo digital del Museo metropolitano 
    de Arte, con el cual se interactúa mediante linea de comandos. Muestra un simple menú
    en el que se da a elegir visualizar las listas de obras de arte por: Departamento, Nacionalidad del 
    autor y nombre del autor. Una vez seleccionada la obra segun la clasificacion elegida, se pueden 
    consultar su informacion completa, incluyendo imagen.


                                          Aspectos técnicos
                                          -----------------

    La aplicion se diseñó siguiendo una estructura muy similar a la vista en evaluaciones de POO anteriores en
    la asignatura, siguiendo la misma mecánica. El codigo fue modularizado en varios modulos y paquetes que 
    incluyen las clases, la lista de nacionalidades, la app en sí y un modulo principal desde el cual se ejecuta 
    todo el programa.

"""