import streamlit as st

import time

#Example 1
# st.title("#Example 1 st.progress")

# with st.expander("About this app") :
#     st.write("You can now disply the progress of ypur calculations in a Streamlit app with the `st.progress` command.")

# my_bar = st.progress(0)

# for percent_complete in range(100):
#     time.sleep(0.05)
#     my_bar.progress(percent_complete + 1)

st.balloons()


#Example 2
st.title("# Example 2 st.form")

st.header("1.Example of using `with` notation")
st.subheader('Coffee machine')

with st.form("my_form"):
    st.subheader("**Order your coffee**")
    coffee_bean_val = st.selectbox("Coffee bean",["Arabica","Robusta"])
    coffee_roast_val = st.selectbox("Coffee roast",["Light","Medium","Dark"])
    brewing_val = st.selectbox('Brewing method',['Aeropress','Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity',['None',"Low",'Medium','High'])
    owncup_val = st.checkbox('Bring own cup')

    submitted = st.form_submit_button("Submit")

if submitted :
    st.markdown(f'''
    ☕ You have ordered :
    - Coffee bean : `{coffee_bean_val}`
    - Coffee roast : `{coffee_roast_val}`
    - Brewing : `{brewing_val}` 
    - Serving type : `{serving_val}`
    - Milk  : `{milk_val}`
    - Bring own cup : `{owncup_val}`   
       
    ''')
else:
    st.write("☝️ Place your order!")

st.header('2.Example of object notation')
form = st.form('my_form_2')
selected_val = form.slider("Select a value")
form.form_submit_button("Submit")

st.write("Select value: ",selected_val)






