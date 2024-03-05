from api_config import db

class EjemplarPromocion(db.Model):
    __tablename__ = "ejemplar_promocion"
    id_ejemplar = db.Column(db.String(13), db.ForeignKey("ejemplar.isbn"), nullable=False, primary_key=True)
    id_promocion_descuento = db.Column(db.Integer, db.ForeignKey("promocion_descuento.id_promocion_descuento"), nullable=False, primary_key=True)
    ejemplar = db.relationship("Ejemplar", backref="promociones")
    promocion_descuento = db.relationship("PromocionDescuento", backref="ejemplares")
