def mango(quantity, price_per_mango):
    """
    Calcula el costo total de los mangos con una oferta de "3 por 2".

    :param quantity: La cantidad de mangos que se quiere comprar.
    :param price_per_mango: El precio por mango.
    :return: El costo total aplicando la oferta "3 por 2".
    """
    # Dividimos la cantidad en grupos de 3 y sumamos los mangos que se pagan.
    paid_mangoes = (quantity // 3) * 2 + (quantity % 3)

    # Calculamos el costo total
    total_cost = paid_mangoes * price_per_mango

    return total_cost


# Ejemplos de uso
print(mango(2, 3))  # Output: 6
print(mango(3, 3))  # Output: 6
print(mango(5, 3))  # Output: 12
print(mango(9, 5))  # Output: 30
