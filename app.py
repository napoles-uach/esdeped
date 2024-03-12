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

# Configuraciones para la sección de Actualización en el último año
max_puntos_capacitacion = 30  # Máximo para capacitación pedagógica
max_puntos_eventos = 12  # Máximo para asistencia a eventos
puntos_por_evento = 3  # 3 puntos por evento

st.header('Actualización en el último año')

# Cursos de formación docente y/o actualización pedagógica
st.subheader('Cursos de formación docente y/o actualización pedagógica')
curso1 = st.checkbox('Curso 1 (10 puntos)')
curso2 = st.checkbox('Curso 2 (10 puntos)')
curso3 = st.checkbox('Curso 3 (10 puntos)')

# Cálculo de puntos obtenidos por cursos
puntos_por_cursos = (curso1 + curso2 + curso3) * 10

# Asistencia a eventos profesionales
st.subheader('Asistencia a eventos profesionales')
eventos_asistidos = st.slider('Cantidad de eventos profesionales asistidos', 0, 4, 0)  # Hasta 4 eventos, dado el máximo de 12 puntos
puntos_por_eventos = min(eventos_asistidos * puntos_por_evento, max_puntos_eventos)

# Muestra de resultados
st.subheader('Puntuación por Actualización en el Último Año')
st.write(f'Puntos obtenidos por cursos: {puntos_por_cursos}')
st.write(f'Puntos obtenidos por asistencia a eventos: {puntos_por_eventos}')
total_puntos_actualizacion = puntos_por_cursos + puntos_por_eventos
st.write(f'Total de puntos obtenidos en Actualización: {total_puntos_actualizacion}')

# Visualización gráfica
if total_puntos_actualizacion > 0:
    st.progress(total_puntos_actualizacion / (max_puntos_capacitacion + max_puntos_eventos))
else:
    st.write("No has seleccionado ninguna opción aún.")

# Explicación de la visualización
st.text("La barra muestra la proporción del total de puntos obtenidos en Actualización respecto a los puntos máximos posibles.")
