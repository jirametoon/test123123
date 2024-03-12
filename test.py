import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px

st.title("Supplier-List")

# Specify the file path with escaped backslashes
path = "C:\Users\Toon PC\Desktop\\test123123\Supplier-List.csv"

# Read the CSV file
df = pd.read_csv(path)

# Display the DataFrame
st.write(df)

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

##################################################################################################

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

# Count occurrences of each Main Product Group
group_counts = df['Main Product Group'].value_counts().reset_index()
group_counts.columns = ['Main Product Group', 'Count']

# Create Bar chart using Altair
chart = alt.Chart(group_counts).mark_bar().encode(
    x=alt.X('Main Product Group:N', axis=alt.Axis(labelAngle=-45)),
    y='Count:Q',  # y-axis as count of occurrences
    color='Main Product Group:N',  # color each bar based on Main Product Group
    tooltip=['Main Product Group', 'Count']  # show tooltip on hover
).properties(
    width=600,
    height=400
)

# Display the Bar chart in Streamlit
st.altair_chart(chart, use_container_width=True)

##################################################################################################

group_counts = df.groupby(['Nationality', 'Main Product Group']).size().reset_index(name='Count')

# Create Bar chart using Altair
chart = alt.Chart(group_counts).mark_bar().encode(
    x=alt.X('Nationality:N', axis=alt.Axis(labelAngle=-45)),
    y='Count:Q',
    color='Main Product Group:N',
    tooltip=['Nationality', 'Main Product Group', 'Count']
).properties(
    width=600,
    height=400
)

# Display the Bar chart in Streamlit
#st.altair_chart(chart, use_container_width=True)

# Create Bar chart using Altair
chart = alt.Chart(group_counts).mark_bar().encode(
    y=alt.X('Nationality:N'),
    x='Count:Q',
    color='Main Product Group:N',
    tooltip=['Nationality', 'Main Product Group', 'Count']
).properties(
    width=600,
    height=400
)

# Display the Bar chart in Streamlit
st.altair_chart(chart, use_container_width=True)