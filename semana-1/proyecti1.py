def crearNombre(msn):
    while True:
        try:
            resultado = input(msn).strip()
            if not resultado:
                raise ValueError("Error con vacio")
            if any(m.isdigit() for m in resultado):
                raise ValueError("Error con vacio")
            return resultado
        except ValueError as e:
            print(f"{e}")

def mostrarNombre():
    resultado =[crearNombre(f"Que {item} te gustaria visitar \n") for item in ["ciudad","Color"]]
    nombre_final =" ".join(resultado)
    print(f"El nombre de tu cerveza es '{nombre_final}'")

if __name__=="__main__":
    mostrarNombre()
    print("===================")