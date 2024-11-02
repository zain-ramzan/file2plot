import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Global variables to store data after upload
uploaded_data = None
headers = None
plot_title = None

# Streamlit app
st.title("File 2 Plot")

# File upload
uploaded_file = st.file_uploader("Choose a .txt, .csv, or .xlsx file", type=["txt", "csv", "xlsx"])
if uploaded_file is not None:
    filename = uploaded_file.name
    plot_title = filename.split('.')[0]

    # Load data based on file type
    if filename.endswith('.txt'):
        headers = uploaded_file.readline().decode().strip().split(',')
        uploaded_data = np.genfromtxt(uploaded_file, delimiter=',', skip_header=1)

    elif filename.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
        headers = df.columns.tolist()
        uploaded_data = df.values

    elif filename.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
        headers = df.columns.tolist()
        uploaded_data = df.values

    # Show a preview of the data
    st.write("Data Preview:")
    # st.write(pd.DataFrame(uploaded_data, columns=headers))

    # Dropdowns for x and y axis selection
    x_axis = st.selectbox("Select X-axis", options=headers)
    y_axis = st.selectbox("Select Y-axis", options=headers)

    # Extract data for selected x and y headers
    x_index = headers.index(x_axis)
    y_index = headers.index(y_axis)
    x = uploaded_data[:, x_index]
    y = uploaded_data[:, y_index]

    # Generate and display plot directly with Streamlit
    st.write("Data Visualization:")
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    ax.set_title(plot_title or "Line Graph")
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    st.pyplot(fig)