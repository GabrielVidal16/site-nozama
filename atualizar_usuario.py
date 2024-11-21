from flask import Flask, jsonify, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'trab_final'

@app.route('/change_usuario/<int:usuario_id>', methods=['PUT'])
def atualizar_usuario(usuario_id):
    # Obter os dados do formulário
    dados = request.json  # Assumindo que os dados são enviados em formato JSON

    # Validar os dados
    # ... (implementar a validação aqui)

    # Construir a consulta SQL
    sql = "UPDATE usuarios SET nome=%s, email=%s, data_nascimento=%s WHERE id=%s"
    valores = (dados['nome'], dados['email'], dados['data_nascimento'], usuario_id)

    # Conectar ao banco de dados e executar a consulta
    try:
        with mysql.connector.connect(
            host=db_host, user=db_user, password=db_password, database=db_name
        ) as mydb:
            mycursor = mydb.cursor()
            mycursor.execute(sql, valores)
            mydb.commit()
            return jsonify({'mensagem': 'Usuário atualizado com sucesso'}), 200
    except mysql.connector.Error as error:
        return jsonify({'error': str(error)}), 500
    
@app.route('/sucesso')
def sucesso():
    return 'Dados inseridos com sucesso!'



if __name__ == '__main__':
    app.run(debug=True)







