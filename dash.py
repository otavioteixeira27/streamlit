import streamlit as st
import pandas as pd
import numpy as np

st.subheader('Map of all pickups')

st.map(data)

st.subheader('Map of all pickups')
st.map(data)

hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h

st.subheader('Raw data')
st.write(data)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
