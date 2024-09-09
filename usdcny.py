# Función para convertir USD a CNY
def convert_usd_to_cny(usd, conversion_rate=6.75):
    """
    Convierte una cantidad en USD a CNY usando una tasa de conversión proporcionada.
    Si la cantidad no es válida o negativa, devuelve un mensaje de error.

    :param usd: Monto en USD (debe ser un número entero o decimal positivo)
    :param conversion_rate: Tasa de conversión de USD a CNY (opcional, por defecto 6.75)
    :return: Una cadena de texto con el valor convertido a CNY o un mensaje de error
    """
    try:
        # Verificar si la cantidad es positiva
        if usd < 0:
            return "Error: La cantidad no puede ser negativa."

        # Convertir a yuanes chinos
        cny = usd * conversion_rate

        # Devolver la cadena formateada con dos decimales
        return f"{cny:.2f} Chinese Yuan"

    except TypeError:
        return "Error: La cantidad debe ser un número."


# Función principal para interactuar con el usuario
def main():
    print("Bienvenido al convertidor de USD a CNY")

    # Bucle principal para permitir varias conversiones
    while True:
        # Capturar la entrada del usuario
        usd_input = input("Ingrese la cantidad en USD (o 'salir' para terminar): ")

        if usd_input.lower() == 'salir':
            print("Gracias por usar el convertidor. ¡Adiós!")
            break

        try:
            # Intentar convertir la entrada a un número float
            usd_amount = float(usd_input)

            # Llamar a la función de conversión y mostrar el resultado
            result = convert_usd_to_cny(usd_amount)
            print(result)

        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

        # Ofrecer la opción de cambiar la tasa de conversión
        change_rate = input("¿Desea cambiar la tasa de conversión actual (6.75)? (sí/no): ").lower()
        if change_rate == 'sí':
            try:
                new_rate = float(input("Ingrese la nueva tasa de conversión (CNY por 1 USD): "))
                result = convert_usd_to_cny(usd_amount, new_rate)
                print(f"Con la nueva tasa de conversión: {result}")
            except ValueError:
                print("Error: Tasa de conversión no válida, usando la tasa por defecto.")


if __name__ == "__main__":
    main()
