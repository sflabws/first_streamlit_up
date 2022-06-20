import streamlit
import pandas
import requests

streamlit.title('My Parents new healthy diner')

streamlit.header('Breakfast favorites')
streamlit.text('🥣 Omega 3 and Bluberry Oatmeal')
streamlit.text('🥗 Kale, spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
fruityvice_response=response.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)


streamlit.dataframe(fruits_to_show)
