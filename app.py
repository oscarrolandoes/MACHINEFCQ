import streamlit as st
st.title("MI APLICACIÓN")
st.sidebar.header("ESTA APLICACIÓN ES SOLO UN DEMO")
st.sidebar.image("http://fcq.uach.mx/images/institucionales/Escudos/Dorado.png")
boton = st.button("globos")
if boton:
  st.balloons()
#comentario#