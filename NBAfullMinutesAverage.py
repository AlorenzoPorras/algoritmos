def nba_extrap(ppg, mpg):
    """
    Calcula la extrapolación de los puntos por juego si un jugador jugara los 48 minutos completos.

    :param ppg: Puntos por juego actuales (en los minutos jugados).
    :param mpg: Minutos jugados por juego actualmente.
    :return: Puntos extrapolados por juego en 48 minutos, redondeados a un decimal.
    """
    # Si mpg es 0, retornamos 0 para evitar división por 0.
    if mpg == 0:
        return 0

    # Extrapolamos los puntos para 48 minutos.
    extrapolated_ppg = (ppg / mpg) * 48

    # Redondeamos el resultado a un decimal.
    return round(extrapolated_ppg, 1)


# Ejemplos de uso
print(nba_extrap(12, 20))  # Output: 28.8
print(nba_extrap(10, 10))  # Output: 48.0
print(nba_extrap(5, 17))  # Output: 14.1
print(nba_extrap(0, 0))  # Output: 0
