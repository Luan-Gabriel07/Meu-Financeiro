import streamlit as st

st.title ("Meu Financeiro")
st.write("Bem-Vindo ao meu controle financeiro")
st.subheader("Visão geral")
st.metric(
    label="Saldo atual",
    value="R$ 0,00"
)