import streamlit as st

st.title('Hello to our wage app :sunglasses:')
hours = st.number_input('Insert hours')
rate = st.number_input('Insert rate')

def calc_wage(hour,rate):
    return hour*rate


if st.button('Calculate your wage'):
    result = calc_wage(hours, rate)
    st.write('Your wage is: ', result)
