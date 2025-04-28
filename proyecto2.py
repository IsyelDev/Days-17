
import random
def ingreseNombre(msn):
    while True:
       nombre = input(msn).strip()
       if not nombre:
          print("ERROR")
       if any(n.isdigit() for n in nombre):
          print("No hay nombre")
       else:
          return nombre


def sumar():
    listaIngresos =[random.randint(5,100) for _ in range(10)]
    print(" ".join(map(str,listaIngresos)))

    sumatoria = sum(listaIngresos)
    print(f"Sumatoria de ingresos {sumatoria}")

    comisiones = (sumatoria * .13)
    print(f"{comisiones:.2f}")
    
    total = comisiones + sumatoria
    print(f"La suma de {comisiones:.2f} y de {sumatoria} es {round(total,2)}")
    
    return comisiones

def salida():
    nombre = ingreseNombre("INGRESE SU NOMBRE \n")
    comision = sumar()
    return f"Su nombre es {nombre} y su comision es {comision}"

if __name__=="__main__":
    print(salida())