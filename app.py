import streamlit as st

st.title('Calculadora de Puntuación para Beca')

# Definición de los máximos puntos por categoría y grado
max_puntos_grado = 130  # Máximo para cualquier grado
puntos_maestria = 100
puntos_especialidad = 100
puntos_doctorado = 130

# Checkbox para seleccionar el grado académico
st.header('Grado Académico')
maestria = st.checkbox('Maestría')
especialidad = st.checkbox('Especialidad')
doctorado = st.checkbox('Doctorado')

# Lógica para asignar puntos según el grado seleccionado
if maestria:
    puntos_obtenidos = puntos_maestria
elif especialidad:
    puntos_obtenidos = puntos_especialidad
elif doctorado:
    puntos_obtenidos = puntos_doctorado
else:
    puntos_obtenidos = 0  # Si no se selecciona ningún grado

# Visualización de los puntos
st.subheader('Puntuación por Grado Académico')
st.write(f'Puntos obtenidos: {puntos_obtenidos}')
st.write(f'Puntos máximos posibles: {max_puntos_grado}')

# Visualización gráfica de los puntos
st.progress(puntos_obtenidos / max_puntos_grado)

# Explicación de la visualización
st.text("La barra muestra la proporción de puntos obtenidos respecto a los puntos máximos posibles.")
