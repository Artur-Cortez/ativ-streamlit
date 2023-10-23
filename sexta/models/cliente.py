class Cliente:
  def __init__(self, id, nome, email, fone):
    self.__id, self.__nome, self.__email, self.__fone = id, nome, email, fone

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome == nome
  def set_email(self, email): self.__email = email
  def set_fone(self, fone): self.__fone = fone

  def get_id(self):  return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_fone(self): return self.__fone

  def __eq__(self, o: object):
      if self.__id == o.__id and self.__nome == o.__nome and self.__email == o.__email and self.__fone == o.__fone:
        return True
      return False

  def __str__(self):
    return f'\nID: {self.__id}\nNome: {self.__nome}\nEmail: {self.__email}\nTelefone: {self.__fone}'

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
