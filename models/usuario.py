from api_config import db

class Usuario(db.Model):
    __tablename__ = "usuario"
    id_usuario = db.Column(db.String, primary_key = True) 
    nombre = db.Column(db.String(225), nullable=False) 
    apellido = db.Column(db.String(225), nullable=False)
    email = db.Column(db.String(225), nullable=False)
    imagen = db.Column(db.String, nullable=False)
    fecha_creacion = db.Column(db.TIMESTAMP, nullable=False)
    rol = db.Column(db.Integer, nullable=False)
    id_carrito = db.Column(db.Integer, db.ForeignKey("carrito.id_carrito"), nullable=False) 
    carrito = db.relationship("Carrito", backref="usuario")