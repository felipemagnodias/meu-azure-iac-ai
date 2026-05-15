import streamlit as st
import requests

st.title("🤖 Azure IaC Creator")
st.subheader("O que você deseja criar hoje?")

# Campo de texto para o usuário
user_input = st.text_area("Descreva seu recurso (Ex: 'Crie uma rede virtual com 3 subnets')", "")

if st.button("Gerar e Implantar"):
    if user_input:
        st.info("Processando seu pedido com IA...")
        # Chamada para a sua Azure Function (Substitua pela sua URL da Função)
        func_url = "funciaciaazure-epbpdjd7bte2gne3.eastus-01.azurewebsites.net/api/generate"
        response = requests.post(func_url, json={"prompt": user_input})
        
        if response.status_code == 200:
            st.success("Infraestrutura gerada com sucesso!")
            st.code(response.json()['bicep_code'], language='bicep')
        else:
            st.error("Erro ao processar o pedido.")
