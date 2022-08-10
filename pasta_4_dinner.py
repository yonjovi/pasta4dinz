from textwrap import wrap
import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import pandas as pd

st.markdown("""
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
    """, unsafe_allow_html=True)
recipez = pd.read_csv('testing_clean_data.csv')

st.title("Lets eat some pasta! 🍝")
st.text("Go on then...check your pantry or fridge")

ingredients = st_tags(
    label='# Enter Ingredients:',
    text='Press enter to add more',
    value=[],
    suggestions=['pecorino', 'tomato', 'cherry', 'pancetta', 'bolognese', 'pork', 'chicken', 'mushroom', 'beef', 'basil', 'ricotta', 'prawn', 'egg', 'olive oil', 'butter'],
    maxtags=8,
    key='1')

# st.write(ingredients)

ingredients_lower_list = []

for ing in ingredients:
    ing = ing.lower()
    ingredients_lower_list.append(ing)

search_result_dict = {}
# search_result_dict["Recipe Index"] = {}
recipe_dict = {}

recipe_results_title = []
recipe_results_link = []
recipe_results_ings = []
recipe_results_img = []

# results_df = pd.DataFrame
if ingredients_lower_list:
    st.text("And the results...🥁🥁🥁")
    # results_df = pd.DataFrame(columns=['Title', 'Link', 'Ingredients', 'img_links'])
    for i, row in recipez.iterrows():
        if all(ing in row[3].lower() for ing in ingredients_lower_list):
            recipe_title = row[1]
            recipe_link = row[2]
            recipe_ing = row[3]
            recipe_img = row[4]
            # st.write(f"[{row[1]}](%s)" % row[2])
            # st.image(row[4])
            recipe_results_title.append(recipe_title)
            recipe_results_link.append(recipe_link)
            recipe_results_ings.append(recipe_ing)
            recipe_results_img.append(recipe_img)
    results_df = pd.DataFrame(list(zip(recipe_results_title, recipe_results_link, recipe_results_ings, recipe_results_img)), columns=['Title', 'Link', 'Ingredients', 'Img'])
    # st.write(recipe_results_img)
    # for i, row in results_df.iterrows():
    #     st.write(row[3])
    n_cols = 2
    # st.write(n_cols)
    n_rows = int(1 + len(recipe_results_img) / n_cols)
    rows = [st.columns(n_cols) for _ in range(n_rows)]
    cols = [column for row in rows for column in row]

    for col, img, title, link in zip(cols, recipe_results_img, recipe_results_title, recipe_results_link):
        col.write(f"[{title}](%s)" % link)
        col.image(img)
        


    # st.markdown("""
    #         <div class="carousel-item">
    #         {% for i,row in results_df.iterrows() %}}
    #             <img src={{ row[3] }} alt="...">
    #             <div class="carousel-caption d-none d-md-block">
    #                 <h5>""</h5>
    #                 <p><a href="">GO TO RECIPE</a></p>
    #             </div>
    #         {% endfor %}
    #         </div>
            
    #     """, unsafe_allow_html=True)
