import streamlit as st;
import Controllers.DespesasController as DespesasController
from Models.Despesas import Despesas;
import pandas as pd;

def Lista():
    colms = st.columns((1,2,2,3,2,2))
    campos = ['Id','Valor','Categoria','Descricao', 'Excluir', 'Alterar']
    for col, campo_valor in zip(colms, campos):
        col.write(campo_valor)

    for item in DespesasController.SelecionarTodos():
        col1, col2, col3, col4, col5, col6 = st.columns((1,2,2,3,2,2))
        col1.write(item.id)
        col2.write(item.valor)
        col3.write(item.categoria)
        col4.write(item.descricao)
        button_space_excluir = col5.empty()
        on_click_excluir = button_space_excluir.button('Excluir','btnExcluir' + str(item.id))
        button_space_alterar = col6.empty()
        on_click_alterar = button_space_alterar.button('Alterar','btnAlterar' + str(item.id))

        if on_click_excluir:
            DespesasController.Excluir(item.id)
            button_space_excluir.button('Excluido','btnExcluir' + str(item.id))

        if on_click_alterar:
            DespesasController.Excluir(item.id)
            button_space_excluir.button('Alterar','btnAlterar' + str(item.id))
        