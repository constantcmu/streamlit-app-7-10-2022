import streamlit as st


#Example 1
st.header("Example 1 st.selectbox")

option = st.selectbox(
    "what is your favorite color?",
    ("Blue","Red","Green")
)
st.write("Your favorite color is : ",option)

#Example 2
st.header("Example 2 st.multiselect")

option2 = st.multiselect(
    "What are your favorite colors",
    ['Green','Yellow','Red','Blue','Aooddy'],
    ['Yellow','Aooddy'] #frist show in box
)
st.write("Your selected : ",option2)
 
#Example 3
st.header("Example 3 st.checkbox")

st.write("What would you like to order?")

icecream = st.checkbox('Ice cream')
coffee = st.checkbox("coffee")
cola = st.checkbox('cola')

if icecream :
    st.write("Great! Here's some more 🍦")
if coffee :
    st.write("Okey, here's some coffee ☕")
if cola :
    st.write("Here you go 🥤")






