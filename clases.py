

class Auto():
    color = "verde"
    modelo = "toyota"
    precio = 8828

    def __init__(self, piloto, medallas):
        self.piloto = piloto
        self.medallas = medallas

    def acelerar(self, velocidad):
        self.velocidad = velocidad

        print("la velocidad es ", self.velocidad)

    def frenar(self, semaforo):
        self.color_semaforo = semaforo

        print("el estado del semaforo es", self.color_semaforo)



autoToyota = Auto()

print(autoToyota.color)
print(autoToyota.modelo)
print(autoToyota.precio)

print(autoToyota.color_semaforo)


autoToyota.acelerar("30km/h")

print(autoToyota.velocidad)


autoToyota.frenar("rojo")
