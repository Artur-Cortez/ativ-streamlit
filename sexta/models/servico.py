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
