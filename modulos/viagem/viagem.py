class Viagem:
  def __init__(self, veiculo_id, motorista_id, destino, id=None):
    self.id = id
    self.veiculo_id = veiculo_id
    self.motorista_id = motorista_id
    self.destino = destino
  
  def __str__(self) :
    return f'Veiculo id: {self.veiculo_id}, Motorista id: {self.motorista_id}, Destino: {self.destino}'