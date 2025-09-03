import streamlit as st


#--- HERO SECTION---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.logo("assets/profile.jpg")

with col2:
    st.title("Amidou Nahimana", anchor=False)
    st.subheader("Master en Developpement rural et Agrobusiness")
    st.write("Consultant et Analyste de données assistant les entreprises et les particuliers à prendre des décisions éclairées basées sur des données fiables")
#--- Experience & Qualifications
st.subheader("💻 Compétences Techniques", anchor=False)
st.markdown("""
    **🔹SQL:** 
    - Extraction des données
    - Nettoyage et agrégation de données
    - Création de bases de données relationnelles.
    - Optimisation de requêtes sur PostgreSQL, MySQL, SQLite, etc.
    
    **🔹Python:**
    - Manipulation de données avec Pandas (nettoyage, feature engineering)
    - Analyse de données
    - Visualisation avec Matplotlib, Seaborn, Plotly, 
    - Déploiement d’applications interactives avec Streamlit.

    **🔹Excel avancé:** 
    - Formules avancées
    - Tableaux croisés dynamiques(Analyse multidimensionnelle)
    - Tableaux de bord (Création de rapports dynamiques).

    **🔹Analyse de Données et Visualisation:**
    - Création de Dashboards(Excel, Streamlit)
    - Statistiques descriptives (moyenne, écart-type, corrélations)
    - Statistiques inférentielles
    """)

st.subheader("🎯 Qualifications & Expériences")
st.write("""
    **📂 Projets Data Analyse:** 
    - [Analyses statistiques avec Pandas]("views/insurance.py") 
    - [Analyse des ventes avec SQL]("views/retail_sales_sql")
    - [Analyse et Visualisation des donnees de ventes avec Pandas et Plotly]("views/sales_analyse.py")
         
    **📌 Soft Skills:**
    - Résolution de problèmes orientée données.
    - Capacité à traduire des besoins métier en analyses techniques.
    - Autonomie et gestion de projets data.
""")

# Section Contact
st.subheader("💌 Contactez-moi")
#Use local CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



contact_form = '''
<form action="c304fc50610484fbfc317177d438c9f5" method="POST">
    <div class="form-group">
        <label for="nom">Nom complet</label>
        <input type="text" id="nom" name="nom" required>
    </div>
    <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" name="email" required>
    </div>
    <div class="form-group">
        <label for="message">Message</label>
        <textarea id="message" name="message" rows="5" required></textarea>
    </div>
    <button type="submit">Envoyer</button>
</form>
'''
st.markdown(contact_form, unsafe_allow_html=True)



load_css("style/style.css")
