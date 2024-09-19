import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image


if st.__version__ != '1.29.0':
    st.warning(f"Warning: Streamlit version is {st.__version__}")

# Show the page title and description.
st.title("Self Check 4")
st.header(
    """
    Edit the camera view
    """
)

if 'grid_width' not in st.session_state:
    st.session_state.grid_width = 4
if 'grid_height' not in st.session_state:
    st.session_state.grid_height = 4


if 'dataframe' not in st.session_state:
    init_data = np.random.rand(st.session_state.grid_height, st.session_state.grid_width)
    df = pd.DataFrame(init_data, columns=[f"{i}" for i in range(st.session_state.grid_width)])
    st.session_state.dataframe = np.round(df, decimals=2)
    st.session_state.init_data = init_data


with st.sidebar:
    container = st.container(border=True)
    container.header("Grid Size")

    col1, col2 = container.columns(2)

    with col1:
        container.write("Select a Width:")
        st.session_state.grid_width = container.number_input("Select a Width", min_value=2, max_value=10, value=4, step=1, key="select_width", label_visibility="collapsed")

    with col2:
        container.write("Select a Height:")
        st.session_state.grid_height = container.number_input("Select a Height", min_value=2, max_value=10, value=4, step=1, key="select_height", label_visibility="collapsed")
            
    submit = container.button("Submit", key="submit_button")


if submit:
    init_data = np.random.rand(st.session_state.grid_height, st.session_state.grid_width)
    df = pd.DataFrame(init_data, columns=[f"{i}" for i in range(st.session_state.grid_width)])
    st.session_state.dataframe = np.round(df, decimals=2)
    st.session_state.init_data = init_data


st.data_editor(st.session_state.dataframe)

display = st.button("Display")

if display:

    init_data = st.session_state.get('init_data')

    if init_data is not None:

        figure = plt.figure(figsize = (4, 4))
        axes = figure.add_subplot(1, 1, 1)

        pixels = np.array([255 - p * 255 for p in init_data], dtype='uint8')
        pixels = pixels.reshape((st.session_state.grid_height, st.session_state.grid_width))

        axes.set_title( "Camera View")
        axes.imshow(pixels, cmap='gray')

        axes.set_xticks(np.arange(0, st.session_state.grid_width, 2))
        axes.set_yticks(np.arange(0, st.session_state.grid_height, 2))


        #st.pyplot(figure)
        figure.savefig("data_grid.png")
        data_grid = Image.open('data_grid.png')
        st.image(data_grid)

    else:
        st.error("Please press submit before attempting to display data.")

