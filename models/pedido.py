from api_config import db

class Pedido(db.Model):
    __tablename__ = "pedido"
    id_pedido = db.Column(db.Integer, primary_key=True)
    id_envio = db.Column(db.Integer, db.ForeignKey("tipo_envio.id_tipo_envio"), nullable=False)
    fecha = db.Column(db.TIMESTAMP, nullable=False)
    costo_envio = db.Column(db.Numeric(10, 2), nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)
    id_usuario = db.Column(db.Text, db.ForeignKey("usuario.id_usuario"), nullable=False)
    envio = db.relationship("TipoEnvio", backref="pedidos")
    usuario = db.relationship("Usuario", backref="pedidos")