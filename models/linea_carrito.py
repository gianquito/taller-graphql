from api_config import db

class LineaCarrito(db.Model):
    __tablename__ = "linea_carrito"
    id_carrito = db.Column(db.Integer, db.ForeignKey("carrito.id_carrito"), primary_key = True) 
    id_ejemplar = db.Column(db.String(13), db.ForeignKey("ejemplar.isbn"), primary_key = True) 
    cantidad = db.Column(db.Integer)
    carrito = db.relationship("Carrito")
    ejemplar = db.relationship("Ejemplar")