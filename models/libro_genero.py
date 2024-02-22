from api_config import db

class LibroGenero(db.Model):
    __tablename__ = "libro_genero"
    id_libro = db.Column(db.Integer, db.ForeignKey("libro.id_libro"), nullable=False, primary_key=True)
    id_genero = db.Column(db.Integer, db.ForeignKey("genero.id_genero"), nullable=False, primary_key=True)
    libro = db.relationship("Libro", backref="generos")
    genero = db.relationship("Genero", backref="libros")