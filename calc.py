import streamlit as st

st.title("My Basic Calculator - Veeranna")

def square(x):
    return x*x

number = st.number_input("Insert a number")
#st.write("The current number is ", number)

# st.button("Get square", type="primary")
if st.button("Get square"):
    res = square(number)
    st.header(res)
else:
    st.write("Goodbye")

