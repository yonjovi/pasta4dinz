import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import pandas as pd

recipez = pd.read_csv('VINCENZO_REAL_RECIPES_NEW.csv')

st.header("Lets eat some pasta!")
st.text("Enter ingredients you wish to use and find some pasta inspiration 🍝")

ingredients = st_tags(
    label='# Enter Ingredients:',
    text='Press enter to add more',
    value=[],
    suggestions=['pecorino', 'tomato', 'cherry', 'pancetta', 'bolognese', 'pork', 'chicken', 'mushroom', 'beef'],
    maxtags=8,
    key='1')

st.write(ingredients)

if ingredients:
    for i, row in recipez.iterrows():
        if all(ing in row[3] for ing in ingredients):
            st.write(f"[{row[1]}](%s)" % row[2])
            # st.write("Recipe Link:", row[2])



# input_list = []

# while True:
#     ingredient = input("Please enter an ingredient: ")
#     input_list.append(ingredient)
#     add_more = input("Would you like to add more? (Y/N)  ")
#     if add_more.lower() == "n":
#         break
# print(input_list)
#


#
# for i, row in recipez.iterrows():
#     if all(ing in row[3] for ing in input_list):
#         print("Recipe name:", row[1])
#         print("Recipe Link:", row[2])

# for i, row in recipez.iterrows():
#     check = any(item in input_list for item in row[3])
#     if check:
#         print("Recipe name:", row[1])
#         print("Recipe Link:", row[2])
#
# for i, row in recipez.iterrows():
#     if input_list[0:] in row[3]:
#         print("Recipe name:", row[1])
#         print("Recipe Link:", row[2])
