import json
from cliente import Cliente

class NCliente: 
  __clientes = [] #lista de dicionarios

  @classmethod
  def inserir(cls, c):
    
    id = 0
    for cliente in cls.__clientes:
      if cliente.get_id() > id:  id = cliente.get_id()
        
    c.set_id(id+1)
   
    cls.__clientes.append(c)    
    
  @classmethod
  def listar_id(cls, id):
    for i in cls.__clientes:
      if i.get_id() == id:
        return i
        
  @classmethod
  def listar(cls):
    # print('-----LISTA CLIENTES-----\n')
    return cls.__clientes
      
  @classmethod
  def atualizar(cls, id, nome='', email='', fone=''):
    c = cls.listar_id(id)
    
    if nome == '': pass      
    else: 
      c.set_nome(nome)
      
    if email == '': pass
    else:
      c.set_email(email)
      
    if fone == '': pass
    else:
      c.set_fone(fone)

  @classmethod        
  def excluir(cls, id):
    c = cls.listar_id(id)
    cls.__clientes.remove(c)    

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