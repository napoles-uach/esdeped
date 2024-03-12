import streamlit as st

st.title('Calculadora de Puntuación para Beca')

# Sección de Actualización en el último año
st.header("1.1.2 Actualización en el último año")

# Cursos de formación docente y/o actualización pedagógica
st.subheader('1.1.2.1 Cursos de formación docente y/o actualización pedagógica')
curso1 = st.checkbox('Curso 1 (10 puntos)')
curso2 = st.checkbox('Curso 2 (10 puntos)')
curso3 = st.checkbox('Curso 3 (10 puntos)')
puntos_por_cursos = (curso1 + curso2 + curso3) * 10

# Asistencia a eventos profesionales
st.subheader('1.1.2.3 Asistencia a eventos profesionales')
eventos_asistidos = st.slider('Cantidad de eventos profesionales asistidos', 0, 4, 0)
puntos_por_eventos = min(eventos_asistidos * puntos_por_evento, max_puntos_eventos)

# Diplomado acreditado por el área pedagógica y/o disciplinar del docente
st.subheader('1.1.2.4 Diplomado acreditado')
diplomado1 = st.checkbox('Diplomado 1 (20 puntos)')
diplomado2 = st.checkbox('Diplomado 2 (20 puntos)')
puntos_por_diplomados = (diplomado1 + diplomado2) * 20

with st.expander("Información sobre diplomados acreditados"):
    st.write("""
    Diplomado acreditado por el área pedagógica y/o disciplinar del docente. Deberá
    anexar comprobante del diplomado concluido durante el periodo enero-diciembre. Este
    diplomado deberá evidenciar la actualización en el área de formación profesional del docente
    (100 – 120 horas). Se otorgarán 20 puntos por diplomado, máximo 40 puntos.
    """)

# Muestra de resultados
total_puntos_actualizacion = puntos_por_cursos + puntos_por_eventos + puntos_por_diplomados
st.subheader('Total de puntos obtenidos en Actualización')
st.write(f'Total de puntos: {total_puntos_actualizacion}')

# Visualización gráfica
if total_puntos_actualizacion > 0:
    st.progress(total_puntos_actualizacion / (max_puntos_capacitacion + max_puntos_eventos + max_puntos_diplomados))
else:
    st.write("No has seleccionado ninguna opción aún.")


