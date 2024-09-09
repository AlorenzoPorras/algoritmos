import math


def calculate_16_9_resolution(x, y):
    """
    Calcula la resolución con una relación de aspecto de 16:9 manteniendo la altura (Y) constante.

    Parámetros:
    x (int): Resolución original en el eje X (ancho).
    y (int): Resolución original en el eje Y (altura).

    Retorna:
    tuple: Una tupla que contiene la nueva resolución (nuevo_x, y) donde nuevo_x mantiene la relación 16:9.
    """
    # Calcula el nuevo ancho (X) utilizando la relación 16:9
    # 16:9 implica que el ancho (X) es 16/9 veces la altura (Y)
    new_x = (16 / 9) * y

    # Redondea el nuevo ancho hacia arriba al entero más cercano
    new_x = math.ceil(new_x)

    return new_x, y


def validate_resolution(x, y):
    """
    Valida que las resoluciones proporcionadas sean valores enteros positivos.

    Parámetros:
    x (int): Resolución original en el eje X (ancho).
    y (int): Resolución original en el eje Y (altura).

    Retorna:
    bool: True si ambas resoluciones son válidas, de lo contrario False.
    """
    # Verifica que X e Y sean valores enteros positivos
    if x > 0 and y > 0:
        return True
    else:
        return False


def convert_resolution(x, y):
    """
    Convierte una resolución arbitraria a una resolución de aspecto 16:9.

    Parámetros:
    x (int): Resolución original en el eje X (ancho).
    y (int): Resolución original en el eje Y (altura).

    Retorna:
    tuple: Nueva resolución en formato 16:9 (nuevo_x, y) o mensaje de error si la entrada no es válida.
    """
    # Valida las resoluciones proporcionadas
    if validate_resolution(x, y):
        # Calcula la nueva resolución en formato 16:9
        new_resolution = calculate_16_9_resolution(x, y)
        return new_resolution
    else:
        return "Error: Las resoluciones proporcionadas deben ser enteros positivos."


# Ejemplo de uso:
x_original = 374  # Ancho original
y_original = 280  # Altura original

# Convierte la resolución a 16:9 manteniendo la altura
new_resolution = convert_resolution(x_original, y_original)

# Imprime el resultado
print(f"Resolución original: {x_original}x{y_original}")
print(f"Nueva resolución 16:9: {new_resolution[0]}x{new_resolution[1]}")
