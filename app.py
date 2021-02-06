
import pandas as pd
import numpy as np
import streamlit as st
import requests
from io import StringIO

import app1
import app2
import homeapp

# insert new pages here to display on navigation bar
PAGES = {
    "Home":homeapp,
    "Python-PPTX": app1,
    "Python Functions": app2
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
