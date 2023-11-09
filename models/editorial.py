from api_config import db


class Editorial(db.Model):
    __tablename__ = "editorial"
    id_editorial = db.Column(db.Serial, primary_key=True)
    nombre_editorial = db.Column(db.String(255), nullable=False)