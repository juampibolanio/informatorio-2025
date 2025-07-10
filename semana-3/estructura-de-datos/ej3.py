# -----------------------------------------------------------------------------
# Ejercicio 3: Ingredientes Únicos (Conjuntos) 🍇
# -----------------------------------------------------------------------------
"""
Instrucciones:
1. Crea una lista llamada `ingredientes_receta` que contenga ingredientes
   repetidos. Por ejemplo: ["harina", "huevo", "azúcar", "huevo", "harina"].
2. Convierte esta lista en un conjunto (set) para eliminar los duplicados.
   Guarda el resultado en una variable llamada `ingredientes_unicos`.
3. Imprime el conjunto `ingredientes_unicos` para ver el resultado.
4. Usa una condición para verificar si el ingrediente "azúcar" está en el
   conjunto de ingredientes únicos e imprime un mensaje confirmándolo.

"""

ingredientes_receta = ["Leche", "Azúcar", "Sal", "Agua", "Agua"];

print(ingredientes_receta); #Esto es una lista normal

print("====================================")

ingredientes_unicos = set(ingredientes_receta); #Ahora se convirtió a un conjunto.

print(ingredientes_unicos);

if "Azúcar" in ingredientes_unicos:
    print("El conjunto tiene el ingrediente azúcar.");