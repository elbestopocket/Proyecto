import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    return riesgo, edad_normalizada

# Función para mostrar estadísticas de la enfermedad
def mostrar_estadisticas(data, enfermedad):
    # Agrupar por 'Sexo' y 'Enfermedad' y contar el número de casos
    grupo_enfermedad = data.groupby(['Sexo', 'Enfermedad']).size().reset_index(name='Cantidad')

    # Calcular el total por grupo de sexo
    total_por_sexo = data.groupby('Sexo').size().reset_index(name='Total')

    resultado = pd.merge(grupo_enfermedad, total_por_sexo, on='Sexo')
    resultado['Porcentaje'] = (resultado['Cantidad'] / resultado['Total']) * 100

    # Mostrar estadísticas
    print("\nEstadísticas para la enfermedad:", enfermedad)
    print(resultado[resultado['Enfermedad'] == enfermedad])

    # Visualización
    plt.figure(figsize=(10, 6))
    sns.barplot(data=resultado[resultado['Enfermedad'] == enfermedad], x='Sexo', y='Porcentaje')
    plt.title(f'Porcentaje de {enfermedad} por Sexo')
    plt.ylabel('Porcentaje')
    plt.xlabel('Sexo')
    plt.xticks(rotation=45)
    plt.tight_layout()  
    plt.show()

# Interacción con el usuario
print("Bienvenido al sistema de predicción de riesgos de enfermedades.")
print("Puedes ingresar cualquier edad.")
print("Las enfermedades disponibles son: diabetes, hipertensión, gripe_estacional, dengue")

while True:
    edad = input("\nIngresa tu edad: ").strip()
    enfermedad = input("Ingresa la enfermedad de interés: ").strip().lower()
    
    riesgo, edad_normalizada = predecir_riesgo(edad, enfermedad)
    print(f"\nEl riesgo de {enfermedad} para la población de edad {edad_normalizada} es de {riesgo * 100:.2f}%.")

    # Cargar los datos desde el archivo CSV
    try:
        data = pd.read_csv('datos_salud_publica.csv')
        mostrar_estadisticas(data, enfermedad)
    except FileNotFoundError:
        print("El archivo 'datos_salud_publica.csv' no se encontró. Asegúrate de que el archivo esté en el mismo directorio que este script.")
        break

    # Validar respuesta para continuar
    while True:
        continuar = input("\n¿Deseas analizar otra enfermedad? (sí/no): ").strip().lower()
        if continuar in ["si", "no"]:
            break
        print("Por favor, responde con 'sí' o 'no'.")

    if continuar == "no":
        print("Gracias por usar el sistema. ¡Cuídate!")
        break