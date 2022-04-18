import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
try :
  fruit_choice = streamlit.text_input('What fruit would you like information about ?') #, 'Kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get informations.")
  else:   
    fruityvice_response = requests.get('https://fruityvice.com/api/fruit/'+fruit_choice)
    fruityvice_norm = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_norm)
except URLError as e:
  streamlit.error()





#don't run anything past here while we troubleshoot
streamlit.stop()




my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_rows)

fruit_choice = streamlit.text_input('What fruit would you like information about ?', 'jackfruit')
streamlit.write('the user entered', fruit_choice)


my_cur.execute("insert into fruit_load_list values ('from streamlit')")
