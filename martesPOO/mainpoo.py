from cosas import Alumno

def main():
    """
    al1 = Alumno()
    print(al1)
    al2 = Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    #OJO
    print("----------------------------------")
    #Al hacerlo lo siguiente agregas un atributo del objeto
    #no modificas el atributo de clase
    al1.facultad = "FES ARAGON EDOMEX"
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    print("------------VISTAZO A OBJETOS------------")
    print(vars(al1))
    print(vars(al2))

    print("------------MODIFICACIÓN DE ATRIBUTOS PÚBLICOS------------")
    al1.edad=999
    print(vars(al1))
    print(vars(al2))
    """
    al1 = Alumno("Diego",22,"ICO")
    al2 = Alumno("Montse",20,"DERECHO")


    print(vars(al1))
    #CUANDO SE INTENTA MODIFICAR EL ATRIBUTO ENCAPSULADO, LO HACE DE TAL FORMA QUE
    #NO MODIFICA EL ATRIBUTO DEL OBJETO SEÑALADO PERO AGREGA OTRO ATRIBUTO AL OBJETO CON EL VALOR DADO AL MISMO
    al1.__edad=333
    al1.__carrera="PERIODISMO"
    print(al1.__edad)
    print(vars(al1))

main()