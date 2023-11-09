from api_config import db

class Sesion(db.Model):
    __tablename__ = "sesion"
    id_sesion = db.Column(db.String, primary_key = True) 
    id_usuario = db.Column(db.String, db.ForeignKey("usuario.id_usuario")) 
    usuario = db.relationship("Usuario")