import streamlit as st;
import Controllers.DespesasController as DespesasController;
import models.Despesas as Despesas;

st.title("Adicionar Despesas")

with st.form(key="include_despesas"):
    input_valor = st.number_input(label="Insira o Valor da Despesa")
    input_categoria = st.selectbox(label="Selecione a categoria da sua Despesa", options=["Água","Luz","Escola","Telefone","Gás","Aluguel","Internet","Gasolina","Alimentação","Festas","Viagens","Investimentos","Outros"])
    input_descricao = st.text_input(label="Descreva sua Despesa")

    input_botao = st.form_submit_button("Adicionar")

if input_botao:
    Despesas.valor = input_valor
    Despesas.categoria = input_categoria
    Despesas.descricao = input_descricao

    DespesasController.Incluir(Despesas)
    st.success("Despesa Adicionada com Sucesso")