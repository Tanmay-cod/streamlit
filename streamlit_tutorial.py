import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

st.title("Welcome to chatgpt Go")
st.text_input("Ask your question")

st.write("This is our first streamlit app")
st.text("Let's get started")

name = st.text_input("Enter you name")
if st.button("Greet") :
    st.success(f"Hello {name}")
    
# How to upload csv file

upload_file = st.file_uploader("Upload a csv file", type = "csv")
if upload_file :
    df = pd.read_csv(upload_file)
    st.dataframe(df)
    
st.header(" This is a header") 
st.subheader("This is a subheader")
st.markdown("[Github](https://github.com/reveshrathod005)")
st.text_area('Enter your message : ')

level = st.slider("Choose a level", min_value=1, max_value=5)
st.write(f"Selected level: {level}")


result = st.selectbox("Select Language:", ['Python', 'Java', 'CPP'])
st.write(f"You selected {result} language")

languages = st.multiselect("Select Language:", ['Python', 'Java', 'CPP'])
st.write("You selected", len(languages), "languages")


if st.checkbox("show details") :
    st.info("here are more details")
    
#from tag
with st.form("login form") :
    username = st.text_input("Enter the username : ")
    password = st.text_input("password", type = "password")
    
    submitted = st.form_submit_button("Login")
    
    if submitted :
        st.success(f"Welcome {name}")

df = pd.DataFrame(np.random.randn(20, 3), columns = ["A", "B", "C"])

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

st.video("https://youtu.be/H-JTC5P6RKU?si=dTLnpmudHfr3ZvsB")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQD5KiW2AtGp0DwZO2a3GqHa-tJ7lcg6y2tZKBGMoq4MA&s=10", caption = "Streamlit")