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

    # Graph type selection
    graph_type = st.selectbox("Select Graph Type", ["Line Graph", "Bar Graph"])

    if graph_type == "Line Graph":
        # Allow user to select x-axis and y-axis columns for line graph
        st.subheader("Line Graph Customization")
        x_axis = st.selectbox("Select X-axis column", integer_columns)
        y_axis = st.selectbox("Select Y-axis column", integer_columns)

        # Create the line graph based on user selections
        if st.button("Generate Line Graph"):
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=df_clean, x=x_axis, y=y_axis)
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
                df_clean,
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

else:
    st.error("The cleaned data is empty.")
