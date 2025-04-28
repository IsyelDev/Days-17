def variables(nombre,edad):
    while True:
        try:
            if not nombre or not edad:
                raise ValueError("Error valor vacio")
            if any(m.isdigit() for m in nombre):
                raise ValueError("Ingrese un valor string")
            if any(x.isalpha() for x in str(edad)):
                raise ValueError("Ingrese un valor numerico")
            return f"Mi nombre es {nombre}\nMi edad es {edad}"
        except ValueError as e:
            print(f"Error {e}")
            break


def imprimir(msn):
    while True:
        try:
           resultado = input(msn)
           if not resultado:
               raise ValueError("Valores Vacios")
           if any(matc.isdigit() for matc in resultado):
               raise ValueError("Valores String")
           return resultado.upper()
        except ValueError as e:
            print(f"{e}")

def mostrar():
    resultado = imprimir("Ingrese un curso \n")
    print(f"Estas tomando un curso de {resultado} ")



def conversion():
    num1 = 7.5
    print(type(int(num1)))

if __name__=="__main__":
    print(variables("Tony Sopranor",51))
    mostrar()
    numero = 2056.25451
    print(f"{numero:.2f}")
    print(type(numero))
    conversion()