import streamlit as st
import matplotlib.pyplot as plt

st.title('Prueba de Matplotlib')

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
st.pyplot(fig)