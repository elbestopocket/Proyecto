from tabulate import tabulate
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
# Información sobre las enfermedades
enfermedades = {
    "diabetes": {
        "Nombre": "Diabetes",
        "Causa": "Insuficiencia de insulina o resistencia a la insulina",
        "Síntomas": "Sed excesiva, micción frecuente, hambre extrema, pérdida de peso",
        "Diagnóstico": "Pruebas de glucosa en sangre, A1C",
        "Tratamiento": "Insulina, medicamentos, dieta, ejercicio"
    },
    "hipertension": {
        "Nombre": "Hipertensión",
        "Causa": "Genética, dieta, estilo de vida, condiciones médicas subyacentes",
        "Síntomas": "Generalmente asintomática, dolores de cabeza, dificultad para respirar",
        "Diagnóstico": "Medición de la presión arterial",
        "Tratamiento": "Medicamentos, dieta baja en sal, ejercicio, control del estrés"
    },
    "leucemia": {
        "Nombre": "Leucemia",
        "Causa": "Mutaciones genéticas, factores ambientales",
        "Síntomas": "Fiebre, fatiga, moretones fáciles, pérdida de peso",
        "Diagnóstico": "Análisis de sangre, biopsia de médula ósea",
        "Tratamiento": "Quimioterapia, radioterapia, trasplante de médula ósea"
    }
}

# Función para mostrar la información en una tabla
def mostrar_informacion(enfermedad):
    if enfermedad in enfermedades:
        data = [[key, value] for key, value in enfermedades[enfermedad].items()]
        print(tabulate(data, headers=["Campo", "Descripción"], tablefmt="grid"))
    else:
        print("Enfermedad no encontrada. Por favor, elige entre: diabetes, hipertension, leucemia.")

# Solicitar al usuario que elija una enfermedad
enfermedad_elegida = input("Elige una enfermedad (diabetes, hipertension, leucemia): ").lower()
mostrar_informacion(enfermedad_elegida)
