from collections import deque
import time
import random
from clases.ejercicio import*

def main():
    cola_espera = ColaEspera()
    cola_repostaje = ColaDeRepostaje()
    coche1 = Coche(1)
    coche2 = Coche(2)
    coche3 = Coche(3)
    cola_espera.agregar_coche(coche1)
    cola_espera.agregar_coche(coche2)
    cola_espera.agregar_coche(coche3)
    print("Coches en cola de espera:")
    for coche in cola_espera.cola:
        print(coche)
    coche_en_repostaje = cola_espera.eliminar_coche()
    cola_repostaje.añadir_coche(coche_en_repostaje)
    print("Coches en cola de repostaje:")