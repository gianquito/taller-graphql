from api_config import db

class LineaCarrito(db.Model):
    __tablename__ = "lineacarrito"
    id_carrito = db.Column(db.Integer, db.ForeignKey("carrito.id_carrito")) 
    id_libro = db.Column(db.Integer, db.ForeignKey("libro.isbn"), primary_key = True) 
    cantidad = db.Column(db.Integer)
    carrito = db.relationship("Carrito")
    libro = db.relationship("Libro")