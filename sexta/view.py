from ncliente import NCliente
from cliente import Cliente

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
        NCliente.excluir(id)
     