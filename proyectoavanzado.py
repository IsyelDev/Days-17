import random

# Excepción personalizada para errores de validación
class InputValidationError(Exception):
    pass

def ingreseNombre(msn):
    """
    Función para ingresar el nombre del usuario.
    Valida que el nombre no esté vacío y no contenga números.
    """
    while True:
        nombre = input(msn).strip()
        
        if not nombre:
            raise InputValidationError("El nombre no puede estar vacío.")
        
        if any(char.isdigit() for char in nombre):
            raise InputValidationError("El nombre no puede contener números.")
        
        return nombre

def generarIngresos(cantidad=10, minimo=5, maximo=100):
    """
    Función para generar una lista de ingresos aleatorios.
    :param cantidad: número de elementos a generar (por defecto 10).
    :param minimo: valor mínimo de los ingresos (por defecto 5).
    :param maximo: valor máximo de los ingresos (por defecto 100).
    :return: lista de ingresos aleatorios.
    """
    return [random.randint(minimo, maximo) for _ in range(cantidad)]

def calcularComisiones(sumatoria, porcentaje=0.13):
    """
    Función para calcular las comisiones a partir de la sumatoria de ingresos.
    :param sumatoria: total de los ingresos.
    :param porcentaje: porcentaje de comisión a aplicar (por defecto 13%).
    :return: monto de la comisión calculada.
    """
    return sumatoria * porcentaje

def mostrarResumen(ingresos, comisiones, sumatoria):
    """
    Función para mostrar el resumen de los ingresos, las comisiones y la suma total.
    :param ingresos: lista de ingresos generados.
    :param comisiones: monto de las comisiones calculadas.
    :param sumatoria: total de los ingresos generados.
    """
    print("Lista de ingresos generados:", " ".join(map(str, ingresos)))
    print(f"Sumatoria de ingresos: {sumatoria}")
    print(f"Comisiones (13%): {comisiones:.2f}")
    
    total = comisiones + sumatoria
    print(f"La suma de comisiones y sumatoria es: {total:.2f}")

def salida():
    """
    Función principal que orquesta el flujo del programa.
    Solicita el nombre, genera los ingresos, calcula las comisiones
    y muestra el resumen final.
    :return: mensaje final con nombre y comisión calculada.
    """
    try:
        nombre = ingreseNombre("INGRESE SU NOMBRE: \n")
        ingresos = generarIngresos()
        sumatoria = sum(ingresos)
        comisiones = calcularComisiones(sumatoria)
        
        mostrarResumen(ingresos, comisiones, sumatoria)
        
        return f"Su nombre es {nombre} y su comisión es {comisiones:.2f}."
    
    except InputValidationError as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Mostrar resultado final al usuario
    print(salida())
