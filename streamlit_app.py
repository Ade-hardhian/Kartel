import streamlit as st
import pandas as pd
import math
from pathlib import Path
from streamlit_gsheets import GSheetsConnection
url= "https://docs.google.com/spreadsheets/d/1K9c8RuEmUI2yTrhZU1ZLEy2jSbjmStyFU5DNPkNTRpg/edit?usp=sharing"
# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spredsheet=url)

# Print results.
for row in df.itertuples():
    st.write(df)
