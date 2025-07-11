# -----------------------------------------------------------------------------
# Ejercicio 1: Calculadora Básica (Parámetros y Retorno) 🧮
# -----------------------------------------------------------------------------
"""
Instrucciones:
1. Define una función llamada `calcular_area_rectangulo` que acepte dos
   parámetros: `base` y `altura`.
2. Dentro de la función, calcula el área (base * altura).
3. La función debe `retornar` el resultado del cálculo.
4. Llama a la función con dos números de tu elección (por ejemplo, 10 y 5)
   y guarda el resultado en una variable llamada `area_resultado`.
5. Imprime la variable `area_resultado`.

"""

def calcular_area_rectangulo(base, altura):
    area = base * altura
    
    return area

print("=== CALCULAR AREA DE UN RECTÁNGULO ===")
try:
    base = int(input("Ingrese la base >> "))
    altura = int (input("Ingrese la altura >> "))

    resultado_area = calcular_area_rectangulo(base, altura)
    print(f"El valor del área es: {resultado_area}")

except ValueError:
    print("Por favor, ingrese valores numéricos.")