import streamlit as st

st.title('Calculadora de Puntuación para Beca')

# Definiciones de puntos máximos y por actividad
max_puntos_academico = 130  # Máximo para grado académico
max_puntos_actualizacion = 200  # Máximo total para actualización en el último año

# Grado Académico
st.header("1.1.1 Grado Académico")
grado_academico = st.selectbox('Selecciona tu grado académico máximo',
                               ['Ninguno', 'Licenciatura', 'Maestría', 'Doctorado'],
                               index=0)
puntos_grado_academico = 0
if grado_academico == 'Licenciatura':
    puntos_grado_academico = 100
elif grado_academico == 'Maestría':
    puntos_grado_academico = 100
elif grado_academico == 'Doctorado':
    puntos_grado_academico = 130

with st.expander("Información sobre Grado Académico"):
    st.write("""
    Se considera sólo el grado máximo de estudios, por lo que deberá presentar el Título del máximo
    grado de estudios. No se aceptarán Actas de Examen. Máximo 130 puntos.
    """)
st.progress(puntos_grado_academico / max_puntos_academico)

# Actualización en el último año: Resumen de subsecciones
st.header("1.1.2 Actualización en el último año")
total_puntos_actualizacion = 0  # Inicialización del total de puntos en actualización

# Subsecciones de Actualización
# Variables para cada subsección con valores por defecto
puntos_por_cursos = 0
puntos_por_cursos_disciplinares = 0
puntos_por_eventos = 0
puntos_por_diplomados = 0

# Implementación de cada subsección...

# Cálculo y muestra de puntos por subsección
# Ejemplo para cursos de formación docente:
# puntos_por_cursos = <cálculo según la entrada del usuario>
# st.progress(puntos_por_cursos / max_puntos_subsección)

# Cálculo del total de puntos en actualización
total_puntos_actualizacion = puntos_por_cursos + puntos_por_cursos_disciplinares + puntos_por_eventos + puntos_por_diplomados
st.write(f"Total de puntos en Actualización en el último año: {total_puntos_actualizacion} de {max_puntos_actualizacion}")
st.progress(total_puntos_actualizacion / max_puntos_actualizacion)

# Cálculo del total general y barra de progreso global
total_general = puntos_grado_academico + total_puntos_actualizacion
max_total_general = max_puntos_academico + max_puntos_actualizacion  # Ajusta según el máximo total de todos los rubros
st.header('Total de puntos obtenidos')
st.subheader(f'Total de puntos: {total_general} de {max_total_general}')
st.progress(total_general / max_total_general)


