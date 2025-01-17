import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


# Sanity check for streamlit version
if st.__version__ != '1.29.0':
    st.warning(f"Warning: Streamlit version is {st.__version__}")

# Show the page title and description.
st.title("Self Check 4")
st.header(
    """
    Edit the camera view
    """
)

# Create initial grid height and width
if 'grid_width' not in st.session_state:
    st.session_state.grid_width = 4
if 'grid_height' not in st.session_state:
    st.session_state.grid_height = 4

# Initialize dataframe when starting up page using initial grid height and width
# Populate with random data
if 'dataframe' not in st.session_state:
    init_data = np.random.rand(st.session_state.grid_height, st.session_state.grid_width)
    df = pd.DataFrame(init_data, columns=[f"{i}" for i in range(st.session_state.grid_width)])
    st.session_state.dataframe = np.round(df, decimals=2)
    st.session_state.init_data = init_data

with st.sidebar:
    container = st.container(border=True)   #Unify all values in sidebar
    container.header("Grid Size")

    container.write("Select a Width:")
    st.session_state.grid_width = container.number_input("Select a Width", min_value=2, max_value=10, value=4, step=1, key="select_width", label_visibility="collapsed")

    container.write("Select a Height:")
    st.session_state.grid_height = container.number_input("Select a Height", min_value=2, max_value=10, value=4, step=1, key="select_height", label_visibility="collapsed")
            
    submit = container.button("Submit", key="submit_button")

# Display randomized data based on user input for table height and width
if submit:
    init_data = np.random.rand(st.session_state.grid_height, st.session_state.grid_width)
    df = pd.DataFrame(init_data, columns=[f"{i}" for i in range(st.session_state.grid_width)])
    st.session_state.dataframe = np.round(df, decimals=2)
    st.session_state.init_data = init_data

# Make data editable and reflect on display
st.session_state.dataframe = st.data_editor(st.session_state.dataframe)
st.session_state.init_data = st.session_state.dataframe.values

display = st.button("Display")

if display:

    init_data = st.session_state.get('init_data')

    # Plotting based off module 2
    if init_data is not None:

        figure = plt.figure(figsize = (4, 4))
        axes = figure.add_subplot(1, 1, 1)

        pixels = np.array([255 - p * 255 for p in init_data], dtype='uint8')
        pixels = pixels.reshape((st.session_state.grid_height, st.session_state.grid_width))

        axes.set_title( "Camera View")
        axes.imshow(pixels, cmap='gray')

        axes.set_xticks(np.arange(0, st.session_state.grid_width, 2))
        axes.set_yticks(np.arange(0, st.session_state.grid_height, 2))

        st.pyplot(figure)

    # Debugging check if data processed
    else:
        st.error("Please press submit before attempting to display data.")

