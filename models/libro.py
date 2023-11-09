from api_config import db


class Libro(db.Model):
    __tablename__ = "libro"
    isbn = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255))
    precio = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    descripcion = db.Column(db.String(1000))
    dimensiones = db.Column(db.String(255))
    paginas = db.Column(db.Integer)
    imagen = db.Column(db.LargeBinary)