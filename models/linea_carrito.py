from api_config import db

class LineaCarrito(db.Model):
    __tablename__ = "linea_carrito"
    id_carrito = db.Column(db.Integer, db.ForeignKey("carrito.id_carrito"), primary_key = True) 
    id_libro = db.Column(db.Integer, db.ForeignKey("libro.isbn"), primary_key = True) 
    cantidad = db.Column(db.Integer)
    carrito = db.relationship("Carrito")
    libro = db.relationship("Libro")