from api_config import db

class Ciudad(db.Model):
    __tablename__ = "ciudad"
    cp = db.Column(db.Integer, primary_key=True)
    nombre_ciudad = db.Column(db.String(255), nullable=False)