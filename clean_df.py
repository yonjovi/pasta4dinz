from textwrap import wrap
import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import pandas as pd

recipez = pd.read_csv('VINCENZO_REAL_RECIPES_NEW.csv')



recipez['Ingredients'] = recipez['Ingredients'].str.split('Utensils').str[0]

recipez['Ingredients'] = recipez['Ingredients'].str.split('UTENSILS').str[0]
recipez['Ingredients'] = recipez['Ingredients'].str.split('utensils').str[0]
recipez['Ingredients'] = recipez['Ingredients'].str.split('Instructions').str[0]
recipez['Ingredients'] = recipez['Ingredients'].str.split('INSTRUCTIONS').str[0]
recipez['Ingredients'] = recipez['Ingredients'].str.split('instructions').str[0]
recipez['Ingredients'] = recipez['Ingredients'].str.split('Method').str[0]
recipez['Ingredients'] = recipez['Ingredients'].str.split('METHOD').str[0]
recipez['Ingredients'] = recipez['Ingredients'].str.split('method').str[0]

print(recipez)


# recipez.to_csv('testing_clean_data.csv')