import streamlit as st
from view import View
import pandas as pd
from cliente import Cliente
from ncliente import NCliente

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
            opcoes_clientes = [f"ID: {c.get_id()} Nome: {c.get_nome()} Email: {c.get_email()} Telefone: {c.get_fone()}" for c in clientes]
            
            chave_unica = hash("seu_identificador_unico_aqui")
            cliente_selecionado = st.selectbox("Atualização de clientes", opcoes_clientes, key=chave_unica)

            nome = st.text_input("Informe o novo nome")
            email = st.text_input("Informe o novo email")
            fone = st.text_input("Informe o novo fone")
            atualizar = st.button("Atualizar")

            if cliente_selecionado:
                id_cliente_selecionado = int(cliente_selecionado.split("ID: ")[1].split(" ")[0])

                if atualizar:
                    c = None
                    for cliente in clientes:
                        if cliente.get_id() == id_cliente_selecionado:
                            c = cliente
                    if c:
                        
                        View.ClienteAtualizar(c.get_id(), nome, email, fone)

    @classmethod
    def Excluir(cls):
        with cls.tab4:
            clientes = View.ClienteListar()
            opcoes_clientes = [f"ID: {c.get_id()} Nome: {c.get_nome()} Email: {c.get_email()} Telefone: {c.get_fone()}" for c in clientes]
            c_s = st.selectbox("Atualização de clientes", opcoes_clientes)
            excluir = st.button("Excluir")
            
            if c_s:
                id_cliente_selecionado = int(c_s.split("ID: ")[1].split(" ")[0])

                if excluir:
                    c = None
                    for cliente in clientes:
                        if cliente.get_id() == id_cliente_selecionado:
                            c = cliente
                    if c:
                        View.ClienteExcluir(c.get_id())