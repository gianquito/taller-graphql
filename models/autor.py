from api_config import db

class Autor(db.Model):
    __tablename__ = "autor"
    id_autor = db.Column(db.Serial, primary_key=True)
    nombre_autor = db.Column(db.String(255), nullable=False)
