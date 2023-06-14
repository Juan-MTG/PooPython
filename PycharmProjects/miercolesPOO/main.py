from cosas import Alumno,Perro

def main():
    al1 = Alumno("José",19,"ICO")
    print(vars(al1))
    al1.__nombre="Juan"
    print(vars(al1))
    al1.set_nombre("María")
    print(vars(al1))
    print("\n--------To String----------")
    print(al1)
    al1.set_edad(999)
    print(al1)

    al1.estudiar(30)

    print("-----------PERRO--------------")
    perro1 = Perro("Poddle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "De la calle"
    print(vars(perro1))
    perro1.__raza = "otra"
    perro1.edad = 12
    print(perro1)
    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir()

    danes = Perro.perro_grande(0.8)
    print(danes)



main()

