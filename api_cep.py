#Importação das libs
from flask import Flask, jsonify
from flask_restful import Resource, Api
import mysql.connector

#Criando aplicação
app = Flask(__name__)
api = Api(app)

#Abrindo arquivo de configurações
config = open('api.config', 'r')
configuracoes = {}
for lines in config:
    line = lines.split('=')
    #Guarda configurações num dicionário e remove o enter do final da linha
    configuracoes[line[0]] = line[1].split('\n')[0]

#Inicia conexão
db = mysql.connector.connect(
    host = configuracoes['host'],
    user = configuracoes['user'],
    password = configuracoes['password'],
    database = configuracoes['database']
)

#Criação do cursor
cursor = db.cursor()
sql = ''

class Endereco(Resource):
    def get(self, cep):
        sql = 'SELECT CEP, CIDADE, ESTADO, BAIRRO, COMPLEMENTO FROM endereco WHERE cep = ' + cep
        cursor.execute(sql)
        resultado = cursor.fetchall()
        retorno = {'CEP':resultado[0][0],
                   'Cidade':resultado[0][1],
                   'Estado':resultado[0][2],
                   'Bairro':resultado[0][3],
                   'Complemento':resultado[0][4]
        }
        return jsonify(retorno)


#Adicionando recursos
api.add_resource(Endereco, '/endereco/<cep>')

if __name__ == '__main__':
    app.run()