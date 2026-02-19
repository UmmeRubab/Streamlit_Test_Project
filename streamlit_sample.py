#importing libs
import streamlit as st
import pandas as pd #used to convert things into data frames
import numpy as np

#building title of the application #important component
st.title("Hello Streamlit")
st.write("sample")

#create a simple dataframe
df = pd.DataFrame({
    'First column' : [1,2,3,4],
    'Second column' : [10,20,30,40]
})

#show the above df to streamlit
st.write("Here is the DF")
st.write(df)

#cretae graph
chartData = pd.DataFrame(
    np.random.randn(20,4), columns=['a','b','c', 'd']
)

st.line_chart(chartData)
