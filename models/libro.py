from api_config import db


class Libro(db.Model):
    __tablename__ = "libro"
    isbn = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(1000), nullable=False)
    dimensiones = db.Column(db.String(255), nullable=False)
    paginas = db.Column(db.Integer, nullable=False)
    imagen = db.Column(db.String)