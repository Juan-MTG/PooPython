from cosas import *

def main():
    l1 = Libro.libro_planeta("El perfume",Autor("Patick","PS"),1980)
    print(l1)

    #el codigo para cambiar el pseudonimo dentro del objeto
    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)

    print("------------HERENCIA----------------")
    alumno1 = Alumno("Jose",20,"9238492303","ICO",9)
    alumno1.nombre = "JUAN"
    print(vars(alumno1))
main()