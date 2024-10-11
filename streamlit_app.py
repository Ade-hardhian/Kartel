import streamlit as st
import pandas as pd
import math
from pathlib import Path
from streamlit_gsheets import GSheetsConnection

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data

# Create a connection object.
conn = st.connection("streamlit_gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples():
    st.write(df)

df = conn.read(
    worksheet="Sheet1",
    ttl="10m",
    usecols=[0, 1],
    nrows=3,
)
