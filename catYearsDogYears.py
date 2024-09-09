#Calcula la edad del perro y gato en años humanos
def calculate_pet_ages(humanYears):
    # Calcular los años de los gatos
    if humanYears == 1:
        catYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4

    # Calcular los años de los perros
    if humanYears == 1:
        dogYears = 15
    elif humanYears == 2:
        dogYears = 15 + 9
    else:
        dogYears = 15 + 9 + (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]


# Ejemplo de uso:
#humanYears = 15
humanYears = int(input("Dame los años humanos "))

ages = calculate_pet_ages(humanYears)
# print(ages)

#imprime las edades formateadas
print(f"Un animal con {ages[0]} años humanos tendria: ")
print(f"- {ages[1]} años de gato ")
print(f"- {ages[2]} años de perro ")

#imrpime el tipo de dato devuelto por la funcion
print(f"El tipo de dato devuelto es {type(ages)}")

#imprime el tipo de datos de vuelta por la funcion
#print(type(ages))


# print(calculate_pet_ages(1))  # Output: [1, 15, 15]
