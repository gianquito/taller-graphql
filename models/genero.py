from api_config import db

class Genero(db.Model):
    __tablename__ = "genero"
    id_genero = db.Column(db.Serial, primary_key=True)
    nombre_genero = db.Column(db.String(255), nullable=False)
