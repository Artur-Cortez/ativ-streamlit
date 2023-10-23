import streamlit as st
from views import View
import pandas as pd

class ManterServicoUI:

    @classmethod
    def main(cls):
        st.title("Cadastro de Servicos")
        cls.tab1, cls.tab2, cls.tab3, cls.tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        cls.Listar()
        cls.Inserir()
        cls.Atualizar()
        cls.Excluir()
        
    @classmethod
    def Listar(cls):       
            
        with cls.tab1:
            servicos = View.ServicoListar()
            servico_data = [{"ID": s.get_id(), "Desc": s.get_nome(), "Valor": s.get_valor(), "Duração": s.get_duracao()} for s in servicos]
            df = pd.DataFrame(servico_data)
            st.dataframe(df)
    
    @classmethod
    def Inserir(cls):            
        with cls.tab2:
            desc = st.text_input("Informe a descrição")
            valor = st.text_input("Informe o valor")
            duracao = st.text_input("Informe a duração")
            inserir = st.button("Inserir")

            if inserir:
                View.HorarioInserir(desc, valor, duracao)
                

    @classmethod
    def Atualizar(cls):
        with cls.tab3:
            servicos = View.ServicoListar()
            
            opcoes = st.selectbox("Atualização de clientes", servicos)

            desc = st.text_input("Informe a nova descrição")
            valor = st.text_input("Informe o novo valor")
            duracao = st.text_input("Informe a nova duracao")
            atualizar = st.button("Atualizar")

            if atualizar:
                View.ServicoAtualizar(opcoes.get_id(), desc, valor, duracao)

    @classmethod
    def Excluir(cls):
        with cls.tab4:
            servicos = View.ServicoListar()
            
            opcoes = st.selectbox("Atualização de clientes", servicos)
            excluir = st.button("Excluir")
            
            if excluir:
                View.ServicoExcluir(opcoes.get_id())