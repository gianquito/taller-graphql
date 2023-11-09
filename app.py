from flask_graphql import GraphQLView
from models.schema import schema
from flask import request
import requests
import uuid


from api_config import (
    app,
    db
)

def userExists(userData):
    query = {
        'query': '''
            query resolve_usuarios($idUsuario: String!) {
                usuarios(idUsuario: $idUsuario) {
                    idUsuario
                }
            }
        ''',
        'variables': {
            'idUsuario': userData["sub"] # Replace with the user ID you want to check
        }
    }
    response = requests.post("http://localhost:5000/graphql", json=query)
    data = response.json()
    if 'data' in data:
        if(data['data']['usuarios']):
            return True
    return False

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True #Interfaz grafica
))

def createUser(userData):
    createUserQuery = {
            'query': '''
                mutation ($idUsuario: String!, $nombre: String!, $apellido: String!, $email: String!, $imagen: String!, $rol: Int!) {
                    createUsuario(idUsuario: $idUsuario, nombre: $nombre, apellido: $apellido, email: $email, imagen: $imagen, rol: $rol) {
                        usuario {
                            idUsuario
                        }
                    }
                }
            ''',
            'variables': {
                'idUsuario': userData["sub"],
                'nombre': userData["given_name"],
                'apellido': userData["family_name"],
                'email': userData["email"],
                'imagen': userData["picture"],
                'rol': 1,
            }
        }
    requests.post("http://localhost:5000/graphql", json=createUserQuery)

def createSesion(userData):
    sesionId = str(uuid.uuid4())

    createSesionQuery = {
        'query': '''
            mutation ($idSesion: String!, $idUsuario: String!) {
                createSesion(idSesion: $idSesion, idUsuario: $idUsuario) {
                    sesion {
                        idSesion
                    }
                }
            }
        ''',
        'variables': {
            'idSesion': sesionId,
            'idUsuario': userData["sub"],
        }
    }
    requests.post("http://localhost:5000/graphql", json=createSesionQuery)
    return sesionId

def deleteSesion(sesionId):
    deleteSesionQuery = {
        'query': '''
            mutation ($idSesion: String!) {
                deleteSesion(idSesion: $idSesion) {
                    sesion {
                        idSesion
                    }
                }
            }
        ''',
        'variables': {
            'idSesion': sesionId
        }
    }
    return requests.post("http://localhost:5000/graphql", json=deleteSesionQuery)

@app.route('/validate', methods=['POST']) # @ decorador
def validateLogin():
    #Verificamos si el cliente envio el codigo
    code = request.get_data(as_text=True)
    if(code is None): return '', 400

    #Enviamos el codigo a google para validarlo
    Gresponse = requests.post(f"https://oauth2.googleapis.com/token",
                            data={"code": code,
                                    "client_id": "922082614639-te6q4juqlgmiqomf96n0jq2p2go4bnqa.apps.googleusercontent.com",
                                    "client_secret": "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",
                                    "redirect_uri": "http://localhost:3000",
                                    "grant_type": "authorization_code"}
                                )
    if(Gresponse.status_code != 200): return '', 401
    #A partir de la respuesta de google solicitamos un JWT con informacion del usuario
    jwtRes = requests.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={Gresponse.json()['id_token']}")
    if(jwtRes.status_code != 200): return '', 401
    
    #Crear usuario y sesion en db
    #Chequear que no exista
    userData = jwtRes.json()
    if(userExists(userData) == False):
        createUser(userData)

    return createSesion(userData)

@app.route('/logout', methods=['POST']) # @ decorador
def userLogout():
    sesionId = request.get_data(as_text=True)
    return '', deleteSesion(sesionId).status_code

@app.route('/', methods=['GET', 'POST', 'PUT']) # @ decorador
def index():
    return 'Hola Mundo desde Flask'

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
