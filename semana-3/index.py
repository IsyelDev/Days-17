def posicion(nombre):
    return nombre[4]

def primera(aparicion):
    while True:  # Bucle infinito hasta que ingrese un valor no vacío
        if not aparicion:  # Si la cadena está vacía
            # Lanza un error con un mensaje personalizado
            raise ValueError("¡Error! No puedes ingresar un valor vacío.")
        else:
            # Busca la primera aparición de 'práctica'
            if "práctica" in aparicion:
                return aparicion.index("práctica")
            else:
                raise ValueError("La palabra 'práctica' no se encontró en el texto.")

def ultima(aparicion):
    while True:  # Bucle infinito hasta que ingrese un valor no vacío
        if not aparicion:  # Si la cadena está vacía
            # Lanza un error con un mensaje personalizado
            raise ValueError("¡Error! No puedes ingresar un valor vacío.")
        else:
            # Busca la última aparición de 'práctica'
            salida = aparicion.find("práctica", 30)
            if salida == -1:
                raise ValueError("La palabra 'práctica' no se encontró después del índice 30.")
            return salida
        
def slicing(oracion):
    return oracion[0:9]

def slicing2(oracion):
    return oracion[9:-1:3]

def slicing3(oracion):
    print("".join(reversed(oracion)))
    return oracion[::-1]

def cambio(oracion):
    if "difícil" in oracion:
        oraciono =oracion.replace("difícil","facil")
    if "mala" in oracion:
        oraciono = oracion.replace("mala","buena")
    return oraciono


def valores(prueba):
    return True if prueba == "booleano" else False
        


if __name__ == "__main__":
    print(posicion("ordenador"))  # Sale 'n'
    print(slicing("Controlar la complejidad es la esencia de la programación"))
    print(slicing2("Nunca confíes en un ordenador que no puedas lanzar por una ventana"))
    print(slicing3("Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"))
    print(cambio("Si la implementación es difícil de explicar, puede que sea una mala idea."))
    print(valores("booleano"))

"""
    try:
        texto_entrada = input("Ingresa una cadena para buscar la primera aparición de 'práctica': ")
        print(primera(texto_entrada))  # Busca la primera aparición
    except ValueError as e:
        print(e)  # Muestra el mensaje de error si se lanza una excepción

    try:
        texto_entrada = input("Ingresa una cadena para buscar la última aparición de 'práctica': ")
        print(ultima(texto_entrada))  # Busca la última aparición
    except ValueError as e:
        print(e)  # Muestra el mensaje de error si se lanza una excepción
"""

