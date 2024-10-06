# Output.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys

def load_cleaned_data(file_path):
    # Load the cleaned data from the provided file path
    df_clean = pd.read_csv(file_path)  # Load your cleaned DataFrame
    return df_clean

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

    # Bar chart and Pie chart visualizations...
