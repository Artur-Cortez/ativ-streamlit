from uis.manterclienteui import ManterClienteUI
from uis.manterhorarioui import ManterHorarioUI
from uis.manterservicoui import ManterServicoUI
import streamlit as st

class IndexUI:
    
    @classmethod
    def sidebar(cls):
        op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda"])
        if op == "Manter Clientes": ManterClienteUI.main()
        if op == "Manter Serviços": ManterServicoUI.main()
        if op == "Manter Agenda": ManterHorarioUI.main()
    
    @classmethod
    def main(cls):
        cls.sidebar()
        if "page" not in st.session_state: st.session_state["page"] = "manter_ClienteUI"
        if st.session_state["page"] == "manter_clienteUI": ManterClienteUI.main()
 
        


IndexUI.main()