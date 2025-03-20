import streamlit as st

about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True #first page user will see

)


project_1_page = st.Page(
    "views/chat_bot.py",
    title="Chat_bot",
    icon=":material/smart_toy:"
)


project_2_page = st.Page(
    "views/ai_web_scrape.py",
    title="AI Web Scraper",
    icon=":material/search:"
)

project_3_page = st.Page(
    "views/pdf_to_png.py",
    title="PDF to PNG Converter",
    icon=":material/picture_as_pdf:"
)


pg = st.navigation({
    "Info": [about_page],
    "Projects": [project_1_page, project_2_page, project_3_page]
})


st.sidebar.text("Made with 👩🏿‍🦰 by Alexander T.")


pg.run()


