class Horario: 
  def __init__(self, id, data, confirmado, idCliente, idServico):
    self.__id, self.__data = id, data
    self.__confirmado, self.__idCliente = confirmado, idCliente
    self.__idServico = idServico

  def set_id(self, id):
    self.__id = id
    
  def get_id(self):
    return self.__id

  def set_data(self, data):
    self.__data = data
  
  def get_data(self):
    return self.__data
  
  def set_confirmado(self, status_de_confirmacao):
    self.__confirmado = status_de_confirmacao

  def get_confirmado(self): return self.__confirmado

  def set_idCliente(self, idCliente):
    self.__idCliente = idCliente

  def get_idCliente(self): return self.__idCliente

  def get_idServico(self): return self.__idServico

  def set_idServico(self, idServico):
    self.__idServico = idServico

  def __str__(self):
    return f'ID do horário: {self.__id}\nData: {self.__data}\nConfirmado: {self.__confirmado}\nID do cliente: {self.__idCliente}\nID do serviço: {self.__idServico}\n'