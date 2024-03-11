import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load data
path = 'Supplier-List.csv'
df = pd.read_csv(path)

# Create a pivot table to count the occurrences of each combination of country and product group
pivot_table = pd.pivot_table(df, values='EntryID', index=['Country RA'],
                             columns=['Product Group'], aggfunc='count', fill_value=0)

# Convert the pivot table to a DataFrame for plotting
pivot_data = pivot_table.reset_index().melt('Country RA', var_name='Product Group', value_name='Count')

# Create a horizontal bar chart
plt.figure(figsize=(12, 8))
chart = sns.barplot(x='Count', y='Country RA', hue='Product Group', data=pivot_data, orient='h')

# Set labels and title
plt.xlabel('Count', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.title('Product Groups by Country', fontsize=16)

# Rotate x-axis labels
plt.xticks(rotation=45)

# Show the plot
plt.show()