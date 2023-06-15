class Autor:
    def __init__(self,nom,pseudo):
        self.__nombre = nom
        self.__pseudonimo = pseudo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom

    @property
    def pseudonimo(self):
        return self.__pseudonimo

    @pseudonimo.setter
    def pseudonimo(self,pseudo):
        self.__pseudonimo = pseudo

    def __str__(self):
        return f"""
            --------------------------------------
            Nombre : {self.__nombre}
            Pseudonimo: {self.__pseudonimo}
            --------------------------------------"""

    def escribir(self):
        print(f"{self.__pseudonimo} está escribiendo su siguiente obra")

class Libro:
    def __init__(self, titulo, autor, año, editorial):
        self.__titulo = titulo
        self.__autor = autor
        self.__año = año
        self.editorial = editorial

    @property
    def titulo(self, titulo):
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self,autor):
        self.__autor = autor

    @property
    def año(self):
        return self.__año

    @año.setter
    def año(self, an):
        self.__año = an

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, ed):
        self.__editorial = ed

    def __str__(self):
        return f"""
            Titulo : {self.__titulo}
            Autor : {self.__autor}
            Año : {self.__año}
            Editorial : {self.editorial}
        """

    @classmethod
    def libro_planeta(cls,titulo,autor,año):
        return cls(titulo,autor,año,"Planeta")

    def leer(self,minutos):
        print(f"Leyendo por {minutos} minutos")

class Persona:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

#HERENCIA class subclase (superclase)
class Alumno(Persona):
    def __init__(self, nombre, edad, num_cuenta, carrera, promedio):
        super().__init__(nombre, edad)
        self.__num_cuenta = num_cuenta
        self.__carrera = carrera
        self.__promedio = promedio



