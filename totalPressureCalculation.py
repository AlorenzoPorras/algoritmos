def total_pressure(M1, M2, m1, m2, V, T):
    """
    Calcula la presión total ejercida por dos gases en un recipiente de acuerdo con la ecuación de gases ideales.

    :param M1: Masa molar del primer gas (g/mol)
    :param M2: Masa molar del segundo gas (g/mol)
    :param m1: Masa presente del primer gas (g)
    :param m2: Masa presente del segundo gas (g)
    :param V: Volumen del recipiente (dm^3)
    :param T: Temperatura en grados Celsius (°C)
    :return: La presión total en atm.
    """
    # Constante de los gases en atm·dm^3/(mol·K)
    R = 0.082

    # Convertir la temperatura de Celsius a Kelvin
    T_kelvin = T + 273.15

    # Aplicamos la fórmula: P_total = [(m1/M1) + (m2/M2)] * R * T / V
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_kelvin / V

    return P_total


# Ejemplos de uso
print(total_pressure(28, 32, 10, 15, 2, 25))  # Ejemplo de cálculo
print(total_pressure(44, 18, 5, 20, 10, 100))  # Otro ejemplo de cálculo
