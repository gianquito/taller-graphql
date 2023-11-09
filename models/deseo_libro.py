from api_config import db

class DeseoLibro(db.Model):
    __tablename__ = "deseo_libro"
    id_usuario = db.Column(db.Text, db.ForeignKey("usuario.id_usuario"), nullable=False, primary_key=True)
    id_libro = db.Column(db.Integer, db.ForeignKey("libro.isbn"), nullable=False, primary_key=True)
    usuario = db.relationship("Usuario", backref="libros_deseados")
    libro = db.relationship("Libro", backref="usuarios_deseados")
