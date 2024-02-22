from api_config import db

class FavoritoLibro(db.Model):
    __tablename__ = "favorito_libro"
    id_usuario = db.Column(db.Text, db.ForeignKey("usuario.id_usuario"), nullable=False, primary_key=True)
    id_libro = db.Column(db.Integer, db.ForeignKey("libro.id_libro"), nullable=False, primary_key=True)
    usuario = db.relationship("Usuario", backref="libros_favoritos")
    libro = db.relationship("Libro", backref="usuarios_favoritos")
