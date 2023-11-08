from api_config import db

class Usuario(db.Model):
    __tablename__ = "usuario"
    id_usuario = db.Column(db.String, primary_key = True) 
    nombre = db.Column(db.String) 
    apellido = db.Column(db.String)
    email = db.Column(db.String)
    imagen = db.Column(db.String)
    fecha_creacion = db.Column(db.TIMESTAMP)
    rol = db.Column(db.Integer)
    id_carrito = db.Column(db.Integer, db.ForeignKey("carrito.id")) 
    carrito = db.relationship("Carrito")