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
    
