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
    ['Green','Yellow','Red','Blue'],
    ['Yellow','Red']
)
st.write("Your selected : ",option2)




