from shutil import which
import streamlit as st

st.set_page_config(layout="wide")
st.title("How to layout your Streamlit app")

with st.exception("About this app"):
    st.write("นี่เป็นการโชว์ App ของคุณ")
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=400)

st.sidebar.header("Input")
user_name = st.sidebar.text_input('What is User nane')
User_emoji = st.sidebar.selectbox("Choose an emoji",['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header("Output")

col1,col2,col3 = st.columns(3)

with col1 :
    if user_name != " ":
        st.write(f"👋 Hello {user_name}!")
    else:
        st.write("👈 Please enter your name!!")

with col2 :
    if User_emoji !=" ":
        st.write(f"{User_emoji} is your favorite emoji!!")
    else:
        st.write("👈 Please enter your emoji!!")
with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')


