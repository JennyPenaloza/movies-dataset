import altair as alt
import pandas as pd
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

    starting_data = np.zeros(st.session_state.grid_height, st.session_state.grid_width)
    df = pd.DataFrame(starting_data, columns=[f"Col {i}" for i in range(st.session_state.grid_width)])
    np.round(df, decimals=2)

st.button("Display")

# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/movies_genres_summary.csv")
    return df


df = load_data()

# Show a multiselect widget with the genres using `st.multiselect`.
genres = st.multiselect(
    "Genres",
    df.genre.unique(),
    ["Action", "Adventure", "Biography", "Comedy", "Drama", "Horror"],
)

# Show a slider widget with the years using `st.slider`.
years = st.slider("Years", 1986, 2006, (2000, 2016))

# Filter the dataframe based on the widget input and reshape it.
df_filtered = df[(df["genre"].isin(genres)) & (df["year"].between(years[0], years[1]))]
df_reshaped = df_filtered.pivot_table(
    index="year", columns="genre", values="gross", aggfunc="sum", fill_value=0
)
df_reshaped = df_reshaped.sort_values(by="year", ascending=False)


# Display the data as a table using `st.dataframe`.
st.dataframe(
    df_reshaped,
    use_container_width=True,
    column_config={"year": st.column_config.TextColumn("Year")},
)


