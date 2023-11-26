from api_config import db

class PromocionDescuento(db.Model):
    __tablename__ = "promocion_descuento"
    id_promocion_descuento = db.Column(db.Integer, primary_key=True)
    nombre_promocion = db.Column(db.String(225))
    porcentaje = db.Column(db.Numeric(10, 2), nullable=False, check_constraint="porcentaje > 0 AND porcentaje < 100")
    fecha_inicio = db.Column(db.TIMESTAMP, nullable=False)
    fecha_fin = db.Column(db.TIMESTAMP, nullable=False)
    imagen = db.Column(db.String)
