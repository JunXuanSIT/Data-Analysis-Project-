import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the root Tkinter window
Tk().withdraw()

# Prompt the user to select the file
file_path = askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
if not file_path:
    raise FileNotFoundError("No file selected")

# Load the data, skipping the first two rows
df = pd.read_excel(file_path, header=None, skiprows=[0, 1])

# Print out the first few rows and the columns to check the data
print("First few rows of the DataFrame:")
print(df.head())

print("\nColumns available in the DataFrame:")
print(df.columns)

# Manually set the correct headers
headers = [
    'responses', 'time taken survey in mins', 'Gender', 'Birth Year',
    'Mobile Phone Plan', 'Mobile Service Provider', 'Satisfaction with Plan Options',
    'Satisfaction with Reception', 'Satisfaction with Customer Service',
    'Action in Case of Outage', 'Biggest Factor for Changing Provider',
    'Aspect for Improvement'
]

# Set the headers
df.columns = headers

# Drop any rows that have NaN in 'Birth Year' or 'time taken survey in mins'
df['Birth Year'] = pd.to_numeric(df['Birth Year'], errors='coerce')
df_clean = df.dropna(subset=['Birth Year', 'time taken survey in mins'])

# Ensure 'Birth Year' is integer type
df_clean['Birth Year'] = df_clean['Birth Year'].astype(int)

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
