from api_config import db

class Ejemplar(db.Model):
    __tablename__ = "ejemplar"
    isbn = db.Column(db.Integer, primary_key=True)
    precio = db.Column(db.Numeric(10, 2), nullable=False, check_constraint='precio > 0')
    stock = db.Column(db.Integer, nullable=False, check_constraint='stock >= 0')
    dimensiones = db.Column(db.String(225), nullable=False)
    paginas = db.Column(db.Integer, nullable=False, check_constraint='paginas > 0')
    
    id_libro = db.Column(db.Integer, db.ForeignKey('libro.id_libro'), nullable=False)
    id_editorial = db.Column(db.Integer, db.ForeignKey('editorial.id_editorial'), nullable=False)
    id_encuadernado = db.Column(db.Integer, db.ForeignKey('encuadernado.id_encuadernado'), nullable=False)
    
    libro = db.relationship('Libro', backref='ejemplares')
    editorial = db.relationship('Editorial', backref='ejemplares')
    encuadernado = db.relationship('Encuadernado', backref='ejemplares')
