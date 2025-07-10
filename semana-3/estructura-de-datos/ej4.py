# -----------------------------------------------------------------------------
# Ejercicio 4: Información de Contacto (Diccionarios) 📖
# -----------------------------------------------------------------------------
"""
Instrucciones:
1. Crea un diccionario llamado `contacto` con la siguiente información:
   - "nombre": tu nombre
   - "ciudad": tu ciudad
   - "profesion": tu profesión
2. Imprime el valor asociado con la clave "profesion".
3. Agrega un nuevo par clave-valor al diccionario: "telefono" con un número
   de teléfono (como string).
4. Usa un bucle `for` para recorrer e imprimir cada par clave-valor del 
   diccionario en el formato "clave: valor".

"""

contacto = {"nombre" : "Juan Pablo", "ciudad" : "Resistencia", "profesion" : "Programador"};

print(contacto);
print("========================")

print(contacto.get("profesion"));
print("========================");

contacto["telefono"] = "3624-642456";

print(contacto);
print("========================");

for clave, valor in contacto.items():
    print(f"Clave: {clave} \nValor: {valor} \n");