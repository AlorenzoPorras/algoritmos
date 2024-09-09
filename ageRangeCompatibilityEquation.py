import math


def dating_range(age):
    """
    Calcula el rango de edad mínimo y máximo recomendado según la regla "half your age plus seven"
    o la fórmula alternativa si la edad es menor o igual a 14 años. :)

    :param age: La edad de la persona (entero entre 1 y 100).
    :return: Un string con el rango de edad en el formato 'min-max'.
    """
    if age > 14:
        # Si la edad es mayor a 14, usar la regla "half your age plus seven".
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)
    else:
        # Si la edad es menor o igual a 14, usar el 10% de variación.
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)

    # Devolver el rango en el formato 'min-max'.
    return f"{min_age}-{max_age}"


# Ejemplos de uso
print(dating_range(27))  # Output: 20-40
print(dating_range(5))  # Output: 4-5
print(dating_range(17))  # Output: 15-20
