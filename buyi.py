import streamlit as st
from streamlit import button

st.title("Meer Science Academy")
st.header("Admission Form")
name=st.text_input("Name")
age=st.text_input("Age")
fathername=st.text_input("Father name")
adr=st.text_area("enter your address")
classdata=st.selectbox("enter your class",(1,2,3,4,5,6,7,8,9,10,11,12))

button=st .button("submit")
if button :
    st.markdown("""
    Name : {name}
    Age : {age}
    Fathername : {fathername}
    Address : {adr}
    class : {classdata} 
    """)





