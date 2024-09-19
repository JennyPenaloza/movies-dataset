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
    st.session_state.grid_width = 3
if 'grid_height' not in st.session_state:
    st.session_state.grid_height = 3
    

with st.sidebar:
    st.title("Grid Size")

    st.write("Select a Width:")
    st.session_state.grid_width = st.number_input("", min_value=0, max_value=50, value=1, step=1, key="grid_width")
 
    st.write("Select a Height:")
    st.session_state.grid_height = st.number_input("", min_value=0, max_value=50, value=1, step=1. key="grid_height")
            
    submit = st.button("Submit")


if submit:
    init_data = np.random.rand(st.session_state.grid_height, st.session_state.grid_width)
    df = pd.DataFrame(init_data, columns=[f"Col {i}" for i in range(st.session_state.grid_width)])
    np.round(df, decimals=2)
    st.dataframe(df)

st.button("Display")


