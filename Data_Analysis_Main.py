import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

import Global_Variables as glo_vars

# Function to parse excel with checks
def parse_data(headerRow, firstDataRow):
    rowsSkipped = []
    for rowToSkip in range(0, firstDataRow-1): #initialze list of skipped rows, from 0 till the row above the first data row
        rowsSkipped.append(rowToSkip)
    rowsSkipped.pop(rowsSkipped.index(headerRow-1)) #remove the header row from skipped rows list

    try:
        if glo_vars.excel_file_path.lower().endswith(('.xlsx', '.xls')):
            glo_vars.df = pd.read_excel(glo_vars.excel_file_path, header=(headerRow-1), skiprows=rowsSkipped)
        elif glo_vars.excel_file_path.lower().endswith('.csv'):
            glo_vars.df = pd.read_csv(glo_vars.excel_file_path, header=(headerRow-1), skiprows=rowsSkipped)

        return "success"

    except Exception as e:
        return f"Error parsing spreadsheet with following error: {e}"
    
# Function to convert open-ended responses to lowercase and replace invalid responses
def replace_invalid_responses(column_name):
    replace_values = {"nil", "n.a.", "idk", "na"}
    if column_name in glo_vars.df.columns:
        try:
            # Convert to lowercase
            glo_vars.df[column_name] = glo_vars.df[column_name].str.lower()
            # Replace invalid responses
            glo_vars.df[column_name] = glo_vars.df[column_name].replace(replace_values, "No concerns expressed")

            return "success"
        except Exception as e:
            return f"Error cleaning open-ended responses with following error: {e}"

"""
# Function to prompt the user to select a file for saving the data
def save_cleaned_data(df):
    while True:
        save_path = asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx;*.xls"), ("CSV files", "*.csv")]
        )
        if not save_path:
            print("Save operation cancelled.")
            return
        if save_path.lower().endswith(('.xlsx', '.xls', '.csv')):
            try:
                if save_path.lower().endswith('.csv'):
                    df.to_csv(save_path, index=False)
                else:
                    df.to_excel(save_path, index=False)
                print(f"Cleaned data has been saved to {save_path}")
                break
            except Exception as e:
                print(f"Error saving file: {e}")
                print("Please try saving the file again.")
        else:
            print("Invalid file type selected. Please select an Excel or CSV file.")

# Drop any rows that have NaN in 'Birth Year' or 'time taken survey in mins'
df['Birth Year'] = pd.to_numeric(df['Birth Year'], errors='coerce')
df_clean = df.dropna(subset=['Birth Year', 'time taken survey in mins'])

# Ensure 'Birth Year' is integer type
df_clean['Birth Year'] = df_clean['Birth Year'].astype(int)

# Dropping rows based on duplicate values in column 'S/N', but only if 'S/N' exists
if 'S/N' in df_clean.columns:
    df_clean = df_clean.drop_duplicates(subset=['S/N'])

# Aggregate data: Calculate average survey time per birth year
agg_df = df_clean.groupby('Birth Year')['time taken survey in mins'].mean().reset_index()

# Plotting the bar graph for Average Survey Time by Birth Year
plt.figure(figsize=(12, 6))
sns.barplot(x='Birth Year', y='time taken survey in mins', data=agg_df)
plt.title('Average Survey Time by Birth Year')
plt.xlabel('Birth Year')
plt.ylabel('Average Time Taken Survey in Mins')
plt.xticks(rotation=45)  # Rotate x labels for better readability
plt.tight_layout()
plt.show()

# Visualization: Pie chart for 'Mobile Service Provider'
# Get the unique number of mobile service providers and set the explode parameter dynamically
unique_providers = df_clean['Mobile Service Provider'].nunique()
explode = [0.05] * unique_providers  # Create a list of 0.05 for each unique provider

# Plot the pie chart for Mobile Service Provider distribution
plt.figure(figsize=(8, 8))
df_clean['Mobile Service Provider'].value_counts().plot.pie(
    autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3'), explode=explode
)
plt.title('Distribution of Mobile Service Providers')
plt.ylabel('')  # Hide the y-label to make the chart cleaner
plt.tight_layout()
plt.show()

# Call the function to allow the user to save the cleaned data
save_cleaned_data(df_clean)
"""