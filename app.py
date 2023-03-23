import pandas as pd
import streamlit as st
from libraries import * 


countries = ['India','Sri Lanka','China','Australia','USA','Russia']
data_types = ['cases','deaths','recovered']

country_codes = {'USA' : 'us','India':'in','Russia' : 'rus' , 'Sri Lanka' : 'lk' , 'Australia' : 'au', 'China' : 'cn' }


#creating the dashboard sidebar
country = st.sidebar.selectbox('Pick a Country', countries)
days = st.sidebar.slider('Select number of Days', min_value=1,max_value=90)
data_type = st.sidebar.multiselect('Pick Data Types(pick at least one to continue)',data_types)

#Total_cases
total_cases = get_historic_cases(country,str(days))
total_deaths = get_historic_deaths(country,str(days))
total_recoveries = get_historic_recoveries(country,str(days))

total_df = pd.concat([total_cases,total_deaths,total_recoveries],axis=1).astype(int)

#Daily_cases
daily_cases = get_daily_cases(country,str(days))
daily_deaths = get_daily_deaths(country,str(days))
daily_recoveries = get_daily_recoveries(country,str(days))

daily_df = pd.concat([daily_cases,daily_deaths,daily_recoveries],axis=1).astype(int)

#Yesterday_Cases
yesterday_cases = get_yesterday_cases(country,)
yesterday_deaths = get_yesterday_deaths(country,)
yesterday_recoveries = get_yesterday_recoveries(country,)

st.title('Welcome to the COVID Dashboard')
st.metric('Country',country)
st.image(f"https://flagcdn.com/80x60/{country_codes[country]}.png") 

col1,col2,col3 = st.columns(3)



col1.metric('Cases',yesterday_cases)
col2.metric('Deaths',yesterday_deaths)
col3.metric('Recoveries',yesterday_recoveries)

st.line_chart(daily_df)

st.write(daily_df)

video_file = open('covid_video.mp4','rb')
video_bytes = video_file.read()

st.video(video_bytes)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.the-scientist.com/assets/articleNo/69402/aImg/44174/coronavirus-article-s.jpg");
             
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

st.set_page_config(page_title='Covid Dashboard')