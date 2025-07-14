from Persona import Persona
from Universidad import Universidad
from Carrera import Carrera

#class Estudiante(Persona):
#    def __init__(self, nombre, apellido, dni, carrera):
#        super().__init__(nombre, apellido, dni)
#        self.carrera = carrera

#    def mostrarCarrera(self):
#        return print (f"{self.nombre} {self.apellido} estudia {self.carrera}")

class Estudiante(Persona, Carrera, Universidad):
    def __init__(self, nombre, apellido, dni, nombreUniversidad, especialidad, legajo):
        Persona.__init__(self, nombre, apellido, dni)
        Universidad.__init__(self, nombreUniversidad)
        Carrera.__init__(self, especialidad)
        self.legajo = legajo

    def decirNombre(self):
        return print(f"Hola, yo soy {self.nombre} y soy un estudiante")

    def mostrarInformación(self):
        print(f"""
                Nombre completo: {self.nombre} {self.apellido}
                N° de documento: {self.dni}
                Universidad: {self.nombreUniversidad}
                Carrera: {self.especialidad}
                N° Legajo: {self.legajo}
            """)

    def getNombre(self):
        return print(self.nombre)
    
    def getApellido(self):
        return print(self.apellido)



alumno = Estudiante("Juan Pablo", "Bolanio", 46964669, "UTN FRRe", "Téc. en Programación", 29332)

alumno.mostrarInformación()
alumno.mostrarNombreCompleto()
alumno.getNombre()
alumno.getApellido()

alumno.decirNombre()