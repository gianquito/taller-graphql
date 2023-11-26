from api_config import db

class LibroPromocion(db.Model):
    __tablename__ = "libro_promocion"
    id_libro = db.Column(db.Integer, db.ForeignKey("libro.isbn"), nullable=False, primary_key=True)
    id_promocion_descuento = db.Column(db.Integer, db.ForeignKey("promocion_descuento.id_promocion_descuento"), nullable=False, primary_key=True)
    libro = db.relationship("Libro", backref="promociones")
    promocion_descuento = db.relationship("PromocionDescuento", backref="libros")
