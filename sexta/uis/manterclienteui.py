import streamlit as st
from views import View
import pandas as pd


class ManterClienteUI:

    @classmethod
    def main(cls):
        st.title("Cadastro de Clientes")
        cls.tab1, cls.tab2, cls.tab3, cls.tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        cls.Listar()
        cls.Inserir()
        cls.Atualizar()
        cls.Excluir()
        
    @classmethod
    def Listar(cls):       
            
        with cls.tab1:
            clientes = View.ClienteListar()
            cliente_data = [{"ID": c.get_id(), "Nome": c.get_nome(), "Email": c.get_email(), "Fone": c.get_fone()} for c in clientes]
            df = pd.DataFrame(cliente_data)
            st.dataframe(df)
    
    @classmethod
    def Inserir(cls):            
        with cls.tab2:
            nome = st.text_input("Informe o nome")
            email = st.text_input("Informe o email")
            fone = st.text_input("Informe o fone")
            inserir = st.button("Inserir")

            if inserir:
                View.ClienteInserir(nome, email, fone)
                

    @classmethod
    def Atualizar(cls):
        with cls.tab3:
            clientes = View.ClienteListar()
            
            opcoes = st.selectbox("Atualização de clientes", clientes)

            nome = st.text_input("Informe o novo nome")
            email = st.text_input("Informe o novo email")
            fone = st.text_input("Informe o novo fone")
            atualizar = st.button("Atualizar")

            if atualizar:   
                st.write(nome)
                View.ClienteAtualizar(opcoes.get_id(), nome, email, fone)

    @classmethod
    def Excluir(cls):
        with cls.tab4:
            clientes = View.ClienteListar()
            
            opcoes = st.selectbox("Atualização de clientes", clientes)
            excluir = st.button("Excluir")
            
            if excluir:
                View.ClienteExcluir(opcoes.get_id())