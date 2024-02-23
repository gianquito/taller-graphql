from api_config import db

class LibroAutor(db.Model):
    __tablename__ = "libro_autor"
    id_libro = db.Column(db.Integer, db.ForeignKey("libro.id_libro"), nullable=False, primary_key=True)
    id_autor = db.Column(db.Integer, db.ForeignKey("autor.id_autor"), nullable=False, primary_key=True)
    libro = db.relationship("Libro", backref="autores")
    autor = db.relationship("Autor", backref="libros")
