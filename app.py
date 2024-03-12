import streamlit as st

st.title('Calculadora de Puntuación para Beca')

# Definiciones de puntos máximos y por actividad
max_puntos_academico = 130  # Máximo para grado académico
max_puntos_capacitacion = 30  # Máximo para capacitación pedagógica
max_puntos_disciplinar = 15  # Máximo para área disciplinar
max_puntos_eventos = 12  # Máximo para asistencia a eventos
puntos_por_evento = 3  # Puntos otorgados por evento asistido
max_puntos_diplomados = 40  # Máximo para diplomados acreditados

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

# Cursos o talleres del área disciplinar
cursos_disciplinares_completados = st.slider('1.1.2.2 Cursos o talleres del área disciplinar completados (horas)', 0, 30, 0, 1)
puntos_por_cursos_disciplinares = min(0.5 * cursos_disciplinares_completados, max_puntos_disciplinar)

with st.expander("Información sobre cursos del área disciplinar"):
    st.write("""
    Se tomarán en cuenta los cursos o talleres en el área disciplinar del docente cuyo comprobante esté fechado dentro del periodo enero-
    diciembre por el cual concursa. No se tomarán en cuenta cursos que formen parte de un
    Doctorado, Maestría, Especialidad o Diplomado. Se otorgará 0.5 puntos por cada hora y en caso
    de no estar asentado el número de horas se considerarán 3 horas por día. El puntaje máximo a
    considerar para el rubro de área disciplinar es de 15 puntos.
    """)

# Asistencia a eventos profesionales
eventos_asistidos = st.slider('1.1.2.3 Cantidad de eventos profesionales asistidos', 0, 4, 0)  # Asumiendo un máximo de 4 eventos para simplificar
puntos_por_eventos = min(eventos_asistidos * puntos_por_evento, max_puntos_eventos)

with st.expander("Información sobre asistencia a eventos profesionales"):
    st.write("""
    Deberá presentar comprobantes de asistencia a Seminarios, Coloquios, Congresos y Simposios expedidos durante el periodo enero-diciembre
    por el cual concursa. Para el caso de los eventos académicos antes mencionados, éstos deberán
    ser previamente avalados o registrados ante la Dirección Académica y/o el Centro Universitario
    para el Desarrollo Docente. Se otorgarán 3 puntos por evento, máximo 12 puntos.
    """)

# Diplomado acreditado por el área pedagógica y/o disciplinar del docente
diplomado1 = st.checkbox('1.1.2.4 Diplomado 1 completado (20 puntos)')
diplomado2 = st.checkbox('Diplomado 2 completado (20 puntos)')
puntos_por_diplomados = (diplomado1 + diplomado2) * 20

with st.expander("Información sobre diplomados acreditados"):
    st.write("""
    Diplomado acreditado por el área pedagógica y/o disciplinar del docente. Deberá
    anexar comprobante del diplomado concluido durante el periodo enero-diciembre. Este
    diplomado deberá evidenciar la actualización en el área de formación profesional del docente
    (100 – 120 horas). Se otorgarán 20 puntos por diplomado, máximo 40 puntos.
    """)

# Muestra de resultados
st.header('Total de puntos obtenidos')
total_puntos = puntos_grado_academico + puntos_por_cursos + puntos_por_cursos_disciplinares + puntos_por_eventos + puntos_por_diplomados
st.subheader(f'Total de puntos: {total_puntos}')


