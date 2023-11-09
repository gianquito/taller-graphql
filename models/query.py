from graphene import (
    ObjectType,
    String,
    Boolean,
    # relay,
    Field,
    List,
    Int
)

# from .funko import Funko as FunkoModel
# from .objects import (
#     Funko,
#     User,
# )
from .objects import Libro, LineaCarrito, Usuario, Sesion
from .libro import Libro as LibroModel
from .linea_carrito import LineaCarrito as LineaCarritoModel
from .usuario import Usuario as UsuarioModel
from .sesion import Sesion as SesionModel



class Query(ObjectType):
    libros = List(lambda: Libro, id=Int(), precio=Int())
    libros_en_carrito = List(lambda: LineaCarrito, id_carrito=Int(), id_producto=Int())
    usuarios = List(lambda: Usuario, id_usuario=String())
    sesiones = List(lambda: Sesion, id_sesion=String())

    def resolve_libros(self, info, id=None, precio=None):
        print(info.context.cookies.get("user_id"))
        query = Libro.get_query(info=info)
        if id:
            query = query.filter(LibroModel.id==id)
        if precio:
            query = query.filter(LibroModel.precio==precio)
        return query.all()
    
    def resolve_libros_en_carrito(self, info, id_carrito=None, id_producto=None):
        query = LineaCarrito.get_query(info=info)
        if id_carrito:
            query = query.filter(LineaCarritoModel.id_carrito==id_carrito)
        if id_producto:
            query = query.filter(LineaCarritoModel.id_producto==id_producto)
        return query.join(LibroModel).all()
    
    def resolve_usuarios(self, info, id_usuario=None):
        query = Usuario.get_query(info=info)
        if id_usuario:
            query = query.filter(UsuarioModel.id_usuario==id_usuario)
        return query.all()
    
    def resolve_sesiones(self, info, id_sesion=None):
        query = Sesion.get_query(info=info)
        if id_sesion:
            query = query.filter(SesionModel.id_sesion==id_sesion)
        return query.all()