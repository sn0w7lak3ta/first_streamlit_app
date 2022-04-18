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

import requests
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/Watermelon')
streamlit.text(fruityvice_response.json())

