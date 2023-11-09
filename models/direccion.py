from api_config import db

class Direccion(db.Model):
    __tablename__ = "direccion"
    id_direccion = db.Column(db.Serial, primary_key=True)
    calle = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    id_usuario = db.Column(db.Text, db.ForeignKey("usuario.id_usuario"), nullable=False)
    cp_ciudad = db.Column(db.Integer, db.ForeignKey("ciudad.cp"), nullable=False)
    usuario = db.relationship("Usuario", backref="direcciones")
    ciudad = db.relationship("Ciudad", backref="direcciones")