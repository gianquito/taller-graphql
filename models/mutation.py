from graphene import(
    ObjectType,
    Mutation,
    String,
    Field,
    Int,
    Boolean
)

from api_config import (
    db
)

from .objects import (
    Libro,
    Carrito,
    LineaCarrito,
    Sesion,
    Usuario,
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
    LineaPedido,
    Pedido,
    PromocionDescuento,
    Resenia,
    TipoEnvio
)

from .libro import Libro as LibroModel
from .carrito import Carrito as CarritoModel
from .linea_carrito import LineaCarrito as LineaCarritoModel
from .usuario import Usuario as UsuarioModel
from .sesion import Sesion as SesionModel
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
from .linea_pedido import LineaPedido as LineaPedidoModel
from .pedido import Pedido as PedidoModel
from .promocion_descuento import PromocionDescuento as PromocionDescuentoModel
from .resenia import Resenia as ReseniaModel
from .tipo_envio import TipoEnvio as TipoEnvioModel

class createUsuario(Mutation):
    class Arguments:
        id_usuario = String(required=True)
        nombre = String(required=True)
        apellido = String(required=True)
        email = String(required=True)
        imagen = String(required=True)
        rol = Int(required=True)
    
    usuario = Field(lambda: Usuario)

    def mutate(self, info, id_usuario, nombre, apellido, email, imagen, rol):
        usuario = UsuarioModel(id_usuario=id_usuario, nombre=nombre, apellido=apellido, email=email, imagen=imagen, rol=rol)

        db.session.add(usuario)
        db.session.commit()
        
        return createUsuario(usuario=usuario)

class createSesion(Mutation):
    class Arguments:
        id_sesion = String(required=True)
        id_usuario = String(required=True)

    
    sesion = Field(lambda: Sesion)

    def mutate(self, info, id_sesion, id_usuario):
        sesion = SesionModel(id_sesion=id_sesion, id_usuario=id_usuario)

        db.session.add(sesion)
        db.session.commit()
        
        return createSesion(sesion=sesion)

class deleteSesion(Mutation):
    class Arguments:
        id_sesion = String(required=True)
        # !!!!!!!!!!!!!!! agregar id_carrito y comparar

    sesion = Field(lambda: Sesion)

    def mutate(self, info, id_sesion):
        sesion = SesionModel.query.get(id_sesion)
        
        if sesion:
            db.session.delete(sesion)
            db.session.commit()

        return deleteSesion(sesion=sesion)

class createLineaCarrito(Mutation):
    class Arguments:
        id_carrito = Int(required=True)
        id_producto = Int(required=True)
        cantidad_producto = Int(required=True)
    
    linea_carrito = Field(lambda: LineaCarrito)
    def mutate(self, info, id_carrito, id_producto, cantidad_producto):
        linea_carrito = LineaCarritoModel(id_carrito=id_carrito, id_producto=id_producto, cantidad_producto=cantidad_producto)

        db.session.add(linea_carrito)
        db.session.commit()
        
        return createLineaCarrito(linea_carrito=linea_carrito)

class updateLineaCarrito(Mutation):
    class Arguments:
        id_carrito = Int(required=True)
        id_producto = Int(required=True)
        cantidad_producto = Int()
    
    linea_carrito = Field(lambda: LineaCarrito)

    def mutate(self, info, id_carrito, id_producto, cantidad_producto=None):
        linea_carrito = LineaCarritoModel.query.get(id_producto)
        if linea_carrito:
            if(cantidad_producto):
                linea_carrito.cantidad_producto = cantidad_producto

            db.session.add(linea_carrito)
            db.session.commit()

        return updateLineaCarrito(linea_carrito=linea_carrito)

class deleteLineaCarrito(Mutation):
    class Arguments:
        id_producto = Int(required=True)
        # !!!!!!!!!!!!!!! agregar id_carrito y comparar

    linea_carrito = Field(lambda: LineaCarrito)

    def mutate(self, info, id_producto):
        linea_carrito = LineaCarritoModel.query.get(id_producto)
        
        if linea_carrito:
            db.session.delete(linea_carrito)
            db.session.commit()

        return deleteLineaCarrito(linea_carrito=linea_carrito)

class createAutor(Mutation):
    class Arguments:
        id_autor = Int(required=True)
        nombre_autor = String(required=True)
    
    autor = Field(lambda: Autor)

    def mutate(self, info, id_autor, nombre_autor):
        autor = AutorModel(id_autor=id_autor, nombre_autor=nombre_autor)

        db.session.add(autor)
        db.session.commit()
        
        return createAutor(autor=autor)

class createCiudad(Mutation):
    class Arguments:
        cp = Int(required=True)
        nombre_ciudad = String(required=True)

    ciudad = Field(lambda: Ciudad)

    def mutate(self, info, cp, nombre_ciudad):
        ciudad = CiudadModel(cp=cp, nombre_ciudad=nombre_ciudad)

        db.session.add(ciudad)
        db.session.commit()

        return createCiudad(ciudad=ciudad)

class createDeseoLibro(Mutation):
    class Arguments:
        id_usuario = String(required=True)
        id_libro = Int(required=True)

    deseo_libro = Field(lambda: DeseoLibro)

    def mutate(self, info, id_usuario, id_libro):
        deseo_libro = DeseoLibroModel(id_usuario=id_usuario, id_libro=id_libro)

        db.session.add(deseo_libro)
        db.session.commit()

        return createDeseoLibro(deseo_libro=deseo_libro)

class createEditorial(Mutation):
    class Arguments:
        id_editorial = Int(required=True)
        nombre_editorial = String(required=True)
    
    editorial = Field(lambda: Editorial)

    def mutate(self, info, id_editorial, nombre_editorial):
        editorial = EditorialModel(id_editorial=id_editorial, nombre_editorial=nombre_editorial)

        db.session.add(editorial)
        db.session.commit()
        
        return createEditorial(editorial=editorial)

class createEncuadernado(Mutation):
    class Arguments:
        id_encuadernado = Int(required=True)
        tipo = String(required=True)
    
    encuadernado = Field(lambda: Encuadernado)

    def mutate(self, info, id_encuadernado, tipo):
        encuadernado = EncuadernadoModel(id_encuadernado=id_encuadernado, tipo=tipo)

        db.session.add(encuadernado)
        db.session.commit()
        
        return createEncuadernado(encuadernado=encuadernado)

class createGenero(Mutation):
    class Arguments:
        id_genero = Int(required=True)
        nombre_genero = String(required=True)
    
    genero = Field(lambda: Genero)

    def mutate(self, info, id_genero, nombre_genero):
        genero = GeneroModel(id_genero=id_genero, nombre_genero=nombre_genero)

        db.session.add(genero)
        db.session.commit()
        
        return createGenero(genero=genero)

class createLibroEditorial(Mutation):
    class Arguments:
        id_libro = Int(required=True)
        id_editorial = Int(required=True)
    
    libro_editorial = Field(lambda: LibroEditorial)

    def mutate(self, info, id_libro, id_editorial):
        libro_editorial = LibroEditorialModel(id_libro=id_libro, id_editorial=id_editorial)

        db.session.add(libro_editorial)
        db.session.commit()
        
        return createLibroEditorial(libro_editorial=libro_editorial)

class createLibroGenero(Mutation):
    class Arguments:
        id_libro = Int(required=True)
        id_genero = Int(required=True)
    
    libro_genero = Field(lambda: LibroGenero)

    def mutate(self, info, id_libro, id_genero):
        libro_genero = LibroGeneroModel(id_libro=id_libro, id_genero=id_genero)

        db.session.add(libro_genero)
        db.session.commit()
        
        return createLibroGenero(libro_genero=libro_genero)

class createLibroPromocion(Mutation):
    class Arguments:
        id_libro = Int(required=True)
        id_promocion_descuento = Int(required=True)
    
    libro_promocion = Field(lambda: LibroPromocion)

    def mutate(self, info, id_libro, id_promocion_descuento):
        libro_promocion = LibroPromocionModel(id_libro=id_libro, id_promocion_descuento=id_promocion_descuento)

        db.session.add(libro_promocion)
        db.session.commit()
        
        return createLibroPromocion(libro_promocion=libro_promocion)

class createResenia(Mutation):
    class Arguments:
        texto = String(required=True)
        valoracion = Int(required=True)
        id_usuario = String(required=True)
        id_libro = Int(required=True)
    
    resenia = Field(lambda: Resenia)

    def mutate(self, info, texto, valoracion, id_usuario, id_libro):
        resenia = ReseniaModel(texto=texto, valoracion=valoracion, id_usuario=id_usuario, id_libro=id_libro)

        db.session.add(resenia)
        db.session.commit()
        
        return createResenia(resenia=resenia)

class createTipoEnvio(Mutation):
    class Arguments:
        id_tipo_envio = Int(required=True)
        descripcion = String(required=True)
    
    tipo_envio = Field(lambda: TipoEnvio)

    def mutate(self, info, id_tipo_envio, descripcion):
        tipo_envio = TipoEnvioModel(id_tipo_envio=id_tipo_envio, descripcion=descripcion)

        db.session.add(tipo_envio)
        db.session.commit()
        
        return createTipoEnvio(tipo_envio=tipo_envio)

class Mutation(ObjectType):
    create_linea_carrito = createLineaCarrito.Field()
    update_linea_carrito = updateLineaCarrito.Field()
    delete_linea_carrito = deleteLineaCarrito.Field()
    create_usuario = createUsuario.Field()
    create_sesion = createSesion.Field()
    delete_sesion = deleteSesion.Field()
    create_autor = createAutor.Field()
    create_ciudad = createCiudad.Field()
    create_deseo_libro = createDeseoLibro.Field()
    create_editorial = createEditorial.Field()
    create_encuadernado = createEncuadernado.Field()
    create_genero = createGenero.Field()
    create_libro_editorial = createLibroEditorial.Field()
    create_libro_genero = createLibroGenero.Field()
    create_libro_promocion = createLibroPromocion.Field()
    create_resenia = createResenia.Field()
    create_tipo_envio = createTipoEnvio.Field()