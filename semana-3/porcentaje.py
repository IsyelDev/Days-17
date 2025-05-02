def descuento():
    return print(850 * 0.85)

def empleado(anual):
    return print(round(anual * 1.12),2)

def porcentajeAlumnos(alumnos,mujeres):
    return print((mujeres/alumnos)*100)

def comparador():
    return ((15625-12500)/12500)*100

def iva(iva):
    return 1380*iva

def descuento_inverso():
    return 280 /(1-0.30)

decimal = 25/100
print(decimal)
porcentaje = 0.375 * 100
print(porcentaje)


if __name__=="__main__":
    descuento()
    empleado(52000)
    porcentajeAlumnos(240,96)
    print(comparador())
    print(iva(1.21))
    print(descuento_inverso())