# -----------------------------------------------------------------------------
# Ejercicio 3: Suma de Múltiples Números (*args) ➕
# -----------------------------------------------------------------------------
"""
Instrucciones:
1. Define una función llamada `sumar_todos` que pueda aceptar un número
   indeterminado de argumentos numéricos. (Pista: usa *args).
2. Dentro de la función, inicializa una variable `total` en 0.
3. Usa un bucle `for` para recorrer todos los números recibidos en `args` y
   sumarlos a la variable `total`.
4. La función debe `retornar` el `total`.
5. Llama a la función con diferentes cantidades de números (ej: `sumar_todos(1, 2, 3)`
   y luego `sumar_todos(10, 20, 30, 40, 50)`) e imprime los resultados.

"""
def sumar_todos(*args):
    total = 0

    for numero in args:
        total += numero
    
    return total

print(sumar_todos(1, 2, 3))
print(sumar_todos(10, 20, 30, 40, 50))

def imprimir_palabras(**kwargs):

    for clave, valor in kwargs.items():
        print(f"Clave >> {clave}\n Valor >> {valor}")

imprimir_palabras(nombre = "Juan", edad = 18)