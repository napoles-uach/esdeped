import streamlit as st

# Títulos y subtítulos
st.title('Calculadora de Puntuación para Beca')
st.header('Ingresar los puntos obtenidos en cada categoría')

# Máximos puntos por categoría
max_puntos_docencia = 250
max_puntos_actualizacion = 200

# Entrada de usuario para puntos actuales
puntos_docencia = st.number_input('Puntos en Calidad en Docencia', min_value=0, max_value=max_puntos_docencia, value=0, step=1)
puntos_actualizacion = st.number_input('Puntos en Actualización en el Último Año', min_value=0, max_value=max_puntos_actualizacion, value=0, step=1)

# Cálculo de puntos faltantes
faltan_docencia = max_puntos_docencia - puntos_docencia
faltan_actualizacion = max_puntos_actualizacion - puntos_actualizacion

# Visualización de resultados
st.subheader('Resultados')
st.write(f'### Puntos faltantes para alcanzar el máximo en Calidad en Docencia: {faltan_docencia}')
st.write(f'### Puntos faltantes para alcanzar el máximo en Actualización en el Último Año: {faltan_actualizacion}')

# Visualización gráfica (opcional)
st.bar_chart({"Puntos Obtenidos": [puntos_docencia, puntos_actualizacion], "Puntos Faltantes": [faltan_docencia, faltan_actualizacion]}, use_container_width=True)
