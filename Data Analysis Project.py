import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Hide the root Tkinter window
Tk().withdraw()

# Function to prompt the user to select a file for saving the data
def save_cleaned_data(df):
    save_path = asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx;*.xls")])
    if save_path:
        df.to_excel(save_path, index=False)
        print(f"Cleaned data has been saved to {save_path}")
    else:
        print("Save operation cancelled.")

# Function to replace "nil", "NIL", "N.A.", "n.a.", "IDK", "idk", "Nil" with "No concerns expressed"
def replace_invalid_responses(df, column_name):
    replace_values = ["nil", "NIL", "N.A.", "n.a.", "IDK", "idk", "Nil"]
    df[column_name] = df[column_name].replace(replace_values, "No concerns expressed")
    return df

# Prompt the user to select the file
file_path = askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
if not file_path:
    raise FileNotFoundError("No file selected")

# Load the data, skipping the second row, and obtain df header columns
df = pd.read_excel(file_path, header=0, skiprows=[1])

# Print out the first few rows and the columns to check the data
print("First few rows of the DataFrame:")
print(df.head())

print("\nColumns available in the DataFrame:")
print(df.columns)

headersToCleanData = ['Biggest Factor for Changing Provider', 'Aspect for Improvement']

# clean data for open-ended header questions
for header in headersToCleanData:
    df = replace_invalid_responses(df, header)

# Drop any rows that have NaN in 'Birth Year' or 'time taken survey in mins'
df['Birth Year'] = pd.to_numeric(df['Birth Year'], errors='coerce')
df_clean = df.dropna(subset=['Birth Year', 'time taken survey in mins'])

# Ensure 'Birth Year' is integer type
df_clean['Birth Year'] = df_clean['Birth Year'].astype(int)

# Dropping rows based off duplicate values in column S/N
df_clean = df_clean.drop_duplicates(subset=['S/N'])

# Aggregate data: Calculate average survey time per birth year
agg_df = df_clean.groupby('Birth Year')['time taken survey in mins'].mean().reset_index()

# Plotting the bar graph
plt.figure(figsize=(12, 6))
sns.barplot(x='Birth Year', y='time taken survey in mins', data=agg_df)
plt.title('Average Survey Time by Birth Year')
plt.xlabel('Birth Year')
plt.ylabel('Average Time Taken Survey in Mins')
plt.xticks(rotation=45)  # Rotate x labels for better readability
plt.show()

# Visualization: Pie chart for 'Mobile Service Provider'
# Get the unique number of mobile service providers and set the explode parameter dynamically
unique_providers = df_clean['Mobile Service Provider'].nunique()
explode = [0.05] * unique_providers  # Create a list of 0.05 for each unique provider

# Plot the pie chart
plt.figure(figsize=(8, 8))
df_clean['Mobile Service Provider'].value_counts().plot.pie(
    autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3'), explode=explode
)
plt.title('Distribution of Mobile Service Providers')
plt.ylabel('')  # Hide the y-label to make the chart cleaner
plt.show()

# Call the function to allow the user to save the cleaned data
save_cleaned_data(df_clean)
