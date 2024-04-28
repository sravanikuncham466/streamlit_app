import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
@st.cache
def load_data():
    df = pd.read_csv('athlete_events.csv')
    return df

df = load_data()

# Sidebar for user input
st.sidebar.title('Olympics App')
selected_chart = st.sidebar.selectbox('Select Chart', ['Age Distribution', 'Height vs. Weight', 'Medal Distribution'])

# Main content
st.title('Olympics Data Analysis')

if selected_chart == 'Age Distribution':
    st.subheader('Distribution of Athlete Ages')
    fig, ax = plt.subplots()
    sns.histplot(data=df, x='Age', bins=30, kde=True, ax=ax)
    st.pyplot(fig)

elif selected_chart == 'Height vs. Weight':
    st.subheader('Height vs. Weight Scatter Plot')
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='Height', y='Weight', hue='Sex', ax=ax)
    st.pyplot(fig)

elif selected_chart == 'Medal Distribution':
    st.subheader('Medal Distribution by Country')
    medal_counts = df.groupby(['NOC', 'Medal']).size().unstack(fill_value=0)
    medal_counts['Total Medals'] = medal_counts.sum(axis=1)
    st.dataframe(medal_counts)

    st.subheader('Select Country for Medal Distribution')
    selected_country = st.selectbox('Country', df['NOC'].unique())
    st.bar_chart(medal_counts.loc[selected_country])

