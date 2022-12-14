from modulos.marca.dao import MarcaDao
class Modelo:
  VALUES=['descricao','marca_id']
  def __init__(self, descricao, marca_id, id=None):
    self.id = id
    self.descricao = descricao
    self.marca_id = marca_id
  
  def __str__(self):
    return f'Id: {self.id}, descricao: {self.descricao}, marca_id: {self.marca_id}'

  def get_data_dict(self):
    dao_marca = MarcaDao()
    marca = dao_marca.get_por_id(self.marca_id)
    return {
      'id': self.id,
      'descricao': self.descricao,
      'marca': marca.get_data_dict()
    }
    
