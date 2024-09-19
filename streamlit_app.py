import altair as alt
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
    col_width = st.columns([1, 2, 1])
    with col_width[0]:
        if st.sidebar.button('➖', key="decrease_width"):
            if st.session_state.grid_width > 1:
                st.session_state.grid_width -= 1    

    with col_width[1]:
        st.write(f"{st.session_state.grid_width}")
    with col_width[2]:
        if st.sidebar.button('➕', key="increase_width"):
            st.session_state.grid_width +=1

    st.write("Select a Height:")
    col_height = st.columns([1, 2, 1])
    with col_height[0]:
        if st.sidebar.button('➖', key="decrease_height"):
            if st.session_state.grid_height > 1:
                st.session_state.grid_height -= 1    

    with col_height[1]:
        st.write(f"{st.session_state.grid_height}")
    with col_height[2]:
        if st.sidebar.button('➕', key="increase_height"):
            st.session_state.grid_height +=1
            
    submit = st.button("Submit")


if submit:
    init_data = np.random.rand(st.session_state.grid_height, st.session_state.grid_width)
    df = pd.DataFrame(init_data, columns=[f"Col {i}" for i in range(st.session_state.grid_width)])
    np.round(df, decimals=2)

st.button("Display")


# Display the data as a table using `st.dataframe`.
st.dataframe(
    df_reshaped,
    use_container_width=True,
    column_config={"year": st.column_config.TextColumn("Year")},
)


