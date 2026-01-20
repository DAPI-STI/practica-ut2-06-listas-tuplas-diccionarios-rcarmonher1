"""
EX06 (Compendio: listas + tuplas + diccionarios)
Ticket de compra: calcula coste por producto y total general.
"""

PRICES: dict[str, float] = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}

def checkout(cart: list[tuple[str, int]]) -> tuple[dict[str, float], float]:
    """
    Recibe un carrito como lista de tuplas (producto, unidades).

    Devuelve:
    - Un diccionario con el coste por producto (producto -> coste)
    - Un float con el total general

    Reglas:
    - Si units < 0 -> ValueError
    - Si un producto no existe en PRICES -> ValueError
    - Si un producto aparece varias veces, se acumulan unidades

    Ejemplo:
    [("Pan", 2), ("Huevos", 1), ("Pan", 1)] ->
      ({"Pan": 4.2, "Huevos": 2.3}, 6.5)
    """
    
    coste_prod = {}
    total = 0
    
    for prod, cantidad in cart:
        if cantidad < 0:
            raise ValueError("Las cantidades no pueden ser negativas")
          
        if prod not in PRICES:
            raise ValueError("El producto no existe en la lista de precios")

        if prod in coste_prod:
            coste_prod[prod] = coste_prod[prod] + (PRICES[prod] * cantidad)
            coste_prod[prod] = round(coste_prod[prod], 2)
            
        else:
            coste_prod[prod] = PRICES[prod] * cantidad
            coste_prod[prod] = round(coste_prod[prod], 2)
        
        total = total + (PRICES[prod] * cantidad)
        
    return coste_prod, round(total, 2)
    
    raise NotImplementedError("Implementa checkout(cart)")
