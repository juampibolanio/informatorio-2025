"""
Instrucciones:
1. Crea una variable llamada `puntuacion` y asígnale un valor numérico entre 0 y 100.
2. Escribe una estructura condicional (if-elif-else) que imprima la calificación 
   en letra correspondiente a la puntuación:
   - 90 a 100: "Sobresaliente"
   - 80 a 89:  "Muy Bueno"
   - 70 a 79:  "Bueno"
   - 60 a 69:  "Suficiente"
   - Menos de 60: "Insuficiente"

"""
print("=== Calificador de notas ===");

try:
    
    nota = int(input("Ingrese su nota (del 1 al 10) >> "));

    if (nota < 1) or (nota > 10):
        print("Debe ingresar valores del 1 al 10");
    elif (nota >= 9) and (nota <= 10):
        print("Sobresaliente");
    elif (nota == 8):
        print("Muy bueno");
    elif (nota == 7):
        print("Bueno");
    elif (nota == 6):
        print("Suficiente");
    else:
        print("Insuficiente");

except ValueError:
    print("Por favor, ingrese un número válido.")