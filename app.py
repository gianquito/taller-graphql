from flask_graphql import GraphQLView
from models.schema import schema
from flask import request
import requests
import uuid
import base64


from api_config import (
    app,
    db
)

def userExists(idUsuario):
    query = {
        'query': '''
            query resolve_usuarios($idUsuario: String!) {
                usuarios(idUsuario: $idUsuario) {
                    idUsuario
                }
            }
        ''',
        'variables': {
            'idUsuario':  idUsuario# Replace with the user ID you want to check
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

def createUser(idUsuario, nombre, apellido, email, imagen):
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
                'idUsuario': idUsuario,
                'nombre': nombre,
                'apellido': apellido,
                'email': email,
                'imagen': imagen,
                'rol': '2',
            }
        }
    requests.post("http://localhost:5000/graphql", json=createUserQuery)

def createSesion(idUsuario):
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
            'idUsuario': idUsuario,
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
def validateGoogle():
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
    if(Gresponse.status_code != 200): return Gresponse.json(), 401
    #A partir de la respuesta de google solicitamos un JWT con informacion del usuario
    jwtRes = requests.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={Gresponse.json()['id_token']}")
    if(jwtRes.status_code != 200): return jwtRes.json(), 401
    
    #Crear usuario y sesion en db
    #Chequear que no exista
    userData = jwtRes.json()
    if(userExists(userData["sub"]) == False):
        createUser(userData["sub"], userData["given_name"], userData["family_name"], userData["email"], userData["picture"])
    return createSesion(userData["sub"])

@app.route('/validateMs', methods=['POST']) # @ decorador
def validateMicrosoft():
    #Verificamos si el cliente envio el codigo
    code = request.get_data(as_text=True)
    if(code is None): return '', 400

    #Enviamos el codigo a microsoft para validarlo
    MsResponse = requests.post(f"https://login.microsoftonline.com/common/oauth2/v2.0/token",
                            data={"code": code,
                                    "client_id": "10f88338-8bd0-45ac-a3c9-5f68ca25dc8b",
                                    "client_secret": "JQI8Q~ErbPidFd-8bJ7uAC8.eGJ9OlMkZxgBwc.r",
                                    "redirect_uri": "http://localhost:3000/ingresar",
                                    "grant_type": "authorization_code",
                                    "scope": "user.read"}
                                )
    if(MsResponse.status_code != 200): return MsResponse.json(), 401
    #A partir de la respuesta de microsoft solicitamos informacion del usuario
    userRes = requests.get(f"https://graph.microsoft.com/v1.0/me", headers={"Authorization": "Bearer "+MsResponse.json()["access_token"]})
    if(userRes.status_code != 200): return userRes.json(), 401
    
    #Solicitamos la imagen de perfil
    imageRes = requests.get(f"https://graph.microsoft.com/v1.0/me/photo/$value", headers={"Authorization": "Bearer "+MsResponse.json()["access_token"]})
    if(imageRes.status_code != 200): return imageRes.text(), 401

    base64_image = base64.b64encode(imageRes.content).decode('utf-8')
    
    #Crear usuario y sesion en db
    #Chequear que no exista
    userData = userRes.json()
    if(userExists(userData["id"]) == False):
        createUser(userData["id"], userData["givenName"], userData["surname"], userData["mail"], f"data:image/jpeg;base64,{base64_image}")
    return createSesion(userData["id"])

@app.route('/logout', methods=['POST']) # @ decorador
def userLogout():
    sesionId = request.get_data(as_text=True)
    return '', deleteSesion(sesionId).status_code

@app.route('/', methods=['GET', 'POST', 'PUT']) # @ decorador
def index():
    return 'Hola Mundo desde Flask'

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
