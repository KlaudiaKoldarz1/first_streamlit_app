import streamlit as st
import pandas as pandas
import requests 
import snowflake.connector 
from urllib.error import URLError

st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list  = my_fruit_list.set_index('Fruit')
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)

def get_fruityadvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized 

st.header('Fruityvice Fruit Advice!')
try :
  fruit_choice = st.text_input('What friut would you like information aobut?', 'Kiwi')
  if not fruit_choice:
    st.error("Please select friut information.")
  else:
    back_from_function = get_fruityadvice_data(fruit_choice)
    st.dataframe(back_from_function)
except URLError as e:
  st.Error()
#st.text(fruityvice_response.json())

#st.stop()

 


st.header("The friut list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
    return  my_cur.fetchall()

if st.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    st.dataframe(my_data_rows)


fruit_choice1 = st.text_input('What friut would you like to add?', 'Kiwi')
st.write('Thank you for adding: ', fruit_choice1)
my_cur.Execute("INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES ('')")
