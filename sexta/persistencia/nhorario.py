from models.horario import Horario
from persistencia.nhorario import NHorario
import json, datetime
class NHorario:
  __horarios = []

  @classmethod
  def inserir(cls, hor):
    
    id = 0
    for horario in cls.__horarios:
      if horario.get_id() > id:  id = horario.get_id()
        
    hor.set_id(id+1)
   
    cls.__horarios.append(hor)

  @classmethod
  def listar(cls): return cls.__horarios

  @classmethod
  def listar_id(cls, id):
    for i in cls.listar():
      if i.get_id() == id:
        return i

  @classmethod
  def atualizar(cls, obj):
    NHorario.abrir()
    h = cls.listar_id(obj.get_id())
    if h is not None:
        h.set_data(obj.get_data())
        h.set_confirmado(obj.get_confirmado())
        h.set_idCliente(obj.get_idCliente())
        h.set_idServico(obj.get_idServico())
  
    
  @classmethod        
  def excluir(cls, obj):
    h = cls.listar_id(obj.get_id())
    cls.__horarios.remove(h)

  @classmethod
  def salvar(cls):
    with open("list_rev_07_crud/lista_horarios.json", "w") as arquivo:

        for horario in cls.__horarios:
            horario.set_data(horario.get_data().strftime('%Y-%m-%d %H:%M:%S'))

        json.dump(cls.__horarios, arquivo, indent=4, default=vars)  

  @classmethod
  def abrir(cls):
    cls.__horarios = []
    with open("list_rev_07_crud/lista_horarios.json", "r") as arquivo:
     horarios_json = json.load(arquivo)
     for obj in horarios_json:

       data_formatada = datetime.datetime.strptime(obj["_Horario__data"], '%Y-%m-%d %H:%M:%S')
       
       h = Horario(obj["_Horario__id"], data_formatada, obj["_Horario__confirmado"], obj["_Horario__idCliente"], obj["_Horario__idServico"])
       cls.__horarios.append(h)