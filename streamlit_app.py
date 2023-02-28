import streamlit
import pandas 
import requests 

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"watermelon")

# take the json file and normalize it  
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it in the screen as a table
streamlit.dataframe(fruityvice_normalized)
