from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
)
# from graphene import (
#     # Int
# )
from models.ejemplar import Ejemplar as EjemplarModel
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
from models.libro_genero import LibroGenero as LibroGeneroModel
from models.ejemplar_promocion import EjemplarPromocion as EjemplarPromocionModel
from models.linea_pedido import LineaPedido as LineaPedidoModel
from models.pedido import Pedido as PedidoModel
from models.promocion_descuento import PromocionDescuento as PromocionDescuentoModel
from models.resenia import Resenia as ReseniaModel
from models.tipo_envio import TipoEnvio as TipoEnvioModel
from models.pregunta_frecuente import PreguntaFrecuente as PreguntaFrecuenteModel

class PreguntaFrecuente(SQLAlchemyObjectType):
    class Meta:
        model = PreguntaFrecuenteModel

class Ejemplar(SQLAlchemyObjectType):
    class Meta:
        model = EjemplarModel

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

class LibroGenero(SQLAlchemyObjectType):
    class Meta:
        model = LibroGeneroModel

class EjemplarPromocion(SQLAlchemyObjectType):
    class Meta:
        model = EjemplarPromocionModel

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