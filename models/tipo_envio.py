from api_config import db

class TipoEnvio(db.Model):
    __tablename__ = "tipo_envio"
    id_tipo_envio = db.Column(db.Serial, primary_key=True)
    descripcion = db.Column(db.String(225), nullable=False)
