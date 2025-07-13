# -----------------------------------------------------------------------------
# Ejercicio 2: Cuenta Bancaria (Encapsulamiento) 🏦
# -----------------------------------------------------------------------------
"""
Instrucciones:
1. Define una clase llamada `CuentaBancaria`.
2. En el `__init__`, debe recibir el `titular` de la cuenta y un `saldo`
   inicial. El saldo debe ser un atributo "privado" (por convención,
   nómbralo `_saldo`).
3. Crea un método `depositar(cantidad)` que sume la cantidad al saldo.
4. Crea un método `retirar(cantidad)` que reste la cantidad al saldo, pero
   solo si hay fondos suficientes. Si no hay fondos, debe imprimir
   "Fondos insuficientes".
5. Crea un método `consultar_saldo()` que retorne el valor del saldo actual.
   Este es un "getter" que permite ver el saldo sin modificarlo directamente.
6. Crea un objeto de `CuentaBancaria`, realiza un depósito, un retiro
   (válido e inválido) y consulta el saldo final.

"""

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, cantidad):
        self._saldo += cantidad
    
    def retirar(self, cantidad):

        if (self._saldo > cantidad):
            self._saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def consultarSaldo(self):
        print(f"Su saldo actual es de: {self._saldo}")


miCuenta = CuentaBancaria("Juan Pablo Bolanio", 5000)

miCuenta.consultarSaldo()

miCuenta.retirar(2000)

miCuenta.consultarSaldo()

miCuenta.depositar(10000)

miCuenta.consultarSaldo()
