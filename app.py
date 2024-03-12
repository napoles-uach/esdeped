import streamlit as st

st.title('Calculadora de Puntuación para Beca')
'''# I. CALIDAD. Se otorgará un máximo de 700 puntos.
# 1.Calidad en docencia. Puntuación máxima: 250 puntos'''
# Definiciones de puntos máximos y por actividad
max_puntos_docencia = 250 # Puntuaciion maxima, 1.0 Calidad en docencia
max_puntos_academico = 130  # Máximo para grado académico 1.1.1
max_puntos_actualizacion = 200  # Máximo total para actualización en el último año 1.1.2
max_puntos_cursoscudd = 30
max_puntos_capacitacion = 30  # Máximo para capacitación pedagógica

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

# Actualización en el último año
st.header("1.1.2 Actualización en el último año")

# Cursos de formación docente y/o actualización pedagógica
cursos_completados = st.slider('1.1.2.1 Cursos de formación docente y/o actualización pedagógica completados (horas)', 0, 60, 0, 1)
puntos_por_cursos = min(0.5 * cursos_completados, max_puntos_capacitacion)

with st.expander("Información sobre cursos de formación docente"):
    st.write("""
    Se tomarán en cuenta los cursos o talleres cuyo comprobante esté fechado dentro del periodo
    enero-diciembre por el cual concursa. No se tomarán en cuenta cursos que formen parte de un
    Doctorado, Maestría, Especialidad o Diplomado. Se otorgará 0.5 puntos por cada hora y en caso
    de no estar asentado el número de horas se considerarán 3 horas por día. El puntaje máximo a
    considerar para el rubro de capacitación pedagógica es de 30 puntos.
    """)
st.progress(puntos_por_cursos / max_puntos_capacitacion)

# Cálculo del total de puntos en actualización
total_puntos_actualizacion = puntos_por_cursos + puntos_por_cursos_disciplinares + puntos_por_eventos + puntos_por_diplomados
st.write(f"Total de puntos en Actualización en el último año: {total_puntos_actualizacion} de {max_puntos_actualizacion}")
st.progress(total_puntos_actualizacion / max_puntos_actualizacion)

# Cálculo del total general y barra de progreso global
total_general = puntos_grado_academico + total_puntos_actualizacion
max_total_general = max_puntos_docencia #max_puntos_academico + max_puntos_actualizacion  # Ajusta según el máximo total de todos los rubros
st.header('Total de puntos obtenidos')
st.subheader(f'Total de puntos: {total_general} de {max_total_general}')
st.progress(total_general / max_total_general)


