import streamlit as st
from views import View
import pandas as pd

class ManterHorarioUI:

    @classmethod
    def main(cls):
        st.title("Cadastro de Horários")
        cls.tab1, cls.tab2, cls.tab3, cls.tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        cls.Listar()
        cls.Inserir()
        cls.Atualizar()
        cls.Excluir()
        
    @classmethod
    def Listar(cls):       
            
        with cls.tab1:
            horarios = View.HorarioListar()
            horarios_data = [{"ID": h.get_id(), "Data": h.get_nome(), "Confirmado": h.get_confirmado(), "idCLiente": h.get_idCliente(), "idServico": h.get_idServico()} for h in horarios]
            df = pd.DataFrame(horarios_data)
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
            horarios = View.HorarioListar()
            
            opcoes = st.selectbox("Atualização de horários", horarios)

            data = st.text_input("Informe a nova descrição")
            confirmado = st.checkbox()
            # # duracao = st.text_input("Informe a nova duracao")
            # # atualizar = st.button("Atualizar")

            # if atualizar:
            #     View.ServicoAtualizar(opcoes.get_id(), desc, valor, duracao)

    @classmethod
    def Excluir(cls):
        with cls.tab4:
            horarios = View.HorarioListar()
            
            opcoes = st.selectbox("Exclusão de horários", horarios)
            excluir = st.button("Excluir")
            
            if excluir:
                View.HorarioExcluir(opcoes.get_id())