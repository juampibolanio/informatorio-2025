"""
Instrucciones:
1. Crea una variable `numero_secreto` y asígnale un número entero (por ejemplo, 7).
2. Crea otra variable `numero_adivinado` y asígnale un valor inicial diferente, 
   como 0.
3. Usa un bucle `while` que se ejecute mientras el `numero_adivinado` sea 
   diferente del `numero_secreto`.
4. Dentro del bucle:
   a. Pide al usuario que ingrese un número usando `input()` y conviértelo a entero.
   b. Actualiza el valor de la variable `numero_adivinado`.
5. Después de que el bucle termine (cuando el usuario adivine), imprime un 
   mensaje de felicitación como "¡Correcto! ¡Adivinaste el número!".

"""

print("=== ADIVINA EL NÚMERO ===");

numero_secreto = 10;

numero_adivinado = 0;

while (numero_adivinado != numero_secreto):
    numero_adivinado = int(input("Ingrese su adivinanza: "));
    
    if (numero_adivinado > numero_secreto):
        print("Más chico");
    elif (numero_adivinado < numero_secreto):
        print("Más alto");

print(f"CORRECTO! Adivinaste el número. Era el {numero_secreto}")