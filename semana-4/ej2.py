# -----------------------------------------------------------------------------
# Ejercicio 2: Saludo Personalizado (Argumentos por Defecto) 👋
# -----------------------------------------------------------------------------
"""
Instrucciones:
1. Define una función llamada `saludar` que acepte dos argumentos:
   - `nombre` (obligatorio).
   - `mensaje` (opcional, con el valor por defecto "¡Te doy la bienvenida!").
2. La función debe imprimir un string que combine el mensaje y el nombre,
   por ejemplo: "¡Hola, Ana! ¡Te doy la bienvenida!".
3. Llama a la función de dos maneras diferentes:
   a. Solo con el argumento `nombre`.
   b. Con los argumentos `nombre` y `mensaje` (con un mensaje personalizado).

"""

def saludar(nombre, mensaje = "¡Te doy la bienvenida!"):
    print(f"¡Hola, {nombre}! {mensaje}")


saludar("Juan", "Sos un capo pa")
saludar("Pedro")