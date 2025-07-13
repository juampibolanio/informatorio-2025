from Animal import Animal

class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad = edad

    def mostrarEdad(self):
        print(f"Soy el gato {self.nombre} y tengo {self.edad} años")

    def hacerSonido(self):
        print("MIAU!")

miGato = Gato("Pepito", 3)

miGato.hacerSonido()
miGato.mostrarEdad()