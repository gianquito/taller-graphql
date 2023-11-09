from api_config import db

class LineaPedido(db.Model):
    __tablename__ = "linea_pedido"
    id_pedido = db.Column(db.Integer, db.ForeignKey("pedido.id_pedido"), nullable=False, primary_key=True)
    id_libro = db.Column(db.Integer, db.ForeignKey("libro.isbn"), nullable=False, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False, check_constraint="cantidad >= 0")
    pedido = db.relationship("Pedido", backref="lineas_pedido")
    libro = db.relationship("Libro", backref="lineas_pedido")
