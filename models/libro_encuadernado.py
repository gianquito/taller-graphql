from api_config import db

class LibroEncuadernado(db.Model):
    __tablename__ = "libro_encuadernado"
    id_libro = db.Column(db.Integer, db.ForeignKey("libro.isbn"), nullable=False, primary_key=True)
    id_encuadernado = db.Column(db.Integer, db.ForeignKey("encuadernado.id_encuadernado"), nullable=False, primary_key=True)
    libro = db.relationship("Libro", backref="encuadernados")
    encuadernado = db.relationship("Encuadernado", backref="libros")
