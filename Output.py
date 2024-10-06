#!/usr/bin/python3
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px  # Import plotly for interactive plots
import sys

def load_cleaned_data(file_path):
    # Load the cleaned data from the provided file path
    df_clean = pd.read_csv(file_path)  # Load your cleaned DataFrame
    return df_clean

def get_integer_columns(df):
    # Get columns that contain integer data types for line graphs
    return df.select_dtypes(include='int').columns.tolist()

def get_categorical_columns(df):
    # Get columns that contain categorical data types for bar graphs
    return df.select_dtypes(include='object').columns.tolist()

# Streamlit app
st.title("Cleaned Data Visualizations")

# Load the cleaned data from command line argument
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    df_clean = load_cleaned_data(file_path)
else:
    st.error("No data file provided. Please ensure the cleaning process completed successfully.")
    st.stop()

# Display the cleaned data
if df_clean is not None and not df_clean.empty:
    st.write("Cleaned Data Preview:")
    st.dataframe(df_clean)  # Display the cleaned DataFrame

    # Get integer and categorical columns for graphing
    integer_columns = get_integer_columns(df_clean)
    categorical_columns = get_categorical_columns(df_clean)

    # Sidebar for filters
    st.sidebar.header("Filter Options")

    # For each column, provide a filter
    filters = {}
    for col in df_clean.columns:
        if col in categorical_columns:
            unique_vals = df_clean[col].unique()
            selected_vals = st.sidebar.multiselect(f"Filter {col}", unique_vals, default=unique_vals)
            filters[col] = selected_vals
        elif col in integer_columns:
            min_val = float(df_clean[col].min())
            max_val = float(df_clean[col].max())
            selected_range = st.sidebar.slider(f"Filter {col}", min_val, max_val, (min_val, max_val))
            filters[col] = selected_range

    # Apply filters to the dataframe
    df_filtered = df_clean.copy()
    for col, filter_val in filters.items():
        if col in categorical_columns:
            df_filtered = df_filtered[df_filtered[col].isin(filter_val)]
        elif col in integer_columns:
            df_filtered = df_filtered[(df_filtered[col] >= filter_val[0]) & (df_filtered[col] <= filter_val[1])]

    # Display the filtered data
    st.write("Filtered Data Preview:")
    st.dataframe(df_filtered)

    # Graph type selection
    graph_type = st.selectbox("Select Graph Type", ["Line Graph", "Bar Graph", "Pie Chart"])

    if graph_type == "Line Graph":
        # Allow user to select x-axis and y-axis columns for line graph
        st.subheader("Line Graph Customization")
        x_axis = st.selectbox("Select X-axis column", integer_columns)
        y_axis = st.selectbox("Select Y-axis column", integer_columns)

        # Create the line graph based on user selections
        if st.button("Generate Line Graph"):
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=df_filtered, x=x_axis, y=y_axis)
            plt.title(f'Line Graph of {y_axis} vs {x_axis}')
            plt.xlabel(x_axis)
            plt.ylabel(y_axis)
            plt.tight_layout()
            
            # Display the graph in Streamlit
            st.pyplot(plt)

    elif graph_type == "Bar Graph":
        # Allow user to select x-axis and y-axis columns for bar graph
        st.subheader("Bar Graph Customization")
        x_axis = st.selectbox("Select X-axis column (categorical)", categorical_columns)
        y_axis = st.selectbox("Select Y-axis column (numeric)", integer_columns)

        # Create the bar graph based on user selections
        if st.button("Generate Bar Graph"):
            fig = px.bar(
                df_filtered,
                x=x_axis,
                y=y_axis,
                title=f'Bar Graph of {y_axis} by {x_axis}',
                text=y_axis,  # Show the values on the bars
                color=y_axis,  # Optional: color by the y-axis values
                labels={y_axis: y_axis, x_axis: x_axis}
            )

            # Update layout to show hover info and adjust text position
            fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

            # Display the graph in Streamlit
            st.plotly_chart(fig)

    elif graph_type == "Pie Chart":
        # Allow user to select which mcq column to display on pie chart
        st.subheader("Pie Chart Customization")
        selected_column = st.selectbox("Select data column", categorical_columns)
        
        # Count the occurrences of each response category
        response_counts = df_filtered[selected_column].value_counts().reset_index()
        response_counts.columns = ['category', 'count']

        # Create the pie chart based on user selections
        if st.button("Generate Pie Chart"):
            fig = px.pie(response_counts, values="count", names="category")
            st.plotly_chart(fig)
else:
    st.error("The cleaned data is empty.")
