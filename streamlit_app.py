import pandas as pd
import numpy as np
import streamlit as st

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
    df = st.experimental_data_editor(df)
    st.session_state.dataframe = np.round(df, decimals=2)

with st.sidebar:
    container = st.container(border=True)
    container.title("Grid Size")

    col1, col2 = container.columns(2)

    with col1:
        container.write("Select a Width:")
        st.session_state.grid_width = container.number_input("", min_value=2, max_value=10, value=4, step=1, key="select_width", label_visibility="collapsed")

    with col2:
        container.write("Select a Height:")
        st.session_state.grid_height = container.number_input("", min_value=2, max_value=10, value=4, step=1, key="select_height", label_visibility="collapsed")
            
    submit = container.button("Submit", key="submit_button")


if submit:
    init_data = np.random.rand(st.session_state.grid_height, st.session_state.grid_width)
    df = pd.DataFrame(init_data, columns=[f"{i}" for i in range(st.session_state.grid_width)])
    df = st.experimental_data_editor(df)
    st.session_state.dataframe = np.round(df, decimals=2)

st.dataframe(st.session_state.dataframe)

st.button("Display")


