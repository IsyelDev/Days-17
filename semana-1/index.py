def operacion(n1, n2):
    return n1 - n2
print("====================================")

def imprimirUnaVez():
    print("\t Línea 1 \n \t Línea 2 \n \t Línea 3")
    print(" Línea 1 \n Línea 2 \n Línea 3")
    print("===================================")

def expresion():
    print("A\tB\tC \nD\tE\tF \nG\tH\tI")
    print("===================================")

def barrainvertida():
    print("Barra Normal: / \nBarra Invertida: \ ")
    print("===================================")

def respuesta(msn):
    mensaje = input(msn)
    return mensaje

def mensaje():
    value = respuesta("¿Qué estás estudiando? \n ")
    return value
print("===================================")

def nombreApellido(msn):
    return input(msn)

def imprimirNombres():
    lista=["nombre","apellido"]
    respuestas=[ nombreApellido(f"Ingrese su {item}\n") for item in lista]
    print(respuestas)

print("===================================")

if __name__ == "__main__":
    resultado = operacion(1055, 500)
    print(resultado)
    imprimirUnaVez()
    expresion()
    barrainvertida()
    print(f"Estas estudiando {mensaje().capitalize()} ")
    imprimirNombres()
  

