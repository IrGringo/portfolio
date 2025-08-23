import streamlit as st



#---PAGE SETUP---
about_page = st.Page(
    page="views/about_me.py",
    title="About me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page="views/sales_analysis.py",
    title="Sales analysis",
    icon=":material/bar_chart:",
)

project_2_page = st.Page(
    page="views/insurance.py",
    title="Insurance Descriptive Analytics",
    icon=":material/bar_chart:",
)

project_3_page = st.Page(
    page="views/retail_sales_sql.py",
    title="Sales analysis with SQL",
    icon=":material/bar_chart:",
)

#--- NAGIGATION SETUP[WITHOUT SECTIONS]---
#pg = st.navigation(pages=[about_page, project_1_page, project_2_page, project_3_page, project_4_page])

#--- NAGIGATION SETUP[WITHOUT SECTIONS]---
pg = st.navigation({
    "Info": [about_page],
    "Projects":[project_1_page, project_2_page, project_3_page]
})

#--- SHARED ON ALL PAGES---
st.logo("assets/profile.jpg")

#---RUN NAVIGATION---
pg.run()