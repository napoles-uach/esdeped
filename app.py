import streamlit as st

st.title('Calculadora de Puntuación para Beca')
'''### I. CALIDAD. Se otorgará un máximo de 700 puntos.
 1.Calidad en docencia. Puntuación máxima: 250 puntos'''
# Definiciones de puntos máximos y por actividad
max_puntos_docencia = 250 # Puntuaciion maxima, 1.0 Calidad en docencia
max_puntos_academico = 130  # Máximo para grado académico 1.1.1
max_puntos_actualizacion = 200  # Máximo total para actualización en el último año 1.1.2
max_puntos_cursoscudd = 30
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
#st.progress(puntos_grado_academico / max_puntos_academico)
st.progress(puntos_grado_academico / max_puntos_docencia)

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
#st.progress(puntos_por_cursos / max_puntos_capacitacion)
st.progress(puntos_por_cursos / max_puntos_docencia)

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
st.progress(puntos_por_cursos_disciplinares / max_puntos_docencia)

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
st.progress(puntos_por_eventos / max_puntos_docencia)

# Diplomado acreditado por el área pedagógica y/o disciplinar del docente
diplomado1 = st.checkbox('1.1.2.4 Diplomado 1 completado (20 puntos)')
diplomado2 = st.checkbox('1.1.2.4 Diplomado 2 completado (20 puntos)')
puntos_por_diplomados = (diplomado1 + diplomado2) * 20

with st.expander("Información sobre diplomados acreditados"):
    st.write("""
    Diplomado acreditado por el área pedagógica y/o disciplinar del docente. Deberá
    anexar comprobante del diplomado concluido durante el periodo enero-diciembre. Este
    diplomado deberá evidenciar la actualización en el área de formación profesional del docente
    (100 – 120 horas). Se otorgarán 20 puntos por diplomado, máximo 40 puntos.
    """)
st.progress(puntos_por_diplomados / max_puntos_docencia)

st.header("1.1.2.5 Estancias cortas autorizadas")

with st.expander("Información sobre Estancias cortas autorizadas"):
    st.write("""
    El docente deberá presentar tres documentos:
    ● Autorización por parte de la Secretaría Académica y/o de Investigación y Posgrado.
    ● Certificación de la estancia corta académica o de investigación de la institución receptora.
    Puntuación máxima: 200 puntos.
    """)

# Estancias nacionales
semanas_nacionales = st.slider('1.1.2.5.A Estancias nacionales (semanas)', 0, 10, 0)  # Asumiendo un máximo de 10 semanas para simplificar
puntos_nacionales = min(semanas_nacionales * 10, 100)

# Estancias internacionales
semanas_internacionales = st.slider('1.1.2.5.B Estancias internacionales (semanas)', 0, 7, 0)  # Asumiendo un máximo de 7 semanas para alcanzar 100 puntos
puntos_internacionales = min(semanas_internacionales * 15, 100)

# Muestra de puntos por estancias nacionales e internacionales y barras de progreso
#st.write(f"Puntos por estancias nacionales: {puntos_nacionales} de 100")
#st.progress(puntos_nacionales / max_puntos_docencia)
#st.write(f"Puntos por estancias internacionales: {puntos_internacionales} de 100")
#st.progress(puntos_internacionales / max_puntos_docencia)

# Cálculo del total de puntos en el rubro de estancias cortas autorizadas
total_puntos_estancias = puntos_nacionales + puntos_internacionales
#st.write(f"Total de puntos por estancias cortas autorizadas: {total_puntos_estancias} de 200")
st.progress(total_puntos_estancias / max_puntos_docencia)

st.header("1.1.4 Desarrollo de la docencia")

# 1.1.4.1 Material didáctico innovador
material_didactico = st.slider('1.1.4.1 Cantidad de materiales didácticos innovadores aprobados', 0, 4, 0)
puntos_material_didactico = min(material_didactico * 20, 80)

# 1.1.4.2 Software educativo
software_educativo = st.slider('1.1.4.2 Cantidad de software educativo aprobado', 0, 4, 0)
puntos_software_educativo = min(software_educativo * 20, 80)

# 1.1.4.3 Antologías, guías, manuales
antologias_guias_manuales = st.slider('1.1.4.3 Cantidad de antologías, guías, manuales aprobados', 0, 4, 0)
puntos_antologias_guias_manuales = min(antologias_guias_manuales * 20, 80)

# 1.1.4.4A Participación como instructor o profesor de cursos y/o talleres
# Asumimos un límite de 40 horas para simplificar, ajustando a 20 puntos máximo
horas_instructor = st.slider('1.1.4.4A Total de horas como instructor o profesor de cursos y/o talleres', 0, 40, 0)
puntos_instructor = min(horas_instructor, 20)  # 1 punto por hora, máximo 20 puntos

# 1.1.4.4B Participación como instructor o profesor de cursos y/o talleres
# Asumimos un límite de 40 horas para simplificar, ajustando a 20 puntos máximo
horas_instructorB = st.slider('1.1.4.4B Total de horas como instructor o profesor de cursos y/o talleres', 0, 40, 0)
puntos_instructorB = min(horas_instructorB, 20)  # 1 punto por hora, máximo 20 puntos

# 1.1.4.5 Elaboración de exámenes departamentales
examenes_departamentales = st.slider('1.1.4.5 Cantidad de exámenes departamentales elaborados', 0, 2, 0)
puntos_examenes_departamentales = min(examenes_departamentales * 10, 20)

# Mostrar los puntos obtenidos en cada subcategoría
#st.subheader("Puntos obtenidos en Desarrollo de la docencia")
#st.write(f"Puntos por material didáctico innovador: {puntos_material_didactico}")
#st.write(f"Puntos por software educativo: {puntos_software_educativo}")
#st.write(f"Puntos por antologías, guías, manuales: {puntos_antologias_guias_manuales}")
#st.write(f"Puntos por participación como instructor: {puntos_instructor}")
#st.write(f"Puntos por elaboración de exámenes departamentales: {puntos_examenes_departamentales}")

# Cálculo del total de puntos en el rubro Desarrollo de la docencia
total_puntos_desarrollo_docencia = puntos_material_didactico + puntos_software_educativo + puntos_antologias_guias_manuales + puntos_instructor+puntos_instructorB + puntos_examenes_departamentales
total_puntos_desarrollo_docencia=min(total_puntos_desarrollo_docencia,80)
st.write(f"Total de puntos en Desarrollo de la docencia: {total_puntos_desarrollo_docencia} de 80")
st.progress(total_puntos_desarrollo_docencia / 80)





# Cálculo del total de puntos en actualización
total_puntos_actualizacion = puntos_por_cursos + puntos_por_cursos_disciplinares + puntos_por_eventos + puntos_por_diplomados +total_puntos_estancias +total_puntos_desarrollo_docencia
st.write(f"Total de puntos en Actualización en el último año: {total_puntos_actualizacion} de {max_puntos_actualizacion}")
st.progress(total_puntos_actualizacion / max_puntos_actualizacion)



# Cálculo del total general y barra de progreso global
total_general = puntos_grado_academico + total_puntos_actualizacion
max_total_general = max_puntos_docencia #max_puntos_academico + max_puntos_actualizacion  # Ajusta según el máximo total de todos los rubros
st.header('Total de puntos obtenidos')
st.subheader(f'Total de puntos: {total_general} de {max_total_general}')
st.progress(total_general / max_total_general)

st.sidebar.write("# "+str(total_general)+'/'+ str(max_total_general))
st.sidebar.bar_chart([total_general,max_total_general])
