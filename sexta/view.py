from ncliente import NCliente
from cliente import Cliente

class View:
    @classmethod
    def ClienteInserir(cls, nome, email, fone):    
        cliente = Cliente(0, nome, email, fone)
        NCliente.inserir(cliente)
        NCliente.salvar()

    @classmethod
    def ClienteListar(cls):
        cls.ClienteAbrir()
        return NCliente.listar()

    @classmethod
    def ClienteAbrir(cls):
        NCliente.abrir()

    @classmethod
    def ClienteAtualizar(cls, id, nome, email, fone):
        cls.ClienteListar()   
        NCliente.atualizar(id, nome, email, fone)
        NCliente.salvar()
        
    @classmethod
    def ClienteExcluir(cls):
        NCliente.excluir(id)
        NCliente.salvar()    