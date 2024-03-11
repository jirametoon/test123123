import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import plotly.express as px


st.title("Supplier-List")

# Specify the file path with escaped backslashes
path = "Supplier-List.csv"

# Read the CSV file
df = pd.read_csv(path)

# Display the DataFrame
st.write(df)



df = pd.read_csv(path)

#data_Country = df.iloc[24]


# Count occurrences of each country
#country_counts = data_Country['Country RA'].value_counts()

country_counts = df['Country RA'].value_counts()


plt.bar(country_counts.index, country_counts.values)
plt.xlabel('Country RA')
plt.ylabel('Count')
plt.title('Number of Occurrences of Each Country RA')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot() 


st.set_option('deprecation.showPyplotGlobalUse', False)



df = pd.read_csv(path)

# Count occurrences of each country
country_counts = df['Country RA'].value_counts().reset_index()
country_counts.columns = ['Country RA', 'Count']

# Create a numpy array for custom color scale
color_scale = np.linspace(0, 1, len(country_counts))

# Create Altair chart
chart = alt.Chart(country_counts).mark_bar().encode(
    x=alt.X('Country RA', sort='-y'),
    y='Count',
    color=alt.Color('Count', scale=alt.Scale(scheme='greens'), legend=None)
).properties(
    width=600,
    height=400,
    title='Number of Occurrences of Each Country RA'
).configure_axis(
    labelAngle=-45
)

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)

#*****************************************************************************************************************

df = pd.read_csv(path)

# Count occurrences of each country
country_counts = df['Country RA'].value_counts().reset_index()
country_counts.columns = ['Country RA', 'Count']

# Custom color palette for bars
colors = plt.cm.viridis(np.linspace(0, 1, len(country_counts)))

# Plot the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(country_counts['Country RA'], country_counts['Count'], color=colors)

# Add data labels on top of each bar
for bar, count in zip(bars, country_counts['Count']):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), count,
            ha='center', va='bottom', fontsize=10, color='black')

# Remove background and spines
ax.set_facecolor('none')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Set labels and title
ax.set_xlabel('Country RA', fontsize=14)
ax.set_ylabel('Count', fontsize=14)
ax.set_title('Number of Occurrences of Each Country RA', fontsize=16)

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right', fontsize=10)

# Remove y-axis tick marks
ax.tick_params(axis='y', length=0)

# Adjust layout and display the chart
plt.tight_layout()
st.pyplot(fig, bbox_inches='tight', pad_inches=0)






df = pd.read_csv(path)

# Count occurrences of each country
country_counts = df['Country RA'].value_counts().reset_index()
country_counts.columns = ['Country RA', 'Count']

# Create pie chart using Plotly
fig = px.pie(country_counts, values='Count', names='Country RA', title='Number of Occurrences of Each Country RA')

# Display the pie chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

###########################################################################################


Nationality_counts = df['Nationality'].value_counts().reset_index()
Nationality_counts.columns = ['Nationality', 'Count']

# Create pie chart using Plotly
fig = px.pie(Nationality_counts, values='Count', names='Nationality', title='Number of Occurrences of Each Nationality')

# Display the pie chart in Streamlit
st.plotly_chart(fig, use_container_width=True)
