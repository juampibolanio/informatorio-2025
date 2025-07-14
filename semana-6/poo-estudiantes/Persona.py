class Persona():
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def mostrarNombreCompleto(self):
        return print(f"El nombre completo es {self.nombre} {self.apellido}")
    
    def decirNombre(self):
        print(f"Hola, yo soy {self.nombre}")
