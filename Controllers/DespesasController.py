import Services.database as db;
import streamlit as st;
import Controllers.DespesasController as DespesasController;
import Models.Despesas as despesas;

def Incluir(despesa):
    count = db.cursor.execute("""INSERT INTO DESPESAS (valor_desp, categoria_desp, descricao_desp) VALUES (?,?,?)""", despesa.valor, despesa.categoria, despesa.descricao).rowcount
    db.cnxn.commit()

def Excluir(id):
    count = db.cursor.execute("""
     DELETE FROM DESPESAS WHERE id_desp = ?""",
    id).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM DESPESAS")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(despesas.Despesas(row[0], row[1], row[2], row[3]))

    return costumerList