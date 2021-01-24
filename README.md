# api_cep
API simples para consulta de CEP

A aplicação foi totalmente escrita em Python. O banco utilizado é o MySql.

Em breve, será implementado também para SQLite.

Para usar, é necessário restaurar o backup do banco com os endereços e realizar a instalação do FLASK e o conector do MySQL:

$ pip install flask flask-jsonpify flask-sqlalchemy flask-restful

$ pip install mysql-connector-python

Exemplo de uso, chamando a API via GET:

http://localhost:5000/endereco/69006800

Retorno:

{"CEP":"69006800","Cidade":"Manaus","Complemento":"Jorge Teixeira","Estado":"AM"}
