from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
)
# from graphene import (
#     # Int
# )
# from models.funko import Funko as FunkoModel
# from models.user import User as UserModel
from models.libro import Libro as LibroModel
from models.carrito import Carrito as CarritoModel
from models.linea_carrito import LineaCarrito as LineaCarritoModel
from models.usuario import Usuario as UsuarioModel
from models.sesion import Sesion as SesionModel



class Libro(SQLAlchemyObjectType):
    class Meta:
        model = LibroModel

class Carrito(SQLAlchemyObjectType):
    class Meta:
        model = CarritoModel

class LineaCarrito(SQLAlchemyObjectType):
    class Meta:
        model = LineaCarritoModel

class Usuario(SQLAlchemyObjectType):
    class Meta:
        model = UsuarioModel

class Sesion(SQLAlchemyObjectType):
    class Meta:
        model = SesionModel