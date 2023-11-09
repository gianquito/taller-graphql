from api_config import db

class Encuadernado(db.Model):
    __tablename__ = "encuadernado"
    id_encuadernado = db.Column(db.Serial, primary_key=True)
    tipo = db.Column(db.String(255), nullable=False)