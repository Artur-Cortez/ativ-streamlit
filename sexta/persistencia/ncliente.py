import json
from models.cliente import Cliente

class NCliente: 
  __clientes = [] #lista de dicionarios

  @classmethod
  def inserir(cls, c):
    
    id = 0
    for cliente in cls.__clientes:
      if cliente.get_id() > id:  id = cliente.get_id()
        
    c.set_id(id+1)
   
    cls.__clientes.append(c)
    cls.salvar()   
    
  @classmethod
  def listar_id(cls, id):
    for i in cls.__clientes:
      if i.get_id() == id:
        return i
        
  @classmethod
  def listar(cls):
    cls.abrir()
    # print('-----LISTA CLIENTES-----\n')
    return cls.__clientes
      
  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    c = cls.listar_id(obj.get_id())
    
    if c is not None:
      c.set_nome(obj.get_nome())
      c.set_email(obj.get_email())
      c.set_fone(obj.get_fone())

    cls.salvar()
    

  @classmethod        
  def excluir(cls, obj):
    c = cls.listar_id(obj.get_id())
    cls.__clientes.remove(c)    
    cls.salvar()

  @classmethod
  def salvar(cls):
     with open("sexta/lista_clientes.json", "w") as arquivo:
       
       json.dump(cls.__clientes, arquivo, indent=4, default = vars)

  @classmethod
  def abrir(cls):
    cls.__clientes = []
    with open("sexta/lista_clientes.json", "r") as arquivo:
     clientes_json = json.load(arquivo)
     for obj in clientes_json:
       c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"], obj["_Cliente__email"], obj["_Cliente__fone"])
       cls.__clientes.append(c)