def third_angle(angle1, angle2):
    """
    Calcula el tercer ángulo de un triángulo dado los otros dos ángulos.

    :param angle1: Primer ángulo del triángulo (en grados).
    :param angle2: Segundo ángulo del triángulo (en grados).
    :return: El tercer ángulo del triángulo (en grados).
    """
    # La suma de los ángulos interiores de un triángulo siempre es 180 grados
    return 180 - (angle1 + angle2)


# Ejemplos de uso
print(third_angle(60, 60))  # Output: 60
print(third_angle(45, 90))  # Output: 45
print(third_angle(75, 25))  # Output: 80
