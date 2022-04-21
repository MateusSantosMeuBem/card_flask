import json
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> None:
    return render_template('index.html')

@app.route('/usuarios/')
def not_users() -> None:
    info = {
        'message': 'Tente colocar o nome de um usuário como parâmetro na url. Por exemplo "/mateussantosmeubem"',
        'documentation_url': ''
    }
    return render_template('error.html', nome_usuario = info)

@app.route('/usuarios/<user_name>')
def users(user_name: dict) -> None:
    info: str = requests.get(f'https://api.github.com/users/{user_name}').text
    info: dict = json.loads(info)
    if 'message' in info.keys():
        return render_template('error.html', nome_usuario = info)
    else:
        return render_template('usuarios.html', nome_usuario = info)



if __name__ == '__main__':
    app.run(
        debug = True,
        host = '0.0.0.0'
    )