from flask import Flask, jsonify, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'trab_final'

@app.route('/del_usuario/<int:usuario_id>', methods=['DELETE'])
def del_usuario(usuario_id):

    try:
        # Conectar ao banco de dados
        with mysql.connector.connect(
            host=db_host, user=db_user, password=db_password, database=db_name
        ) as mydb:
            mycursor = mydb.cursor()

            sql = "delete from usuarios where id= %s"
            valores = (usuario_id,)

            mycursor.execute(sql,valores)
            mydb.commit()

            return jsonify({'usuario deletado com sucesso':  str()}), 200
        
    except mysql.connector.Error as error:
        return jsonify({'error': str(error)}), 500

@app.route('/sucesso')
def sucesso():
    return 'Dados inseridos com sucesso!'



if __name__ == '__main__':
    app.run(debug=True)
