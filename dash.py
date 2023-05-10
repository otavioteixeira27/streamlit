import streamlit as st
import pandas as pd
import numpy as np

st.subheader('Number of pickups by hour')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, range=(0,24))[0]

st.bar_chart(hist_values)
