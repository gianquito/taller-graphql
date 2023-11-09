from api_config import db

class LibroEditorial(db.Model):
    __tablename__ = "libro_editorial"
    id_libro = db.Column(db.Integer, db.ForeignKey("libro.isbn"), nullable=False, primary_key=True)
    id_editorial = db.Column(db.Integer, db.ForeignKey("editorial.id_editorial"), nullable=False, primary_key=True)
    libro = db.relationship("Libro", backref="editoriales")
    editorial = db.relationship("Editorial", backref="libros")
