from api_config import db

class Resenia(db.Model):
    __tablename__ = "resenia"
    texto = db.Column(db.String(1000), nullable=False)
    valoracion = db.Column(db.Integer, nullable=False, check_constraint="valoracion >= 1 AND valoracion <= 5")
    id_usuario = db.Column(db.Text, db.ForeignKey("usuario.id_usuario"), nullable=False, primary_key=True)
    id_libro = db.Column(db.Integer, db.ForeignKey("libro.isbn"), nullable=False, primary_key=True)
    usuario = db.relationship("Usuario", backref="resenias")
    libro = db.relationship("Libro", backref="resenias")
