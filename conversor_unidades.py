# Programa que convierte unidades de longitud, masa y temperatura.
# El usuario puede elegir entre diferentes tipos de conversión y el programa
# mostrará el resultado de manera clara. Se usan funciones, tipos de datos variados,
# identificadores descriptivos y comentarios explicativos.

# Función para convertir metros a centímetros
def metros_a_centimetros(metros: float) -> float:
    """Convierte metros a centímetros."""
    return metros * 100

# Función para convertir kilogramos a gramos
def kilogramos_a_gramos(kilogramos: float) -> float:
    """Convierte kilogramos a gramos."""
    return kilogramos * 1000

# Función para convertir grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9 / 5) + 32

# Programa principal
print("==== Conversor de Unidades ====")
print("1. Metros a Centímetros")
print("2. Kilogramos a Gramos")
print("3. Celsius a Fahrenheit")

# Solicita al usuario que elija una opción
opcion: int = int(input("Seleccione una opción (1, 2 o 3): "))

# Verifica la opción y realiza la conversión correspondiente
if opcion == 1:
    valor_metros: float = float(input("Ingrese la cantidad en metros: "))
    resultado: float = metros_a_centimetros(valor_metros)
    print(f"{valor_metros} metros = {resultado} centímetros")

elif opcion == 2:
    valor_kilogramos: float = float(input("Ingrese la cantidad en kilogramos: "))
    resultado: float = kilogramos_a_gramos(valor_kilogramos)
    print(f"{valor_kilogramos} kilogramos = {resultado} gramos")

elif opcion == 3:
    valor_celsius: float = float(input("Ingrese la temperatura en grados Celsius: "))
    resultado: float = celsius_a_fahrenheit(valor_celsius)
    print(f"{valor_celsius}°C = {resultado:.2f}°F")

else:
    print("Opción inválida. Por favor seleccione 1, 2 o 3.")