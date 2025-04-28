def nombreCerveza(msn):
    while True:
        try:
            resultado =input(msn).strip()
            if not resultado:
                raise ValueError("Error vacio")
            if any(char.isdigit() for char in resultado):
                 raise ValueError("Error no numeros")
            return resultado
        except ValueError as e:
            print(e)

def mostrar():
    print(nombreCerveza("Ingrese un valor"))   
if __name__=="__main__":
    mostrar()