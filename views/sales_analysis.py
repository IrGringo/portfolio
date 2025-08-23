import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


#set page configuration
st.set_page_config(page_title='Analyse des ventes', layout='centered')
#title
st.header("Analyse des ventes d'Appareils électroniques et Accessoires")
#load dataframe
@st.cache_data
def load_data():
    return pd.read_csv('docs/sales_analysis.csv')
            
df_sales = load_data()

st.dataframe(df_sales.head())

#Display bar plot for months
@st.cache_data
def display_month():
    st.subheader('Analyse des ventes par mois')
    sales_month = df_sales.groupby('Month')['Sales'].sum().sort_values().reset_index()
    st.dataframe(sales_month)
    fig_month = px.bar(sales_month, x='Month', y='Sales')
    st.plotly_chart(fig_month)

#display bar plot for cities
@st.cache_data
def display_city():
    st.subheader('Dans quelle ville on enregistre plus de ventes?')
    #Extraire la ville du dataframe
    df_sales.loc[:,'City'] = df_sales['Purchase Address'].apply(lambda x: x.split(',')[1])
    counts_city = df_sales.groupby('City')['Sales'].sum().sort_values().reset_index()
    st.dataframe(counts_city)
    fig_city = px.bar(counts_city, x='City', y='Sales', color_discrete_sequence=["#99A123"])
    st.plotly_chart(fig_city)

#display line plot for time
@st.cache_data
def display_time():
    st.subheader('A quel moment doit-on faire une campagne publicitaire pour avoir plus de ventes?')
    df_sales.loc[:,'Hour'] = pd.to_datetime(df_sales['Order Date']).dt.hour
    keys=[]
    hours=[]
    for key,hour in df_sales.groupby('Hour'):
        keys.append(key)
        hours.append(len(hour))
    fig_hour = px.line(hours)
    fig_hour.update_layout(
            title='Determination du pic de temps',
            xaxis_title = 'Heure de la journee',
            yaxis_title = 'Nombre de commandes',
            legend_title = 'heure'
            )
    st.plotly_chart(fig_hour)

@st.cache_data
def display_product():
    st.subheader('Quel produit se vend le plus?')
    df_sales_product = df_sales.groupby('Product', as_index=False)['Quantity Ordered'].sum().sort_values(by='Quantity Ordered', ascending=False)
    products = df_sales_product['Product']
    quantity = df_sales_product['Quantity Ordered']
    mean_prices = df_sales.groupby('Product')['Price Each'].mean()
    st.dataframe(df_sales_product)
    fig_product = make_subplots(specs=[[{'secondary_y':True}]])
    fig_product.add_trace(go.Bar(x=products, y=quantity, name='Quantite'),secondary_y=False)
    fig_product.add_trace(go.Scatter(x=products, y=mean_prices, name='Prix moyen', line=dict(color='green', width=2)),secondary_y=True)
    fig_product.update_layout(title='Quantite et prix par produit', xaxis_title= 'Produit', 
                              yaxis= dict(title='Quantite'),
                              yaxis2= dict(title='Prix'))
    st.plotly_chart(fig_product)

@st.cache_data    
def combinaisons_produits():
    st.subheader('Quelles combinaisons de produits se vendent le plus?')
    df_sales['Grouped'] = df_sales.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
    df_sales_comb = df_sales.drop_duplicates(subset=['Order ID'])
    df_sales_comb_freq = df_sales_comb['Grouped'].value_counts().reset_index().rename(columns={'index':'Produits'})[0:5]
    st.dataframe(df_sales_comb_freq)
    fig_comb = px.pie(df_sales_comb_freq, values='Grouped', names='Produits')
    fig_comb.update_layout(title='Part de marche des 5 produits les plus vendus')
    st.plotly_chart(fig_comb)







display_month()
display_city()
display_time()
display_product()
combinaisons_produits()





