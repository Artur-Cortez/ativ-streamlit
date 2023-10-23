from persistencia.ncliente import NCliente
from persistencia.nservico import NServico
from persistencia.nhorario import NHorario

from models.cliente import Cliente
from models.servico import Servico
from models.horario import Horario


class View:
    @classmethod
    def ClienteInserir(cls, nome, email, fone):    
        cliente = Cliente(0, nome, email, fone)
        NCliente.inserir(cliente)

    @classmethod
    def ClienteListar(cls):
        return NCliente.listar()

    @classmethod
    def ClienteAtualizar(cls, id, nome, email, fone):
        NCliente.atualizar(id, nome, email, fone)
        
    @classmethod
    def ClienteExcluir(cls, id):
        cliente = Cliente(id, "", "", "")
        NCliente.excluir(cliente)



    @classmethod
    def ServicoInserir(cls, desc, valor, duracao):    
        cliente = Servico(0, desc, valor, duracao)
        NCliente.inserir(cliente)

    @classmethod
    def ServicoListar(cls):
        return NServico.listar()

    @classmethod
    def ServicoAtualizar(cls, id, desc, valor, duracao):
        obj = Servico(id, desc, valor, duracao)
        NCliente.atualizar(obj)
        
    @classmethod
    def ServicoExcluir(cls, id):
        servico = Servico(id, "", "", "")
        NServico.excluir(servico)



    @classmethod
    def HorarioInserir(cls, data, confirmado, idCliente=0, idServico=0):    
        horario = Horario(0, data, confirmado, idCliente, idServico)
        NHorario.inserir(horario)

    @classmethod
    def HorarioListar(cls):
        return NHorario.listar()

    @classmethod
    def HorarioAtualizar(cls, id, data, confirmado, idCliente, idServico):
        obj = Horario(id, data, confirmado, idCliente, idServico)
        NCliente.atualizar(obj)
        
    @classmethod
    def HorarioExcluir(cls, id):
        horario = Horario(id, "", "", "")
        NHorario.excluir(horario)

    @classmethod
    def Agenda_Abrir_Agenda_do_Dia(cls, data, hora_inicio, hora_fim, intervalor):
        pass

    
     