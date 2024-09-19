import pandas as pd
import numpy as np
import streamlit as st

# Show the page title and description.
st.title("Self Check 4")
st.write(
    """
    Edit the camera view
    """
)

if 'grid_width' not in st.session_state:
    st.session_state.grid_width = 4
if 'grid_height' not in st.session_state:
    st.session_state.grid_height = 4
    

with st.sidebar:
    container = st.container(border=True)
    container.title("Grid Size")

    container.write("Select a Width:")
    container.session_state.grid_width = st.number_input("", min_value=2, max_value=10, value=1, step=1, key="select_width")
 
    container.write("Select a Height:")
    container.session_state.grid_height = st.number_input("", min_value=2, max_value=10, value=1, step=1, key="select_height")
            
    submit = container.button("Submit")


if submit:
    init_data = np.random.rand(st.session_state.grid_height, st.session_state.grid_width)
    df = pd.DataFrame(init_data, columns=[f"Col {i}" for i in range(st.session_state.grid_width)])
    np.round(df, decimals=2)
    st.dataframe(df)

st.button("Display")


