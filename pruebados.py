from collections import deque
import time
import random

class Coche:
    def __init__(self, id_coche, estado):
        self.id_coche = id_coche
        self.estado = estado
        
    def repostandoypago(self):
        self.estado = "repostando y pagando"
        n = random.randint(5, 10)
        time.sleep(n+3)
        
    def en_cola_espera(self):
        self.estado = "en cola de espera"
        
    def en_cola_repostaje(self):
        self.estado = "en cola de repostaje"

class ColaEspera:
    def __init__(self):
        self.cola = deque()
        self.id_siguiente_coche = 1
        
    def agregar_coche(self):
        coche = Coche(self.id_siguiente_coche, "en cola de espera")
        self.cola.append(coche)
        self.id_siguiente_coche += 1
        p=random.randint(1, 15)
        time.sleep(p)
        
    def eliminar_coche(self):
        coche = self.cola.popleft()
        return coche
    
    def mostrar_cola(self):
        for coche in self.cola:
            print(f"Coche {coche.id_coche}: {coche.estado}")

class ColaDeRepostaje:
    def __init__(self):
        self.cola = []

    def añadir_coche(self, coche):
        self.cola.append(coche)
        coche.estado = "en cola de repostaje"
        time.sleep(5) 


    def sacar_coche(self):
        if len(self.cola) == 0:
            return None
        else:
            coche = self.cola.pop(0)
            coche.estado = "repostando y pagando"
            return coche

    def __len__(self):
        return len(self.cola)
    

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