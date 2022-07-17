# import pandas as pd
# import streamlit as st

# # Show the title of our application
# st.markdown("# Demonstrating use of Next button with Session State")

# # Read the data
# data = pd.read_csv("addresses.csv")

# # Render the dataframe to main screen
# st.write(data)

import SessionState
import pandas as pd
import streamlit as st

# Number of entries per screen
N = 15

st.markdown("# Demonstrating use of Next button with Session State")

# Read the table and initialize page number to zero to view the first N entries in dataframe
page_number = 0
data = pd.read_csv("auto-mpg.csv")
last_page = len(data) // N

# Add a next button and a previous button

prev, _ ,next = st.beta_columns([1, 10, 1])

if next.button("Next"):

    if page_number + 1 > last_page:
        page_number = 0
    else:
        page_number += 1

if prev.button("Previous"):

    if page_number - 1 < 0:
        page_number = last_page
    else:
        page_number -= 1

# Get start and end indices of the next page of the dataframe
start_idx = page_number * N 
end_idx = (1 + page_number) * N

# Index into the sub dataframe
sub_df = data.iloc[start_idx:end_idx]
st.write(sub_df)