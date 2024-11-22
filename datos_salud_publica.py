import pandas as pd
import random

# Configuración de los datos
n = 1000  # Número de registros
edades = [random.randint(18, 90) for _ in range(n)]
sexos = [random.choice(['M', 'F']) for _ in range(n)]
historial_medico = [random.choice(['Sí', 'No']) for _ in range(n)]
enfermedades = [
    'Diabetes',
    'Hipertensión',
    'Cáncer',
    'Enfermedad Cardiaca',
    'Asma',
    'Artritis',
    'Enfermedad Pulmonar Crónica',
    'Accidente Cerebrovascular',
    'Obesidad',
    'Enfermedad Renal Crónica'
]

# Generar enfermedades aleatorias para cada paciente
enfermedades_asignadas = [random.choice(enfermedades) for _ in range(n)]

# Crear un DataFrame
data = pd.DataFrame({
    'Edad': edades,
    'Sexo': sexos,
    'Historial Médico': historial_medico,
    'Enfermedad': enfermedades_asignadas
})

# Guardar a un archivo CSV
data.to_csv('datos_salud_publica.csv', index=False)

print("Archivo 'datos_salud_publica.csv' generado con éxito.")