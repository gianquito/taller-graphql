#from flask import abort
from werkzeug.exceptions import HTTPException
from graphene import (
    ObjectType,
    String,
    Boolean,
    # relay,
    Field,
    List,
    Int,
    Float
)

from graphql import GraphQLError

# from .funko import Funko as FunkoModel
# from .objects import (
#     Funko,
#     User,
# )
from .objects import (
                    Autor,
                    Ciudad,
                    DeseoLibro,
                    Direccion,
                    Editorial,
                    Encuadernado,
                    FavoritoLibro,
                    Genero,
                    LibroAutor,
                    LibroEditorial,
                    LibroEncuadernado,
                    LibroGenero,
                    LibroPromocion,
                    Libro,
                    LineaCarrito,
                    LineaPedido,
                    Pedido,
                    PromocionDescuento,
                    Resenia,
                    Sesion,
                    TipoEnvio,
                    Usuario,)

from .autor import Autor as AutorModel
from .ciudad import Ciudad as CiudadModel
from .deseo_libro import DeseoLibro as DeseoLibroModel
from .direccion import Direccion as DireccionModel
from .editorial import Editorial as EditorialModel
from .encuadernado import Encuadernado as EncuadernadoModel
from .favorito_libro import FavoritoLibro as FavoritoLibroModel
from .genero import Genero as GeneroModel
from .libro_autor import LibroAutor as LibroAutorModel
from .libro_editorial import LibroEditorial as LibroEditorialModel
from .libro_encuadernado import LibroEncuadernado as LibroEncuadernadoModel
from .libro_genero import LibroGenero as LibroGeneroModel
from .libro_promocion import LibroPromocion as LibroPromocionModel
from .libro import Libro as LibroModel
from .linea_carrito import LineaCarrito as LineaCarritoModel
from .linea_pedido import LineaPedido as LineaPedidoModel
from .pedido import Pedido as PedidoModel
from .promocion_descuento import PromocionDescuento as PromocionDescuentoModel
from .resenia import Resenia as ReseniaModel
from .sesion import Sesion as SesionModel
from .tipo_envio import TipoEnvio as TipoEnvioModel
from .usuario import Usuario as UsuarioModel



class Query(ObjectType):
    autores = List(lambda: Autor, id_autor=Int(), nombre_autor=String())
    ciudades = List(lambda: Ciudad, cp=Int(), nombre_ciudad=String())
    deseos_libro = List(lambda: DeseoLibro, id_usuario=String(), id_libro=Int())
    direcciones = List(lambda: Direccion, id_direccion=Int(), id_usuario=String())
    editoriales = List(lambda: Editorial, id_editorial=Int(), nombre_editorial=String())
    encuadernados = List(lambda: Encuadernado, id_encuadernado=Int(), tipo=String())
    favoritos_libro = List(lambda: FavoritoLibro, id_usuario=String(), id_libro=Int())
    generos = List(lambda: Genero, id_genero=Int(), nombre_genero=String())
    libros_autores = List(lambda: LibroAutor, id_libro=Int(), id_autor=Int())
    libros_editoriales = List(lambda: LibroEditorial, id_libro=Int(), id_editorial=Int())
    libros_encuadernados = List(lambda: LibroEncuadernado, id_libro=Int(), id_encuadernado=Int())
    libros_generos = List(lambda: LibroGenero, id_libro=Int(), id_genero=Int())
    libros_promociones = List(lambda: LibroPromocion, id_libro=Int(), id_promocion_descuento=Int())
    libros = List(lambda: Libro, isbn=Int(), precio=Float(), titulo=String())
    libros_en_carrito = List(lambda: LineaCarrito, id_carrito=Int(), id_libro=Int())
    lineas_pedidos = List(lambda: LineaPedido, id_pedido=Int(), id_libro=Int())
    pedidos = List(lambda: Pedido, id_pedido=Int(), id_envio=Int(), id_usuario=String(), fecha=String()) #Esta bien fecha = String?
    promociones_descuento = List(lambda: PromocionDescuento, id_promocion_descuento=Int(), nombre_promocion=String())
    resenias = List(lambda: Resenia, texto=String(), valoracion=Int(), id_usuario=String(), id_libro=Int())
    sesiones = List(lambda: Sesion, id_sesion=String())
    tipos_envio = List(lambda: TipoEnvio, id_tipo_envio=Int(), descripcion=String())
    usuarios = List(lambda: Usuario, id_usuario=String())
    
    def resolve_autores(self, info, id_autor=None, nombre_autor=None):
        query = Autor.get_query(info=info)
        if id_autor:
            query = query.filter(AutorModel.id_autor == id_autor)
        if nombre_autor:
            query = query.filter(AutorModel.nombre_autor.startswith(nombre_autor))
        return query.all()

    def resolve_ciudades(self, info, cp=None, nombre_ciudad=None):
        query = Ciudad.get_query(info=info)
        if cp:
            query = query.filter(CiudadModel.cp == cp)
        if nombre_ciudad:
            query = query.filter(CiudadModel.nombre_ciudad == nombre_ciudad)
        return query.all()

    def resolve_deseos_libro(self, info, id_usuario=None, id_libro=None):
        sesion_id = info.context.headers.get('sesionId')
        if not sesion_id:
            # Maneja el caso en que la cookie "sesionId" no este presente o sea invalida.
            raise GraphQLError('La cookie de sesión no está presente o es inválida.')
        sesion = SesionModel.query.filter(SesionModel.id_sesion == sesion_id).first()
        if sesion is None:
            # Si la sesion no existe genera un error indicando que la sesión no esta autenticada.
            raise GraphQLError('La sesión no existe o no está autenticada.')
        query = DeseoLibro.get_query(info=info)
        if id_usuario:
            query = query.filter(DeseoLibroModel.id_usuario == id_usuario)
        if id_libro:
            query = query.filter(DeseoLibroModel.id_libro == id_libro)
        return query.all()

    def resolve_direcciones(self, info, id_direccion=None, id_usuario=None):
        sesion_id = info.context.headers.get('sesionId')
        if not sesion_id:
            # Maneja el caso en que la cookie "sesionId" no este presente o sea invalida.
            raise GraphQLError('La cookie de sesión no está presente o es inválida.')
        sesion = SesionModel.query.filter(SesionModel.id_sesion == sesion_id).first()
        if sesion is None:
            # Si la sesion no existe genera un error indicando que la sesión no esta autenticada.
            raise GraphQLError('La sesión no existe o no está autenticada.')
        query = Direccion.get_query(info=info)
        if id_direccion:
            query = query.filter(DireccionModel.id_direccion == id_direccion)
        if id_usuario:
            query = query.filter(DireccionModel.id_usuario == id_usuario)
        return query.all()

    def resolve_editoriales(self, info, id_editorial=None, nombre_editorial=None):
        query = Editorial.get_query(info=info)
        if id_editorial:
            query = query.filter(EditorialModel.id_editorial == id_editorial)
        if nombre_editorial:
            query = query.filter(EditorialModel.nombre_editorial.startswith(nombre_editorial))
        return query.all()

    def resolve_encuadernados(self, info, id_encuadernado=None, tipo=None):
        query = Encuadernado.get_query(info=info)
        if id_encuadernado:
            query = query.filter(EncuadernadoModel.id_encuadernado == id_encuadernado)
        if tipo:
            query = query.filter(EncuadernadoModel.tipo.startswith(tipo))
        return query.all()

    def resolve_favoritos_libro(self, info, id_usuario=None, id_libro=None):
        sesion_id = info.context.headers.get('sesionId')
        if not sesion_id:
            # Maneja el caso en que la cookie "sesionId" no este presente o sea invalida.
            raise GraphQLError('La cookie de sesión no está presente o es inválida.')
        sesion = SesionModel.query.filter(SesionModel.id_sesion == sesion_id).first()
        if sesion is None:
            # Si la sesion no existe genera un error indicando que la sesión no esta autenticada.
            raise GraphQLError('La sesión no existe o no está autenticada.')
        query = FavoritoLibro.get_query(info=info)
        if id_usuario:
            query = query.filter(FavoritoLibroModel.id_usuario == id_usuario)
        if id_libro:
            query = query.filter(FavoritoLibroModel.id_libro == id_libro)
        return query.all()

    def resolve_generos(self, info, id_genero=None, nombre_genero=None):
        query = Genero.get_query(info=info)
        if id_genero:
            query = query.filter(GeneroModel.id_genero == id_genero)
        if nombre_genero:
            query = query.filter(GeneroModel.nombre_genero.startswith(nombre_genero))
        return query.all()

    def resolve_libros_autores(self, info, id_libro=None, id_autor=None):
        query = LibroAutor.get_query(info=info)
        if id_libro:
            query = query.filter(LibroAutorModel.id_libro == id_libro)
        if id_autor:
            query = query.filter(LibroAutorModel.id_autor == id_autor)
        return query.all()

    def resolve_libros_editoriales(self, info, id_libro=None, id_editorial=None):
        query = LibroEditorial.get_query(info=info)
        if id_libro:
            query = query.filter(LibroEditorialModel.id_libro == id_libro)
        if id_editorial:
            query = query.filter(LibroEditorialModel.id_editorial == id_editorial)
        return query.all()

    def resolve_libros_encuadernados(self, info, id_libro=None, id_encuadernado=None):
        query = LibroEncuadernado.get_query(info=info)
        if id_libro:
            query = query.filter(LibroEncuadernadoModel.id_libro == id_libro)
        if id_encuadernado:
            query = query.filter(LibroEncuadernadoModel.id_encuadernado == id_encuadernado)
        return query.all()

    def resolve_libros_generos(self, info, id_libro=None, id_genero=None):
        query = LibroGenero.get_query(info=info)
        if id_libro:
            query = query.filter(LibroGeneroModel.id_libro == id_libro)
        if id_genero:
            query = query.filter(LibroGeneroModel.id_genero == id_genero)
        return query.all()

    def resolve_libros_promociones(self, info, id_libro=None, id_promocion_descuento=None):
        query = LibroPromocion.get_query(info=info)
        if id_libro:
            query = query.filter(LibroPromocionModel.id_libro == id_libro)
        if id_promocion_descuento:
            query = query.filter(LibroPromocionModel.id_promocion_descuento == id_promocion_descuento)
        return query.all()
    
    def resolve_libros(self, info, isbn=None, precio=None, titulo=None):
        query = Libro.get_query(info=info)
        if isbn:
            query = query.filter(LibroModel.isbn==isbn)
        if precio:
            query = query.filter(LibroModel.precio==precio)
        if titulo:
            query = query.filter(LibroModel.titulo.startswith(titulo))
        return query.all()

    def resolve_libros_en_carrito(self, info, id_carrito=None, id_libro=None):
        sesion_id = info.context.headers.get('sesionId')
        if not sesion_id:
            # Maneja el caso en que la cookie "sesionId" no este presente o sea invalida.
            raise GraphQLError('La cookie de sesión no está presente o es inválida.')
        sesion = SesionModel.query.filter(SesionModel.id_sesion == sesion_id).first()
        if sesion is None:
            # Si la sesion no existe genera un error indicando que la sesión no esta autenticada.
            raise GraphQLError('La sesión no existe o no está autenticada.')
        query = LineaCarrito.get_query(info=info)
        if id_carrito:
            query = query.filter(LineaCarritoModel.id_carrito==id_carrito)
        if id_libro:
            query = query.filter(LineaCarritoModel.id_libro==id_libro)
        return query.join(LibroModel).all()

    def resolve_lineas_pedidos(self, info, id_pedido=None, id_libro=None):
        sesion_id = info.context.headers.get('sesionId')
        if not sesion_id:
            # Maneja el caso en que la cookie "sesionId" no este presente o sea invalida.
            raise GraphQLError('La cookie de sesión no está presente o es inválida.')
        sesion = SesionModel.query.filter(SesionModel.id_sesion == sesion_id).first()
        if sesion is None:
            # Si la sesion no existe genera un error indicando que la sesión no esta autenticada.
            raise GraphQLError('La sesión no existe o no está autenticada.')
        query = LineaPedido.get_query(info=info)
        if id_pedido:
            query = query.filter(LineaPedidoModel.id_pedido == id_pedido)
        if id_libro:
            query = query.filter(LineaPedidoModel.id_libro == id_libro)
        return query.all()

    def resolve_pedidos(self, info, id_pedido=None, id_envio=None, id_usuario=None, fecha=None):
        sesion_id = info.context.headers.get('sesionId')
        if not sesion_id:
            # Maneja el caso en que la cookie "sesionId" no este presente o sea invalida.
            raise GraphQLError('La cookie de sesión no está presente o es inválida.')
        sesion = SesionModel.query.filter(SesionModel.id_sesion == sesion_id).first()
        if sesion is None:
            # Si la sesion no existe genera un error indicando que la sesión no esta autenticada.
            raise GraphQLError('La sesión no existe o no está autenticada.')
        query = Pedido.get_query(info=info)
        if id_pedido:
            query = query.filter(PedidoModel.id_pedido == id_pedido)
        if id_envio:
            query = query.filter(PedidoModel.id_envio == id_envio)
        if id_usuario:
            query = query.filter(LineaPedidoModel.id_usuario == id_usuario)
        if fecha:
            query = query.filter(LineaPedidoModel.fecha == fecha)
        return query.all()

    def resolve_promociones_descuento(self, info, id_promocion_descuento=None, nombre_promocion=None):
        query = PromocionDescuento.get_query(info=info)
        if id_promocion_descuento:
            query = query.filter(PromocionDescuentoModel.id_promocion_descuento == id_promocion_descuento)
        if nombre_promocion:
            query = query.filter(PromocionDescuentoModel.nombre_promocion == nombre_promocion)
        return query.all()

    def resolve_resenias(self, info, texto=None, valoracion=None, id_usuario=None, id_libro=None):
        query = Resenia.get_query(info=info)
        if texto:
            query = query.filter(ReseniaModel.texto == texto)
        if valoracion:
            query = query.filter(ReseniaModel.valoracion == valoracion)
        if id_usuario:
            query = query.filter(ReseniaModel.id_usuario == id_usuario)
        if id_libro:
            query = query.filter(ReseniaModel.id_libro == id_libro)
        return query.all()
    
    def resolve_sesiones(self, info, id_sesion=None):
        query = Sesion.get_query(info=info)
        if id_sesion:
            query = query.filter(SesionModel.id_sesion==id_sesion)
        return query.all()

    def resolve_tipos_envio(self, info, id_tipo_envio=None, descripcion=None):
        sesion_id = info.context.headers.get('sesionId')
        if not sesion_id:
            # Maneja el caso en que la cookie "sesionId" no este presente o sea invalida.
            raise GraphQLError('La cookie de sesión no está presente o es inválida.')
        sesion = SesionModel.query.filter(SesionModel.id_sesion == sesion_id).first()
        if sesion is None:
            # Si la sesion no existe genera un error indicando que la sesión no esta autenticada.
            raise GraphQLError('La sesión no existe o no está autenticada.')
        query = TipoEnvio.get_query(info=info)
        if id_tipo_envio:
            query = query.filter(TipoEnvioModel.id_tipo_envio == id_tipo_envio)
        if descripcion:
            query = query.filter(TipoEnvioModel.descripcion == descripcion)
        return query.all()
    
    def resolve_usuarios(self, info, id_usuario=None):
        # sesion_id = info.context.cookies.get("sesionId")
        # if not sesion_id:
        #     # Maneja el caso en que la cookie "sesionId" no este presente o sea invalida.
        #     raise HTTPException(status_code=401, detail="La cookie de sesión no está presente o es inválida.")
        # sesion = SesionModel.query.filter(SesionModel.id_sesion == sesion_id).first()
        # if sesion is None:
        #     # Si la sesion no existe genera un error indicando que la sesión no esta autenticada.
        #     raise HTTPException(status_code=401, detail="La sesión no existe o no está autenticada.")
        query = Usuario.get_query(info=info)
        if id_usuario:
            query = query.filter(UsuarioModel.id_usuario==id_usuario)
        return query.all()
