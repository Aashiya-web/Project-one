import streamlit as st
import pandas as pd
import pymysql

# Connect to the MySQL database
def get_data_from_db():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='sakila'  # or your database name
    )
    query = "SELECT * FROM bus_routes"
    df = pd.read_sql(query, connection)
    connection.close()
    
    # Ensure that 'price' and 'star_rating' columns are numeric
    df['price'] = pd.to_numeric(df['price'], errors='coerce')  # Convert 'price' to numeric
    df['star_rating'] = pd.to_numeric(df['star_rating'], errors='coerce')  # Convert 'star_rating' to numeric
    
    return df

# Streamlit App with UI enhancements
def run_streamlit_app():
    # Add custom CSS for UI design
    st.markdown("""
        <style>
            body {
                background-color: #f4f4f9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            .header {
                text-align: center;
                font-size: 40px;
                color: #4CAF50;
                font-weight: bold;
                margin-top: 30px;
            }

            .subheader {
                font-size: 26px;
                color: #1976D2;
                font-weight: 600;
                margin-top: 20px;
            }

            .table-container {
                background-color: white;
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                margin-top: 20px;
                overflow-x: auto;  /* Enable horizontal scrolling for wide tables */
            }

            .table {
                width: 100%;  /* Set table width to 100% of its container */
                border-collapse: collapse;
            }

            .table th, .table td {
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }

            /* Custom Table Heading Color */
            .table thead {
                background-color: #1976D2;  /* Table heading color */
                color: white;
            }

            /* Hover effect for table rows */
            .table tbody tr:hover {
                background-color: #f1f1f1;
            }

            .stButton button {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px 20px;
                border-radius: 5px;
                border: none;
                cursor: pointer;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            }

            .stButton button:hover {
                background-color: #45a049;
            }

            .stSelectbox select, .stSlider input {
                border-radius: 5px;
                border: 1px solid #ddd;
                padding: 10px;
            }

        </style>
    """, unsafe_allow_html=True)

    # Load data
    df = get_data_from_db()

    # Header
    st.markdown('<h1 class="header">Redbus Data - Bus Route Information</h1>', unsafe_allow_html=True)
    
    # Container for the table display
    with st.container():
        st.subheader("All Bus Routes")
        # Display the full table without any hidden columns
        st.dataframe(df, use_container_width=True)

    # Filters section in a two-column layout
    col1, col2 = st.columns(2)

    with col1:
        # Filter by Bus Type
        bus_types = df['bustype'].unique()
        selected_bus_type = st.selectbox("Select Bus Type", bus_types)

    with col2:
        # Filter by Route Name
        route_names = df['route_name'].unique()
        selected_route_name = st.selectbox("Select Route Name", route_names)

    filtered_df_by_bus_type = df[df['bustype'] == selected_bus_type]
    filtered_df_by_route = filtered_df_by_bus_type[filtered_df_by_bus_type['route_name'] == selected_route_name]

    st.markdown(f'### Filtered Data - Bus Type: {selected_bus_type} & Route: {selected_route_name}')
    # Display filtered data for bus type and route
    st.dataframe(filtered_df_by_route, use_container_width=True)

    # Slider filters for Price and Rating
    st.subheader("Filter by Price and Rating")

    col1, col2 = st.columns(2)

    with col1:
        # Price Range Filter
        min_price = df['price'].min()
        max_price = df['price'].max()
        selected_price_range = st.slider(
            "Select Price Range",
            min_value=float(min_price),
            max_value=float(max_price),
            value=(float(min_price), float(max_price))
        )

    with col2:
        # Rating Range Filter
        min_rating = df['star_rating'].min()
        max_rating = df['star_rating'].max()
        selected_rating = st.slider(
            "Select Rating Range",
            min_value=float(min_rating),
            max_value=float(max_rating),
            value=(float(min_rating), float(max_rating))
        )

    filtered_df_by_price_rating = filtered_df_by_route[  # Filter data by price and rating
        (filtered_df_by_route['price'] >= selected_price_range[0]) &
        (filtered_df_by_route['price'] <= selected_price_range[1]) &
        (filtered_df_by_route['star_rating'] >= selected_rating[0]) &
        (filtered_df_by_route['star_rating'] <= selected_rating[1])
    ]
    
    st.subheader(f"Filtered Data - Price: {selected_price_range} & Rating: {selected_rating}")
    # Display filtered data based on price and rating
    st.dataframe(filtered_df_by_price_rating, use_container_width=True)

    # Button for detailed view
    if st.button("Show Detailed View of the Selected Route"):
        st.write(filtered_df_by_price_rating)

# Run the Streamlit app
if __name__ == "__main__":
    run_streamlit_app()
