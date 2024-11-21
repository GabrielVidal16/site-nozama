from flask import Flask, jsonify, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'trab_final'

@app.route('/get_usuario', methods=['GET'])
def get_nome_usuarios():
    nome = request.args.get('nome')

    if nome:
        # Construir a consulta SQL com o parâmetro de pesquisa
        sql = "SELECT * FROM usuarios WHERE nome LIKE %s"
        valores = ('%' + nome + '%',)
        try:
            with mysql.connector.connect(
                host=db_host, user=db_user, password=db_password, database=db_name
            ) as mydb:
                mycursor = mydb.cursor()
                mycursor.execute(sql, valores)
                resultados = mycursor.fetchall()

                # Formatar os resultados em um JSON
                usuarios = []
                for usuario in resultados:
                    usuarios.append({'id': usuario[0], 'nome': usuario[1], 'email': usuario[2], 'idade': usuario[3]})

                return jsonify({'usuarios': usuarios}), 200
        except mysql.connector.Error as error:
            return jsonify({'error': str(error)}), 500
    else:
        return jsonify({'mensagem': 'O parâmetro "nome" é obrigatório'}), 400
    
@app.route('/sucesso')
def sucesso():
    return 'Dados inseridos com sucesso!'



if __name__ == '__main__':
    app.run(debug=True)

