from database.connect import ConnectDataBase
from modulos.posto.posto import Posto


class PostoDao:
    _TABLE_NAME = 'POSTO'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(nome, cidade, cnpj)' \
                   ' values(%s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'

    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    def salvar(self, posto):
        if posto.id is None:
            cursor = self.database.cursor()
            cursor.execute(self._INSERT_INTO, (posto.nome, posto.cidade, posto.cnpj))
            id = cursor.fetchone()[0]
            self.database.commit()
            cursor.close()
            posto.id = id
            return posto
        else:
            raise Exception('Não é possível salvar')

    def get_all(self):
        postos = []
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_ALL)
        all_postos = cursor.fetchall()
        coluns_name = [desc[0] for desc in cursor.description]
        for posto_query in all_postos:
            data = dict(zip(coluns_name, posto_query))
            posto = Posto(**data)
            postos.append(posto)
        cursor.close()
        return postos

    def get_por_id(self, id):
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_BY_ID.format(self._TABLE_NAME, id))
        coluns_name = [desc[0] for desc in cursor.description]
        posto = cursor.fetchone()
        if not posto:
            return None
        data = dict(zip(coluns_name, posto))
        posto = Posto(**data)
        cursor.close()
        return posto

    #TODO: atualizar posto