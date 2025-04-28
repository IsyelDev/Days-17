import math
import random
def cuadrado():
    numeros=[random.randint(1,100) for _ in range(10)]
    respuestas=[math.pow(n,2) for n in numeros]
    print(numeros)
    print(respuestas)

if __name__ == "__main__":
    cuadrado()