from textwrap import wrap
import base64
import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import pandas as pd

# st.markdown("""
#         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
#         <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
#     """, unsafe_allow_html=T rue)



page_bg_img = """
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

[data-testid="stAppViewContainer"] {
background-image: url("https://i.ibb.co/BrdYf0z/pastabackz.webp");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="column"] {
background: rgba(255,255,255, 0.5);
border: 25 25 round;
}

[data-testid="column"] img:hover {
background: rgba(255,255,255, 0.5);
background-color: white;
border: 25 25 round;
}


</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

recipez = pd.read_csv('testing_clean_data.csv')

st.title("Lets eat some pasta! 🍝")
st.text("Go on then...check your pantry or fridge")

ingredients = st_tags(
    label='# Enter Ingredients:',
    text='Press enter to add more',
    value=[],
    suggestions=['pecorino', 'tomato', 'cherry', 'pancetta', 'bolognese', 'pork', 'chicken', 'mushroom', 'beef', 'basil', 'ricotta', 'prawn', 'egg', 'olive oil', 'butter', 'chilli', 'tomato paste'],
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
    st.caption("")
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
        col.caption(f"{title}[🤌🤌🤌](%s)" % link)
        col.image(img, use_column_width=True)
        col.caption("")
        
column_shit = """
<style>

[data-testid="column"] {
background: rgba(255,255,255, 0.5);
}

[data-testid="column"] img:hover {
background: rgba(255,255,255, 0.5);
background-color: white;

[data-testid="stText"] {
background: rgba(255,255,255, 0.9);
}

[data-testid="stCaptionContainer"] p{
    font-color: black;
}
</style>
"""

st.markdown(column_shit, unsafe_allow_html=True)

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
