# api_cep
API para consulta de CEP

A aplicação foi totalmente escrita em Python. O banco utilizado é o MySql.

Em breve, será implementado também para SQLite.

Para usar, é necessário restaurar o backup do banco com os endereços e realizar a instalação do FLASK e o conector do MySQL:

$ pip install flask flask-jsonpify flask-sqlalchemy flask-restful

$ pip install mysql-connector-python

Exemplo de uso, chamando a API via GET:

http://localhost:5000/endereco/69006800

Retorno:

{"Bairro":"Jorge Teixeira","CEP":"69006800","Cidade":"Manaus","Complemento":"Rua da Prata\n","Estado":"AM"}


Obs.: configurar conexão com o banco de dados através do arquivo 'api.config',
