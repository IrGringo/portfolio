import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px



# Initialize connection
df = pd.read_csv("docs/retail_sales.csv")
conn = sqlite3.connect(":memory:")
df.to_sql("sales_data", conn, index=False, if_exists="replace")

#Affichage du dataframe
R0 = "SELECT * FROM sales_data"
st.subheader("Affichage des 10 premières lignes du tableau")
data = pd.read_sql(R0, conn)
st.dataframe(data.head(10))

#Data Analysis
R1 = "SELECT COUNT(*) FROM sales_data"
st.subheader("Combien de ventes avons-nous?")
Q1 = pd.read_sql(R1, conn)
st.table(Q1)
st.write("Nous avons 7948 ventes")

st.subheader("Combien de clients avons-nous?")
R2 = "SELECT COUNT(DISTINCT customer_id) FROM sales_data"
Q2 = pd.read_sql(R2, conn)
st.table(Q2)
st.write("Nous avons 155 clients")

st.subheader("Les ventes realisées en date du 05 Novembre 2022")
R3 = "SELECT * FROM sales_data WHERE sale_date = '2022-11-05'"
Q3 = pd.read_sql(R3, conn)
st.dataframe(Q3)
st.write("Il y a en tout 44 ventes")

st.subheader("Le total conditionnel des transactions")
R4 = """SELECT * 
	FROM sales_data 
	WHERE category = 'Clothing' AND quantity>=3 AND strftime('%Y-%m',sale_date)='2023-10'
    """
Q4 = pd.read_sql(R4, conn)
st.dataframe(Q4)
st.write("Il y a 84 transactions pour la catégorie Habillements(Clothing) lorsque la quantité vendue est supérieure à 3 pendant le mois d'Octobre")

st.subheader("Calcul des ventes totales par catégorie de produits")
R5 = "SELECT category, SUM(total_sale) AS net_sale, COUNT(*) AS total_orders FROM sales_data GROUP BY 1"
Q5 = pd.read_sql(R5, conn)
st.dataframe(Q5)
fig_Q5 = px.bar(Q5, x="category", y="net_sale", color="category", color_discrete_sequence=["#1E90FF","#32CD32","#DC143C"])
st.plotly_chart(fig_Q5)

st.subheader("Le total des ventes supérieures à 1000")
R6 = "SELECT customer_id, total_sale FROM sales_data WHERE total_sale > 1000"
Q6 = pd.read_sql(R6, conn)
st.dataframe(Q6)
st.write("1224 ventes ont été trouvées")

st.subheader("Le total des ventes selon le sexe dans chaque catégorie de produits")
R7 = "SELECT category,gender, COUNT(*) as total_trans FROM sales_data GROUP BY 1,2 ORDER BY 1"
Q7 = pd.read_sql(R7, conn)
st.dataframe(Q7)
st.markdown('''
- Dans la catégorie Beauty, on dénomrbre 1320 ventes pour Femmes et 1124 ventes pour Femmes
- Dans la catégorie Clothing, on dénombre 1388 ventes pour Femmes et 1404 ventes pour Hommes
- Dans la catégorie Electronics, on dénombre 1340 ventes pour Hommes et 1372 ventes pour Femmes
''')

st.subheader("Les ventes moyennes pour chaque mois: le mois le plus vendu chaque année")
R8 = '''
SELECT 
       year, 
	   month, 
	   avg_sale 
FROM 
(
	SELECT 
		strftime('%Y',sale_date) as year, 
		strftime('%m',sale_date) as month, 
		avg(total_sale) as avg_sale,
		RANK() OVER(PARTITION BY strftime('%Y',sale_date) ORDER BY avg(total_sale) DESC) AS rank
	FROM sales_data 
	GROUP BY 1,2
) as t1 where rank=1
'''
Q8 = pd.read_sql(R8, conn)
st.dataframe(Q8)

st.subheader("Les 5 premiers clients sur la base des ventes totales les plus élevées")
R9 = '''
SELECT 
	customer_id, 
	SUM(total_sale) as total_sales 
FROM sales_data  
GROUP BY 1 
ORDER BY 2 DESC 
LIMIT 5
'''
Q9 = pd.read_sql(R9, conn)
st.dataframe(Q9)
fig_Q9 = px.pie(Q9, names="customer_id", values="total_sales", color="customer_id")
st.plotly_chart(fig_Q9)

st.subheader("Le nombre de clients ayant acheté des produits pour chaque catégorie")
R10 = '''
SELECT 
	category,
	COUNT(DISTINCT customer_id) AS un_custom
FROM sales_data 
GROUP BY category
'''
Q10 = pd.read_sql(R10, conn)
st.dataframe(Q10)
fig_Q10 = px.bar(Q10, x="category", y="un_custom", color="category", color_discrete_sequence=["#095809","#850842","#540FA3"  ])
st.plotly_chart(fig_Q10)

st.subheader("Nombre de commandes par temps spécifique(Avant-midi, Entre 12h et 17h et Soir)")
R11 = '''
WITH hourly_sale
AS
(
SELECT *,
	   CASE 
			WHEN strftime('%H',sale_time) <= '12' THEN 'Morning' 
			WHEN strftime('%H',sale_time) BETWEEN '12' AND '17' THEN 'Afternoon' 
			ELSE 'Evening'
	   END AS shift
FROM sales_data 
)
SELECT 
	shift,
	COUNT(*) AS total_orders
FROM hourly_sale
GROUP BY shift
'''
Q11 = pd.read_sql(R11, conn)
st.dataframe(Q11)
fig_Q11 = px.pie(Q11, names="shift", values="total_orders")
st.plotly_chart(fig_Q11)






