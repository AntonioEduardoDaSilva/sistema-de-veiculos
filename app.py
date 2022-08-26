from database.connect import ConnectDataBase
from modulos.motorista.dao import MotoristaDao
from modulos.posto.dao import PostoDao
from modulos.posto.posto import Posto
from flask import Flask
from modulos.posto.controller import app_empresa


app = Flask(__name__)
app.register_blueprint(app_empresa)


app.run()

#print(ConnectDataBase().get_instance())

#dao_motorista = MotoristaDao()
#motoristas = dao_motorista.get_all()
#print(motoristas)

dao_posto = PostoDao()
#postoNew = Posto(nome="posto1", cidade="caruaru", cnpj="1234567")
#postoOld = dao_posto.get_por_id(2)

#dao_posto.delete_posto(6)
#dao_posto.salvar(posto)

postos = dao_posto.get_all()
print(postos)
for posto in postos:
  print(posto.nome)
print("--------------------------------")
#print(dao_posto.get_por_id(1))

