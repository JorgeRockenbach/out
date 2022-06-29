from os import write
import streamlit as st;
import Pages.Adicionar as adicionarDespesas;
import Pages.List as listDespesas;

#Flyway flyway = Flyway.configure().dataSource("jdbc:mysql://localhost:3306/out", "root", "root").load()
#flyway.migrate() 


st.sidebar.title('Menu')
Page = st.sidebar.selectbox('Despesas', ['Adicionar', 'Consultar'])

if Page == 'Consultar':
    listDespesas.Lista()

if Page == 'Adicionar':
    adicionarDespesas.adicionar()
