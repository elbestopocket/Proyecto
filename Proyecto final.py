import pandas as pd

# Base de datos simulada
data = {
    "edad": ["<18", "18-35", "36-60", ">60"],
    "diabetes": [0.1, 0.2, 0.4, 0.7],
    "hipertensión": [0.05, 0.2, 0.5, 0.8],
    "gripe_estacional": [0.3, 0.4, 0.5, 0.6],
    "dengue": [0.4, 0.6, 0.3, 0.1]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Función para determinar el rango de edad
def clasificar_edad(edad):
    try:
        edad = int(edad)
        if edad < 18:
            return "<18"
        elif 18 <= edad <= 35:
            return "18-35"
        elif 36 <= edad <= 60:
            return "36-60"
        else:
            return ">60"
    except ValueError:
        return None

# Función para predecir enfermedades
def predecir_riesgo(edad, enfermedad):
    # Clasificar la edad
    edad_normalizada = clasificar_edad(edad)
    if not edad_normalizada:
        return "Edad no válida. Por favor, ingresa un número positivo."

    # Validar entrada de enfermedad
    if enfermedad not in df.columns:
        return "Enfermedad no válida. Elige entre: diabetes, hipertensión, gripe_estacional, dengue."

    # Calcular riesgo
    riesgo = df[df["edad"] == edad_normalizada][enfermedad].values[0]
    return f"El riesgo de sufrir {enfermedad} para la población de edad {edad_normalizada} es del {riesgo * 100:.2f}%."

# Interacción con el usuario
print(
"""
+================================+
|   ¡Bienvenido al software de   |
|   predicción de enfermedades   |
|       del grupo número 5!      |
|    Aquí consultarás ciertas    |
|    enfermedades de interés     |
|    A continuación, ingresa:    |
+================================+
""")
print("Puedes consultar sobre las siguientes enfermedades: \n1. Diabetes \n2. Hipertensión \n3. Gripe común \n4. Dengue")

while True:
    edad = input("\nIngresa tu edad: ").strip()
    enfermedad = input("Ingresa la enfermedad que deseas consultar: ").strip().lower()
    resultado = predecir_riesgo(edad, enfermedad)
    print("\n" + resultado)
    
    # Validar respuesta para continuar
    while True:
        continuar = input("\n¿Deseas consultar sobre alguna otra enfermedad disponible? (sí/no): ").strip().lower()
        if continuar in ["si", "no"]:
            break
        print("Por favor, responde con 'si' o 'no'.")

    if continuar == "no":
        print("Gracias por usar el sistema. ¡Recuerda, la calidad de tu salud depende de tus acciones, así que cuídate!")
        break