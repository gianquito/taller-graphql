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
from models.autor import Autor as AutorModel
from models.ciudad import Ciudad as CiudadModel
from models.deseo_libro import DeseoLibro as DeseoLibroModel
from models.direccion import Direccion as DireccionModel
from models.editorial import Editorial as EditorialModel
from models.encuadernado import Encuadernado as EncuadernadoModel
from models.favorito_libro import FavoritoLibro as FavoritoLibroModel
from models.genero import Genero as GeneroModel
from models.libro_autor import LibroAutor as LibroAutorModel
from models.libro_editorial import LibroEditorial as LibroEditorialModel
from models.libro_encuadernado import LibroEncuadernado as LibroEncuadernadoModel
from models.libro_genero import LibroGenero as LibroGeneroModel
from models.libro_promocion import LibroPromocion as LibroPromocionModel
from models.linea_pedido import LineaPedido as LineaPedidoModel
from models.pedido import Pedido as PedidoModel
from models.promocion_descuento import PromocionDescuento as PromocionDescuentoModel
from models.resenia import Resenia as ReseniaModel
from models.tipo_envio import TipoEnvio as TipoEnvioModel

class Autor(SQLAlchemyObjectType):
    class Meta:
        model = AutorModel

class Ciudad(SQLAlchemyObjectType):
    class Meta:
        model = CiudadModel

class DeseoLibro(SQLAlchemyObjectType):
    class Meta:
        model = DeseoLibroModel

class Direccion(SQLAlchemyObjectType):
    class Meta:
        model = DireccionModel

class Editorial(SQLAlchemyObjectType):
    class Meta:
        model = EditorialModel

class Encuadernado(SQLAlchemyObjectType):
    class Meta:
        model = EncuadernadoModel

class FavoritoLibro(SQLAlchemyObjectType):
    class Meta:
        model = FavoritoLibroModel

class Genero(SQLAlchemyObjectType):
    class Meta:
        model = GeneroModel

class LibroAutor(SQLAlchemyObjectType):
    class Meta:
        model = LibroAutorModel

class LibroEditorial(SQLAlchemyObjectType):
    class Meta:
        model = LibroEditorialModel

class LibroEncuadernado(SQLAlchemyObjectType):
    class Meta:
        model = LibroEncuadernadoModel

class LibroGenero(SQLAlchemyObjectType):
    class Meta:
        model = LibroGeneroModel

class LibroPromocion(SQLAlchemyObjectType):
    class Meta:
        model = LibroPromocionModel

class LineaPedido(SQLAlchemyObjectType):
    class Meta:
        model = LineaPedidoModel

class Pedido(SQLAlchemyObjectType):
    class Meta:
        model = PedidoModel

class PromocionDescuento(SQLAlchemyObjectType):
    class Meta:
        model = PromocionDescuentoModel

class Resenia(SQLAlchemyObjectType):
    class Meta:
        model = ReseniaModel

class TipoEnvio(SQLAlchemyObjectType):
    class Meta:
        model = TipoEnvioModel

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