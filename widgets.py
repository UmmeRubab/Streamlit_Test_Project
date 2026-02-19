import streamlit as st
import pandas as pd

st.title("Streamlit Project by Umme Rubab")

name = st.text_input("Enter your name")

if name:
    st.write(f"HELLO! {name}, welcome to AI class")

age = st.slider("select ur age", 0, 100, 25) #start #end #default

st.write(f"your age is {age}.")

options = ["python", "java", "c++"]

choice = st.selectbox("choose your fav lang", options)
st.write(f"your selected {choice}.")


data = {
    "Name" : ["John", "Jack", "Jill", "Mike"],
    "Age" : [20, 30, 40, 40],
    "City" : ["New York", "Los Angles", "California", "Chichago"]
}

df = pd.DataFrame(data)

df.to_csv("Sampledata.csv")

st.write(df)

uploaded_file = st.file_uploader("Choose a csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

uploaded_file = st.file_uploader("")
uploaded_file = st.file_uploader("Choose a csv file")