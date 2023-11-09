from api_config import db


class Carrito(db.Model):
    __tablename__ = "carrito"
    id_carrito = db.Column(db.Integer, primary_key=True) #La primary key deberia ser numero y hotel_fk