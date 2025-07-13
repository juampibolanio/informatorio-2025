# -----------------------------------------------------------------------------
# Ejercicio 3: Animales y Herencia (Herencia y Polimorfismo) 🐾
# -----------------------------------------------------------------------------
"""
Instrucciones:
1. Crea una clase base llamada `Animal` con:
   - Un `__init__` que acepte un `nombre`.
   - Un método `hacer_sonido()` que imprima "El animal hace un sonido genérico".

2. Crea una clase `Perro` que **herede** de `Animal`.
   - Llama al constructor de la clase padre (`super().__init__(nombre)`).
   - Sobrescribe el método `hacer_sonido()` para que imprima "¡Guau!".

3. Crea una clase `Gato` que también herede de `Animal`.
   - Llama al constructor de la clase padre.
   - Sobrescribe el método `hacer_sonido()` para que imprima "¡Miau!".

4. Crea un objeto `Perro` y un objeto `Gato`. Llama al método `hacer_sonido()`
   de cada uno para ver cómo cada objeto utiliza su propia versión del método.

"""

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        print("El animal hace un sonido genérico.")

    def mostrarNombre(self):
        print(f"Mi nombre es {self.nombre}")