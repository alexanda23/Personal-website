import streamlit as st
from form.contact import contact_form

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")


with col1:
    st.image("./assets/alexlin.png", width=200)

with col2:
    st.title("Alexander Thong", anchor=False)
    st.write(
        "Student at Taipei European School"
    )

    if st.button("✉️ Contact Me"):
        contact_form()

st.write("\n")
st.subheader("Education", anchor=False)
st.write(
    """
    
-  Student of Southview Primary School, Singapore, (Graduated: 2020)
-   Student of Taipei European School (Graduating: 2027)"""
)

st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    
-  Language: Chinese, English
-  Programming: Python
-  Expertise: Simple coding and webscraping to some extent
"""
)

st.write("\n")
st.subheader("Hobbies", anchor=False)
st.write(
    """
    
-  Playing Brawl Stars
-  Watching brainrot
-  Gooning
"""
)










