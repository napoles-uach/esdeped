import streamlit as st

st.title('Calculadora de Puntuación para Beca')

# Sección de Actualización en el último año con Expanders
with st.expander("1.1.2 Actualización en el último año"):
    max_puntos_capacitacion = 30  # Máximo para capacitación pedagógica
    max_puntos_eventos = 12  # Máximo para asistencia a eventos
    puntos_por_evento = 3  # 3 puntos por evento
    max_puntos_diplomados = 40  # Máximo para diplomados

    # Cursos de formación docente y/o actualización pedagógica
    st.subheader('1.1.2.1 Cursos de formación docente y/o actualización pedagógica')
    curso1 = st.checkbox('Curso 1 (10 puntos)')
    curso2 = st.checkbox('Curso 2 (10 puntos)')
    curso3 = st.checkbox('Curso 3 (10 puntos)')
    puntos_por_cursos = (curso1 + curso2 + curso3) * 10

    # Asistencia a eventos profesionales
    st.subheader('1.1.2.3 Asistencia a eventos profesionales')
    eventos_asistidos = st.slider('Cantidad de eventos profesionales asistidos', 0, 4, 0)  # Hasta 4 eventos, dado el máximo de 12 puntos
    puntos_por_eventos = min(eventos_asistidos * puntos_por_evento, max_puntos_eventos)

    # Diplomado acreditado
    st.subheader('1.1.2.4 Diplomado acreditado por el área pedagógica y/o disciplinar del docente')
    diplomado1 = st.checkbox('Diplomado 1 (20 puntos)')
    diplomado2 = st.checkbox('Diplomado 2 (20 puntos)')
    puntos_por_diplomados = (diplomado1 + diplomado2) * 20

    # Muestra de resultados
    st.write(f'Puntos obtenidos por cursos: {puntos_por_cursos}')
    st.write(f'Puntos obtenidos por asistencia a eventos: {puntos_por_eventos}')
    st.write(f'Puntos obtenidos por diplomados: {puntos_por_diplomados}')
    total_puntos_actualizacion = puntos_por_cursos + puntos_por_eventos + puntos_por_diplomados
    st.write(f'Total de puntos obtenidos en Actualización: {total_puntos_actualizacion}')

    # Visualización gráfica
    if total_puntos_actualizacion > 0:
        st.progress(total_puntos_actualizacion / (max_puntos_capacitacion + max_puntos_eventos + max_puntos_diplomados))
    else:
        st.write("No has seleccionado ninguna opción aún.")


