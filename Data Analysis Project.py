import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Hide the root Tkinter window
Tk().withdraw()

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

# Function to convert text responses to lowercase and replace invalid responses
def replace_invalid_responses(df, column_name):
    replace_values = {"nil", "n.a.", "idk", "na"}
    if column_name in df.columns:
        # Convert to lowercase
        df[column_name] = df[column_name].str.lower()
        # Replace invalid responses
        df[column_name] = df[column_name].replace(replace_values, "No concerns expressed")
    return df

# Function to load data with checks
def load_data():
    while True:
        file_path = askopenfilename(
            filetypes=[("Excel files", "*.xlsx;*.xls"), ("CSV files", "*.csv")]
        )
        if not file_path:
            print("File selection cancelled.")
            return None
        try:
            if file_path.lower().endswith(('.xlsx', '.xls')):
                df = pd.read_excel(file_path, header=0, skiprows=[1])
            elif file_path.lower().endswith('.csv'):
                df = pd.read_csv(file_path, header=0, skiprows=[1])
            else:
                print("Invalid file type selected. Please select an Excel or CSV file.")
                continue
            return df
        except Exception as e:
            print(f"Error loading file: {e}. Please try again.")

# Load the data with checks
df = load_data()
if df is None:
    sys.exit()  # Exit the program if no file is selected

# Define the columns to clean and lower text for open-ended questions
headers_to_clean = [
    'Biggest Factor for Changing Provider',
    'Aspect for Improvement',
    'Biggest Area of Improvement'
]

# Clean data for open-ended header questions
for header in headers_to_clean:
    df = replace_invalid_responses(df, header)

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
