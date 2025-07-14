class CuentaBancaria():
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
        print(f"""
            Cuenta creada con éxito
            Titular: {self.titular}
            Saldo actual: ARS${self.saldo}
            """)
        
    def depositar(self, monto):
        if (type(monto) == int or type(monto) == float):
            if (monto > 0):
                self.__saldo += monto
                print(f"¡Depósito realizado correctamente! Su nuevo saldo es de ARS${self.__saldo}")
            else:
                print("Debe ingresar un monto superior a 0")
        else:
            print("El monto debe ser un valor numérico")

    def retirar(self, cantidad):
        if (type(cantidad) == int or type(cantidad) == float):
            if (cantidad > 0):
                if (cantidad <= self.__saldo):
                    self.__saldo -= cantidad
                    print(f"¡Retiro realizado correctamente! Su saldo ahora es de ARS${self.__saldo}")
                else:
                    print("No se pudo realizar el retiro. Fondos insuficientes.")
            else:
                print("La cantidad a retirar debe ser mayor a 0")
        else:
            print("La cantidad a retirar debe ser un valor numérico.")

    def consultarSaldo(self):
        print(f"Hola {self.__titular}. Su saldo actual es {self.__saldo}")

    def consultarTitular(self):
        print(f"El titular de esta cuenta es {self.__titular}")