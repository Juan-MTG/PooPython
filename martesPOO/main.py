'''FORMA 1....
#Al importar podemos poner un alias como en este caso "ari"
#import aritmetica as "ari"'''

#FORMA 2 ...
#Es importar directamente las funciones especificas de ese modulo
from aritmetica import suma,resta
def main ():
        resultado = suma(3,None)
        print(resultado)
        print(resta(b=4,a=3))

main ()
