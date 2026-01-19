"""
EX02 (Listas)
Eliminar duplicados manteniendo el orden de aparición.
"""

def unique_preserve_order(values: list[int]) -> list[int]:
    """
    Devuelve una NUEVA lista sin duplicados, manteniendo el orden.

    Ejemplo:
    - [3, 1, 3, 2, 1] -> [3, 1, 2]

    Requisito:
    - No modifiques la lista original.
    """
    lista_nueva = []
    
    for n in values:
        if n not in lista_nueva:
            lista_nueva.append(n)
            
    return lista_nueva
    
    raise NotImplementedError("Implementa unique_preserve_order(values)")
