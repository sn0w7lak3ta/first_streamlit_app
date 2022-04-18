import streamlit
import pandas

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#filter widget
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]

#display dataframe
streamlit.dataframe(fruit_to_show)

#new section to display fruitvice api response
streamlit.header('Fruityvice Fruit Advice!')

#create input
fruit_choice = streamlit.text_input('What fruit would you like information about ?', 'Kiwi')
streamlit.write('the user entered', fruit_choice)


import requests
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/'+fruit_choice)

fruityvice_norm = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_norm)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("hello from snowflake")
streamlit.text(my_data_row)
