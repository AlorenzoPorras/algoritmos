def format_number(num):
    """
    Redondea el número dado a dos decimales y lo retorna como una cadena.

    :param num: Un número flotante válido.
    :return: El número redondeado a dos decimales en formato de cadena.
    """
    return f"{num:.2f}"


# Ejemplos de uso
print(format_number(5.5589))  # Output: '5.56'
print(format_number(3.3424))  # Output: '3.34'
