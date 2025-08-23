import streamlit as st
import pandas as pd
import plotly.express as px
from numerize.numerize import numerize 

st.subheader("🏢 Analyse descriptive de l'assurance")
st.markdown('##')

## load file
df = pd.read_excel('docs/data.xlsx')
st.dataframe(df.head())
# switcher
st.sidebar.header('Please filter')
region = st.sidebar.multiselect('Select Region', options= df['Region'].unique(),default=df['Region'].unique())
location = st.sidebar.multiselect('Select Location', options= df['Location'].unique(),default=df['Location'].unique())
construction = st.sidebar.multiselect('Select Construction', options= df['Construction'].unique(),default=df['Construction'].unique())

#--------
df_selection = df.query('Region==@region & Location==@location & Construction==@construction')

#Expander

def Home():
    with st.expander('Tabular'):
        showData = st.multiselect('Filter:', df_selection.columns, default=[])
        st.write(df_selection[showData])
    #compute top analytics
    total_investment = float(df_selection['Investment'].sum())
    investment_mode = float(df_selection['Investment'].mode())
    investment_mean = float(df_selection['Investment'].mean())
    investment_median = float(df_selection['Investment'].median())
    rating = float(df_selection['Rating'].sum())

    #------
    total1,total2,total3,total4,total5 = st.columns(5, gap='large')
    with total1:
        st.info('Invest. total', icon='📌')
        st.metric(label='somme TZS', value=f'{total_investment:,.0f}')
    
    with total2:
        st.info('Plus fréquent', icon='📌')
        st.metric(label='mode TZS', value= f'{investment_mode:,.0f}')

    with total3:
        st.info('Moyenne', icon='📌')
        st.metric(label='moyenne TZS', value=f'{investment_mean:,.0f}')
    
    with total4:
        st.info('Gains centraux', icon='📌')
        st.metric(label='médiane TZS', value=f'{investment_median:,.0f}')
    
    with total5:
        st.info('Ratings', icon='📌')
        st.metric(label='Rating', value= numerize(rating), help= f"""  Total rating{rating}  """)
    st.markdown("""---""")


#Graphs display
def graphs():
    investment_by_business_type = df_selection.groupby('BusinessType').count()[['Investment']].sort_values(['Investment'])
    fig_investment = px.bar(investment_by_business_type, 
                            y= investment_by_business_type.index,
                              x='Investment',
                              orientation ='h',
                              title= "<b> Investissement par Type d'affaires </b>"
                              )
    
    investment_state = df_selection.groupby('State').count()['Investment']
    fig_state = px.line(investment_state, 
                        x=investment_state.index, 
                        y='Investment',
                        orientation='v',
                        title='<b> Investissement par zone géo</b>'
                        )

    left,right = st.columns(2)
    left.plotly_chart(fig_state, use_container_width=True)
    right.plotly_chart(fig_investment, use_container_width=True)

Home()
graphs()

