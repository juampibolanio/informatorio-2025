# -----------------------------------------------------------------------------
# Ejercicio 2: Coordenadas (Tuplas) 📍
# -----------------------------------------------------------------------------
"""
Instrucciones:
1. Crea una tupla llamada `coordenadas` que contenga una latitud y una longitud
   (por ejemplo, (-27.45, -58.98)).
2. Desempaqueta la tupla en dos variables: `latitud` y `longitud`.
3. Imprime cada variable por separado con un texto descriptivo, como:
   "Latitud: [valor]" y "Longitud: [valor]".
4. Intenta modificar el primer valor de la tupla `coordenadas` (por ejemplo,
   `coordenadas[0] = 10`). Observa el error que Python te muestra. 
   Esto demuestra la inmutabilidad de las tuplas. (Puedes comentar esta línea).

"""

coordenadas = (-27.45, -58.98);

print(f"Las coordenadas son >> {coordenadas}");

latitud = coordenadas[0];
longitud = coordenadas[1];

print(f"Latitud >> {latitud}");
print(f"Longitud >> {longitud}");

print(type(coordenadas));

# coordenadas[1] = "Pepito";   Esto era para verificar la inmutabilidad de las tuplas.
