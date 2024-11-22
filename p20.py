import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde el archivo CSV
data = pd.read_csv('datos_salud_publica.csv')

# Agrupar por 'Sexo' y 'Enfermedad' y contar el número de casos
grupo_enfermedad = data.groupby(['Sexo', 'Enfermedad']).size().reset_index(name='Cantidad')

# Calcular el total por grupo de sexo
total_por_sexo = data.groupby('Sexo').size().reset_index(name='Total')


resultado = pd.merge(grupo_enfermedad, total_por_sexo, on='Sexo')
resultado['Porcentaje'] = (resultado['Cantidad'] / resultado['Total']) * 100


print(resultado)


plt.figure(figsize=(10, 6))
sns.barplot(data=resultado, x='Enfermedad', y='Porcentaje', hue='Sexo')
plt.title('Porcentaje de Enfermedades por Sexo')
plt.ylabel('Porcentaje')
plt.xlabel('Enfermedad')
plt.legend(title='Sexo')
plt.xticks(rotation=45)
plt.tight_layout()  
plt.show()