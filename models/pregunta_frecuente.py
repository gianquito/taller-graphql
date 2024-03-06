from api_config import db

class PreguntaFrecuente(db.Model):
    __tablename__ = "pregunta_frecuente"
    id = db.Column(db.Integer, primary_key=True)
    pregunta = db.Column(db.String(255), nullable=False)
    respuesta = db.Column(db.String(500), nullable=False)
