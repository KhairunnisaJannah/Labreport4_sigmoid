import matplotlib
matplotlib.use("Agg")  # Required for Streamlit Cloud

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Sigmoid Activation Function")

# Data
x = np.linspace(-5, 5, 50)
z = 1 / (1 + np.exp(-x))

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, z)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("Sigmoid Function")
ax.grid()

# Display in Streamlit
st.pyplot(fig)
