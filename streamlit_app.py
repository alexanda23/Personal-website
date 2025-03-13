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
    icon=":material/search"
)



pg = st.navigation({
    "Info": [about_page],
    "Projects": [project_1_page]
})


st.sidebar.text("Made with 👩🏿‍🦰 by Alexander T.")


pg.run()


