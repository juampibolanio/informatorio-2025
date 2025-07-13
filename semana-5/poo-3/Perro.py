from Animal import Animal

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacerSonido(self):
        print("GUAU!")

    def mostrarRaza(self):
        print(f"Soy un perro de raza {self.raza}")

miPerro = Perro("Rogelio", "Mestizo")

miPerro.mostrarNombre()
miPerro.hacerSonido()