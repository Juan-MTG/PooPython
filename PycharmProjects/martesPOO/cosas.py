class Alumno:

    facultad = "FES ARAGÓN"

    def __init__(self,nombre,edad,carrera):
        '''
        para saber de que tipo es un objeto
        print(type(self))
        '''

        #PYTHON SIMULA EL ENCAPSULAMIENTO  PONIENDO "__" ANTES DE LA DECLARACION DE UN ATRIBUTO
        self.__nombre = nombre
        self.__edad = edad
        self.__carrera = carrera