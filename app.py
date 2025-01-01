import folium  # For maps
import pandas as pd  # For data manipulation
import streamlit as st

# Sample training data (replace with your actual data)
training_data = pd.DataFrame(
    {
        "Date": ["2023-10-15", "2023-10-16", "2023-10-17"],
        "Location": ["Training Ground A", "Training Ground B", "Stadium"],
        "Duration": [60, 90, 120],  # Minutes
        "Drills": ["Passing drills", "Shooting drills", "1v1 drills"],
        "Notes": [
            "Good performance on passing drills",
            "Need to work on shooting accuracy",
            "Intense match simulation",
        ],
    }
)

# Streamlit app layout
st.title("Soccer Training App")

# Sidebar for navigation
with st.sidebar:
    st.header("Navigation")
    selected_page = st.selectbox(
        "Select Page",
        [
            "Training Log",
            "Statistics",
            "Map",
        ],
    )

# Display content based on selected page
if selected_page == "Training Log":
    st.header("Training Log")
    st.dataframe(training_data)

elif selected_page == "Statistics":
    st.header("Statistics")
    # Add code to calculate and display statistics (e.g.,
    # average training duration, most frequent drills)

elif selected_page == "Map":
    st.header("Map")
    # Create a map using Folium (replace with your actual data)
    map = folium.Map(
        location=[55.6763, 12.5683], zoom_start=12
    )  # Adjust coordinates and zoom
    for index, row in training_data.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]], popup=row["Location"]
        ).add_to(map)
    st.folium_map(map)

# Add more sections and features as needed
# (e.g., player profiles, goal tracking)
