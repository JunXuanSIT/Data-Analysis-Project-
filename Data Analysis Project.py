'Lets start our programming project:)'

import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'Score': [88, 79, 93, 85]}

df = pd.DataFrame(data)

# Display DataFrame
print(df)

# Plot a bar chart of scores
plt.bar(df['Name'], df['Score'])
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Scores by Name')
plt.show()