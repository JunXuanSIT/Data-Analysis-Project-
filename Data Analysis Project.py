# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the Excel file (make sure the file path is correct)
# The `engine='openpyxl'` parameter ensures the correct engine is used for .xlsx files
file_path = 'your_excel_file.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Preview the data (check the first 5 rows)
print(df.head())

# Check column names
print(df.columns)

# Example: Plot a graph of two columns
# Replace 'Column1' and 'Column2' with the actual column names in your Excel file
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Column1', y='Column2', data=df)

# Set labels and title
plt.xlabel('Column1')
plt.ylabel('Column2')
plt.title('Scatter Plot of Column1 vs Column2')

# Show the plot
plt.show()

# Example: Bar plot for a categorical column
# Replace 'CategoryColumn' and 'NumericColumn' with actual column names
plt.figure(figsize=(10, 6))
sns.barplot(x='CategoryColumn', y='NumericColumn', data=df)

# Set labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Plot of Categories')

# Show the plot
plt.show()
