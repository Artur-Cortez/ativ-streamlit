import json
class Servico:
  def __init__(self, id, descricao, valor, duracao):
    self.__id, self.__descricao = id, descricao
    self.__valor, self.__duracao = valor, duracao #duracao é do tipo int

  def set_id(self, id): self.__id = id
  def get_id(self): return self.__id
  
  def set_descricao(self, descricao):
    self.__descricao = descricao

  def get_descricao(self): return self.__descricao

  def set_valor(self, valor):
    self.__valor = valor

  def get_valor(self): return self.__valor

  def set_duracao(self, duracao):
    self.__duracao = duracao

  def get_duracao(self): return self.__duracao

  def __str__(this):
    return f'ID: {this.__id}\nDescrição: {this.__descricao}\nValor: {this.__valor}\nDuração: {this.__duracao}'

  import json

class NServico:
  __servicos = []

  @classmethod
  def inserir(cls, s):
    
    id = 0
    for servico in cls.__servicos:
      if servico.get_id() > id:  id = servico.get_id()
        
    s.set_id(id+1)
   
    cls.__servicos.append(s)
    cls.salvar()

  @classmethod
  def listar_id(cls, id):
    for i in cls.__servicos:
      if i.get_id() == id:
        return i
        
  @classmethod
  def listar(cls):
    print('-----LISTA SERVIÇOS-----\n')
    return cls.__servicos

  @classmethod
  def atualizar(cls, obj):
    s = cls.listar_id(obj.get_id())    
    s.set_descricao(obj.get_descricao())
    s.set_valor(obj.get_valor())
    s.set_duracao(obj.get_duracao())
    cls.salvar()
  
  @classmethod
  def abrir(cls):
    cls.__servicos = []
    with open("list_rev_07_crud/lista_servicos.json", "r") as arquivo:
     
     horarios_json = json.load(arquivo)
     
     for obj in horarios_json:
       s = Servico(obj["_Servico__id"], obj["_Servico__descricao"], obj["_Servico__valor"], obj["_Servico__duracao"] )
       cls.__servicos.append(s)

  @classmethod
  def salvar(cls):
     with open("list_rev_07_crud/lista_servicos.json", "w") as arquivo:
       json.dump(cls.__servicos, arquivo, indent=4, default = vars)

  @classmethod
  def excluir(cls, obj):
    s = cls.listar_id(obj.get_id())
    cls.__servicos.remove(s)
    cls.salvar()

