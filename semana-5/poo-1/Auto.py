# -----------------------------------------------------------------------------
# Ejercicio 1: Creación de una Clase Básica (Clase y Objeto) 🚗
# -----------------------------------------------------------------------------
"""
Instrucciones:
1. Define una clase llamada `Coche`.
2. En el método constructor `__init__`, la clase debe recibir tres atributos:
   `marca`, `modelo` y `año`.
3. Crea un método llamado `descripcion` que retorne un string con la
   descripción del coche, por ejemplo: "Coche: Ford Focus del año 2020".
4. Crea otro método llamado `acelerar` que simplemente imprima un mensaje
   como "El coche está acelerando".
5. Crea un objeto (una instancia) de la clase `Coche` con los datos que prefieras.
6. Llama al método `descripcion` e imprime el resultado.
7. Llama al método `acelerar`.

"""

class Coche:
    
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrarDescripcion(self):
        return f"Auto: {self.marca}  {self.modelo}  del año {self.anio}"

    def acelerar(self):
        return "El auto está acelerando."

    def getMarca(self):
        self.marca
    
    def getModelo(self):
        self.modelo
    
    def getAnio(self):
        self.anio

mi_auto = Coche('Ford', 'Focus', '2025')


print(mi_auto.mostrarDescripcion())
print(mi_auto.acelerar())