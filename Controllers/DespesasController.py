import services.database as db;
import streamlit as st;
import Controllers.DespesasController as DespesasController;

def Incluir(despesa):
    count = db.cursor.execute("""INSERT INTO despesas (valor_desp, categoria_desp, descricao_desp) VALUES (?,?,?)""", despesa.valor, despesa.categoria, despesa.descricao).rowcount
    db.cnxn.commit()