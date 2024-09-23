import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990)')
df = pd.read_csv('housing.csv')


price_filter = st.slider('Minimal Median House Pirce :', 0, 500001, 200000)  
st.header('See more filters in the sidebar:')

location_filter= st.sidebar.multiselect(
     'Choose the loctaion type',
     df.ocean_proximity.unique(),  
     df.ocean_proximity.unique())  

income_level =st.sidebar.radio(
    "Select income level:",
    ('Low','Meidum','High'))

if income_level =='Low (≤2.5)':
    filtered_df = df[df.median_income <=2.5]
elif income_level =='Meidum (> 2.5 & < 4.5)':
    filtered_df = df[(df.median_income >2.5)&(df.median_income <4.5)]
else :
    filtered_df = df[df.median_income >4.5]  


# filter by population
df = df[df.median_house_value >= price_filter]

# filter by capital
df = df[df.ocean_proximity.isin(location_filter)]

if income_level == 'Low (≤2.5)':
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium (> 2.5 & < 4.5)':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median_income'] > 4.5] 
 

# show on map
st.map(df)

# show the plot
st.subheader('The Median House Value')
fig, ax = plt.subplots(figsize=(20, 5))


median_income = df.median_house_value.value_counts()
df.median_income.hist(bins=30)
 

fig, ax = plt.subplots(figsize=(15, 8))
data =df[(df.median_house_value>=200000)&(df.median_income<=2.5)]

data.median_house_value.hist(bins=30)


plt.grid(True)
st.pyplot(fig)

