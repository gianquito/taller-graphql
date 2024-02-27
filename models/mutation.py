from graphene import(
    ObjectType,
    Mutation,
    String,
    Field,
    Int,
    Boolean,
    Float
)

from api_config import (
    db
)

from .objects import (
    Autor,
    Carrito,
    Ciudad,
    DeseoLibro,
    Direccion,
    Editorial,
    Encuadernado,
    FavoritoLibro,
    Genero,
    LibroAutor,
    LibroGenero,
    EjemplarPromocion,
    Libro,
    LineaCarrito,
    LineaPedido,
    Pedido,
    PromocionDescuento,
    Resenia,
    Sesion,
    TipoEnvio,
    Usuario,
    Ejemplar
)

from datetime import datetime

from .autor import Autor as AutorModel
from .carrito import Carrito as CarritoModel
from .ciudad import Ciudad as CiudadModel
from .deseo_libro import DeseoLibro as DeseoLibroModel
from .direccion import Direccion as DireccionModel
from .editorial import Editorial as EditorialModel
from .encuadernado import Encuadernado as EncuadernadoModel
from .favorito_libro import FavoritoLibro as FavoritoLibroModel
from .genero import Genero as GeneroModel
from .libro_autor import LibroAutor as LibroAutorModel
from .libro_genero import LibroGenero as LibroGeneroModel
from .ejemplar_promocion import EjemplarPromocion as EjemplarPromocionModel
from .libro import Libro as LibroModel
from .linea_carrito import LineaCarrito as LineaCarritoModel
from .linea_pedido import LineaPedido as LineaPedidoModel
from .pedido import Pedido as PedidoModel
from .promocion_descuento import PromocionDescuento as PromocionDescuentoModel
from .resenia import Resenia as ReseniaModel
from .sesion import Sesion as SesionModel
from .tipo_envio import TipoEnvio as TipoEnvioModel
from .usuario import Usuario as UsuarioModel
from .ejemplar import Ejemplar as EjemplarModel

class createAutor(Mutation):
    class Arguments:
        id_autor = Int()
        nombre_autor = String(required=True)
    
    autor = Field(lambda: Autor)

    def mutate(self, info, nombre_autor):
        autor = AutorModel(nombre_autor=nombre_autor)

        db.session.add(autor)
        db.session.commit()
        
        return createAutor(autor=autor)

class updateAutor(Mutation):
    class Arguments:
        id_autor = Int(required=True)
        nombre_autor = String()

    autor = Field(lambda: Autor)

    def mutate(self, info, id_autor, nombre_autor=None):
        autor = AutorModel.query.get(id_autor)
        if autor:
            if nombre_autor:
                autor.nombre_autor = nombre_autor
            db.session.add(autor)
            db.session.commit()

        return updateAutor(autor=autor)


class deleteAutor(Mutation):
    class Arguments:
        id_autor = Int(required=True)

    autor = Field(lambda: Autor)

    def mutate(self, info, id_autor):
        autor = AutorModel.query.get(id_autor)
        if autor:
            db.session.delete(autor)
            db.session.commit()

        return deleteAutor(autor=autor)

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

class updateCiudad(Mutation):
    class Arguments:
        cp = Int(required=True)
        nombre_ciudad = String()

    ciudad = Field(lambda: Ciudad)

    def mutate(self, info, cp, nombre_ciudad=None):
        ciudad = CiudadModel.query.get(cp)
        if ciudad:
            if nombre_ciudad:
                ciudad.nombre_ciudad = nombre_ciudad
            db.session.add(ciudad)
            db.session.commit()

        return updateCiudad(ciudad=ciudad)

class deleteCiudad(Mutation):
    class Arguments:
        cp = Int(required=True)

    ciudad = Field(lambda: Ciudad)

    def mutate(self, info, cp):
        ciudad = CiudadModel.query.get(cp)
        if ciudad:
            db.session.delete(ciudad)
            db.session.commit()

        return deleteCiudad(ciudad=ciudad)

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

class deleteDeseoLibro(Mutation):
    class Arguments:
        id_usuario = String(required=True)
        id_libro = Int(required=True)

    deseo_libro = Field(lambda: DeseoLibro)

    def mutate(self, info, id_usuario, id_libro):
        deseo_libro = DeseoLibroModel.query.filter_by(id_usuario=id_usuario, id_libro=id_libro).first()
        if deseo_libro:
            db.session.delete(deseo_libro)
            db.session.commit()

        return deleteDeseoLibro(deseo_libro=deseo_libro)

class createDireccion(Mutation):
    class Arguments:
        calle = String(required=True)
        numero = Int(required=True)
        id_usuario = String(required=True)
        cp_ciudad = Int(required=True)

    direccion = Field(lambda: Direccion)

    def mutate(self, info, calle, numero, id_usuario, cp_ciudad):
        direccion = DireccionModel(
            
            calle=calle,
            numero=numero,
            id_usuario=id_usuario,
            cp_ciudad=cp_ciudad
        )

        db.session.add(direccion)
        db.session.commit()

        return createDireccion(direccion=direccion)

class updateDireccion(Mutation):
    class Arguments:
        id_direccion = Int(required=True)
        calle = String()
        numero = Int()
        id_usuario = String()
        cp_ciudad = Int()

    direccion = Field(lambda: Direccion)

    def mutate(self, info, id_direccion, calle=None, numero=None, id_usuario=None, cp_ciudad=None):
        direccion = DireccionModel.query.get(id_direccion)
        if direccion:
            if calle:
                direccion.calle = calle
            if numero is not None:
                direccion.numero = numero
            if id_usuario:
                direccion.id_usuario = id_usuario
            if cp_ciudad is not None:
                direccion.cp_ciudad = cp_ciudad

            db.session.add(direccion)
            db.session.commit()

        return updateDireccion(direccion=direccion)

class deleteDireccion(Mutation):
    class Arguments:
        id_direccion = Int(required=True)

    direccion = Field(lambda: Direccion)

    def mutate(self, info, id_direccion):
        direccion = DireccionModel.query.get(id_direccion)
        if direccion:
            db.session.delete(direccion)
            db.session.commit()

        return deleteDireccion(direccion=direccion)

class createEditorial(Mutation):
    class Arguments:
        nombre_editorial = String(required=True)
    
    editorial = Field(lambda: Editorial)

    def mutate(self, info, nombre_editorial):
        editorial = EditorialModel(nombre_editorial=nombre_editorial)

        db.session.add(editorial)
        db.session.commit()
        
        return createEditorial(editorial=editorial)

class updateEditorial(Mutation):
    class Arguments:
        id_editorial = Int(required=True)
        nombre_editorial = String()

    editorial = Field(lambda: Editorial)

    def mutate(self, info, id_editorial, nombre_editorial=None):
        editorial = EditorialModel.query.get(id_editorial)
        if editorial:
            if nombre_editorial:
                editorial.nombre_editorial = nombre_editorial
            db.session.add(editorial)
            db.session.commit()

        return updateEditorial(editorial=editorial)

class deleteEditorial(Mutation):
    class Arguments:
        id_editorial = Int(required=True)

    editorial = Field(lambda: Editorial)

    def mutate(self, info, id_editorial):
        editorial = EditorialModel.query.get(id_editorial)
        if editorial:
            db.session.delete(editorial)
            db.session.commit()

        return deleteEditorial(editorial=editorial)

class createEncuadernado(Mutation):
    class Arguments:
        tipo = String(required=True)
    
    encuadernado = Field(lambda: Encuadernado)

    def mutate(self, info, tipo):
        encuadernado = EncuadernadoModel(tipo=tipo)

        db.session.add(encuadernado)
        db.session.commit()
        
        return createEncuadernado(encuadernado=encuadernado)

class updateEncuadernado(Mutation):
    class Arguments:
        id_encuadernado = Int(required=True)
        tipo = String()

    encuadernado = Field(lambda: Encuadernado)

    def mutate(self, info, id_encuadernado, tipo=None):
        encuadernado = EncuadernadoModel.query.get(id_encuadernado)
        if encuadernado:
            if tipo:
                encuadernado.tipo = tipo
            db.session.add(encuadernado)
            db.session.commit()

        return updateEncuadernado(encuadernado=encuadernado)

class deleteEncuadernado(Mutation):
    class Arguments:
        id_encuadernado = Int(required=True)

    encuadernado = Field(lambda: Encuadernado)

    def mutate(self, info, id_encuadernado):
        encuadernado = EncuadernadoModel.query.get(id_encuadernado)
        if encuadernado:
            db.session.delete(encuadernado)
            db.session.commit()

        return deleteEncuadernado(encuadernado=encuadernado)

class createFavoritoLibro(Mutation):
    class Arguments:
        id_usuario = String(required=True)
        id_libro = Int(required=True)

    favorito_libro = Field(lambda: FavoritoLibro)

    def mutate(self, info, id_usuario, id_libro):
        favorito_libro = FavoritoLibroModel(
            id_usuario=id_usuario,
            id_libro=id_libro
        )

        db.session.add(favorito_libro)
        db.session.commit()

        return createFavoritoLibro(favorito_libro=favorito_libro)

class deleteFavoritoLibro(Mutation):
    class Arguments:
        id_usuario = String(required=True)
        id_libro = Int(required=True)

    favorito_libro = Field(lambda: FavoritoLibro)

    def mutate(self, info, id_usuario, id_libro):
        favorito_libro = FavoritoLibroModel.query.filter_by(id_usuario=id_usuario, id_libro=id_libro).first()
        if favorito_libro:
            db.session.delete(favorito_libro)
            db.session.commit()

        return deleteFavoritoLibro(favorito_libro=favorito_libro)

class createGenero(Mutation):
    class Arguments:
        nombre_genero = String(required=True)
    
    genero = Field(lambda: Genero)

    def mutate(self, info, nombre_genero):
        genero = GeneroModel(nombre_genero=nombre_genero)

        db.session.add(genero)
        db.session.commit()
        
        return createGenero(genero=genero)

class updateGenero(Mutation):
    class Arguments:
        id_genero = Int(required=True)
        nombre_genero = String()

    genero = Field(lambda: Genero)

    def mutate(self, info, id_genero, nombre_genero=None):
        genero = GeneroModel.query.get(id_genero)
        if genero:
            if nombre_genero:
                genero.nombre_genero = nombre_genero
            db.session.add(genero)
            db.session.commit()

        return updateGenero(genero=genero)

class deleteGenero(Mutation):
    class Arguments:
        id_genero = Int(required=True)

    genero = Field(lambda: Genero)

    def mutate(self, info, id_genero):
        genero = GeneroModel.query.get(id_genero)
        if genero:
            db.session.delete(genero)
            db.session.commit()

        return deleteGenero(genero=genero)

class createLibroAutor(Mutation):
    class Arguments:
        id_libro = Int(required=True)
        id_autor = Int(required=True)

    libro_autor = Field(lambda: LibroAutor)

    def mutate(self, info, id_libro, id_autor):
        libro_autor = LibroAutorModel(
            id_libro=id_libro,
            id_autor=id_autor
        )

        db.session.add(libro_autor)
        db.session.commit()

        return createLibroAutor(libro_autor=libro_autor)

class deleteLibroAutor(Mutation):
    class Arguments:
        id_libro = Int(required=True)
        id_autor = Int(required=True)

    libro_autor = Field(lambda: LibroAutor)

    def mutate(self, info, id_libro, id_autor):
        libro_autor = LibroAutorModel.query.filter_by(id_libro=id_libro, id_autor=id_autor).first()
        if libro_autor:
            db.session.delete(libro_autor)
            db.session.commit()

        return deleteLibroAutor(libro_autor=libro_autor)


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

class deleteLibroGenero(Mutation):
    class Arguments:
        id_libro = Int(required=True)
        id_genero = Int(required=True)

    libro_genero = Field(lambda: LibroGenero)

    def mutate(self, info, id_libro, id_genero):
        libro_genero = LibroGeneroModel.query.filter_by(id_libro=id_libro, id_genero=id_genero).first()
        if libro_genero:
            db.session.delete(libro_genero)
            db.session.commit()

        return deleteLibroGenero(libro_genero=libro_genero)

class createEjemplarPromocion(Mutation):
    class Arguments:
        id_ejemplar = Int(required=True)
        id_promocion_descuento = Int(required=True)
    
    ejemplar_promocion = Field(lambda: EjemplarPromocion)

    def mutate(self, info, id_ejemplar, id_promocion_descuento):
        ejemplar_promocion = EjemplarPromocionModel(id_ejemplar=id_ejemplar, id_promocion_descuento=id_promocion_descuento)

        db.session.add(ejemplar_promocion)
        db.session.commit()
        
        return createEjemplarPromocion(ejemplar_promocion=ejemplar_promocion)

class deleteEjemplarPromocion(Mutation):
    class Arguments:
        id_promocion_descuento = Int(required=True)

    ejemplar_promocion = Field(lambda: EjemplarPromocion)

    def mutate(self, info, id_promocion_descuento):
        ejemplar_promociones = EjemplarPromocionModel.query.filter_by(id_promocion_descuento=id_promocion_descuento).all()
        for ejemplar_promocion in ejemplar_promociones:
            db.session.delete(ejemplar_promocion)
        db.session.commit()

        return deleteEjemplarPromocion(ejemplar_promocion=ejemplar_promocion)

class createLibro(Mutation):
    class Arguments:
        titulo = String(required=True)
        descripcion = String(required=True)
        imagen = String()

    libro = Field(lambda: Libro)

    def mutate(self, info, titulo, descripcion, imagen=None):
        libro = LibroModel(
            titulo=titulo,
            descripcion=descripcion,
            imagen=imagen
        )

        db.session.add(libro)
        db.session.commit()

        return createLibro(libro=libro)

class updateLibro(Mutation):
    class Arguments:
        id_libro = Int(required=True)
        titulo = String()
        descripcion = String()
        imagen = String()

    libro = Field(lambda: Libro)

    def mutate(self, info, id_libro, titulo=None, descripcion=None, imagen=None):
        libro = LibroModel.query.get(id_libro)
        if libro:
            if titulo:
                libro.titulo = titulo
            if descripcion:
                libro.descripcion = descripcion
            if imagen:
                libro.imagen = imagen

            db.session.add(libro)
            db.session.commit()

        return updateLibro(libro=libro)

class deleteLibro(Mutation):
    class Arguments:
        id_libro = Int(required=True)

    libro = Field(lambda: Libro)

    def mutate(self, info, id_libro):
        libro = LibroModel.query.get(id_libro)
        if libro:
            db.session.delete(libro)
            db.session.commit()

        return deleteLibro(libro=libro)

class createLineaCarrito(Mutation):
    class Arguments:
        id_carrito = Int(required=True)
        id_ejemplar = Int(required=True)
        cantidad = Int(required=True)
    
    linea_carrito = Field(lambda: LineaCarrito)
    def mutate(self, info, id_carrito, id_ejemplar, cantidad):
        linea_carrito = LineaCarritoModel(id_carrito=id_carrito, id_ejemplar=id_ejemplar, cantidad=cantidad)

        db.session.add(linea_carrito)
        db.session.commit()
        
        return createLineaCarrito(linea_carrito=linea_carrito)

class updateLineaCarrito(Mutation):
    class Arguments:
        id_carrito = Int(required=True)
        id_ejemplar = Int(required=True)
        cantidad = Int()
    
    linea_carrito = Field(lambda: LineaCarrito)

    def mutate(self, info, id_carrito, id_ejemplar, cantidad=None):
        linea_carrito = LineaCarritoModel.query.filter_by(id_carrito=id_carrito, id_ejemplar=id_ejemplar).first()
        if linea_carrito:
            if(cantidad):
                linea_carrito.cantidad = cantidad

            db.session.add(linea_carrito)
            db.session.commit()

        return updateLineaCarrito(linea_carrito=linea_carrito)

class deleteLineaCarrito(Mutation):
    class Arguments:
        id_ejemplar = Int(required=True)
        id_carrito = Int(required=True)

    linea_carrito = Field(lambda: LineaCarrito)

    def mutate(self, info, id_ejemplar, id_carrito):
        linea_carrito = LineaCarritoModel.query.filter_by(id_carrito=id_carrito, id_ejemplar=id_ejemplar).first()
        # Deberia ser por id_carrito?
        if linea_carrito:
            db.session.delete(linea_carrito)
            db.session.commit()

        return deleteLineaCarrito(linea_carrito=linea_carrito)

class createLineaPedido(Mutation):
    class Arguments:
        id_pedido = Int(required=True)
        id_ejemplar = Int(required=True)
        cantidad = Int(required=True)
        precio = Float(required=True)

    linea_pedido = Field(lambda: LineaPedido)

    def mutate(self, info, id_pedido, id_ejemplar, cantidad, precio):
        linea_pedido = LineaPedidoModel(
            id_pedido=id_pedido,
            id_ejemplar=id_ejemplar,
            cantidad=cantidad,
            precio=precio
        )

        db.session.add(linea_pedido)
        db.session.commit()

        return createLineaPedido(linea_pedido=linea_pedido)

class updateLineaPedido(Mutation):
    class Arguments:
        id_pedido = Int(required=True)
        id_ejemplar = Int(required=True)
        cantidad = Int(required=False)
        precio = Float(required=False)

    linea_pedido = Field(lambda: LineaPedido)

    def mutate(self, info, id_pedido, id_ejemplar, cantidad, precio):
        linea_pedido = LineaPedidoModel.query.filter_by(id_pedido=id_pedido, id_ejemplar=id_ejemplar).first()
        if linea_pedido:
            if cantidad:
                linea_pedido.cantidad = cantidad
            if precio:
                linea_pedido.precio = precio
            db.session.add(linea_pedido)
            db.session.commit()

        return updateLineaPedido(linea_pedido=linea_pedido)

class deleteLineaPedido(Mutation):
    class Arguments:
        id_pedido = Int(required=True)
        id_ejemplar = Int(required=True)

    linea_pedido = Field(lambda: LineaPedido)

    def mutate(self, info, id_pedido, id_ejemplar):
        linea_pedido = LineaPedidoModel.query.filter_by(id_pedido=id_pedido, id_ejemplar=id_ejemplar).first()
        if linea_pedido:
            db.session.delete(linea_pedido)
            db.session.commit()

        return deleteLineaPedido(linea_pedido=linea_pedido)

class createPedido(Mutation):
    class Arguments:
        id_envio = Int(required=True)
        fecha = String(required=False)
        costo_envio = Float(required=True)
        total = Float(required=False)
        id_usuario = String(required=True)
        total_con_descuento = Float(required=False)
        id_direccion = Int(required=False)


    pedido = Field(lambda: Pedido)

    def mutate(self, info, id_envio, costo_envio, id_usuario, id_direccion=None, fecha=None, total=None, total_con_descuento=None):
        pedido = PedidoModel(
            id_envio=id_envio,
            fecha=fecha,
            costo_envio=costo_envio,
            total=total,
            id_usuario=id_usuario,
            total_con_descuento=total_con_descuento,
            id_direccion=id_direccion
        )

        db.session.add(pedido)
        db.session.commit()

        return createPedido(pedido=pedido)

class updatePedido(Mutation):
    class Arguments:
        id_pedido = Int(required=True)
        id_envio = Int()
        fecha = String()
        costo_envio = Float()
        total = Float()
        id_usuario = String()
        id_direccion = Int()
        total_con_descuento = Float()

    pedido = Field(lambda: Pedido)

    def mutate(self, info, id_pedido, id_envio=None, fecha=None, costo_envio=None, total=None, id_usuario=None, id_direccion=None, total_con_descuento=None):
        pedido = PedidoModel.query.get(id_pedido)
        if pedido:
            if id_envio is not None:
                pedido.id_envio = id_envio
            if fecha:
                pedido.fecha = fecha
            if costo_envio is not None:
                pedido.costo_envio = costo_envio
            if total is not None:
                pedido.total = total
            if id_usuario:
                pedido.id_usuario = id_usuario
            if id_direccion is not None:
                pedido.id_direccion = id_direccion
            if total_con_descuento is not None:
                pedido.total_con_descuento = total_con_descuento

            db.session.add(pedido)
            db.session.commit()

        return updatePedido(pedido=pedido)

class deletePedido(Mutation):
    class Arguments:
        id_pedido = Int(required=True)

    pedido = Field(lambda: Pedido)

    def mutate(self, info, id_pedido):
        pedido = PedidoModel.query.get(id_pedido)
        if pedido:
            db.session.delete(pedido)
            db.session.commit()

        return deletePedido(pedido=pedido)

class createPromocionDescuento(Mutation):
    class Arguments:
        nombre_promocion = String(required=True)
        porcentaje = Float(required=True)
        fecha_inicio = String(required=True)
        fecha_fin = String(required=True)
        imagen = String()

    promocion_descuento = Field(lambda: PromocionDescuento)

    def mutate(self, info, nombre_promocion=None, porcentaje=None, fecha_inicio=None, fecha_fin=None, imagen=None):
        promocion_descuento = PromocionDescuentoModel(
            nombre_promocion=nombre_promocion,
            porcentaje=porcentaje,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            imagen=imagen
        )

        db.session.add(promocion_descuento)
        db.session.commit()

        return createPromocionDescuento(promocion_descuento=promocion_descuento)

class updatePromocionDescuento(Mutation):
    class Arguments:
        id_promocion_descuento = Int(required=True)
        nombre_promocion = String()
        porcentaje = Float()
        fecha_inicio = String()
        fecha_fin = String()
        imagen = String()

    promocion_descuento = Field(lambda: PromocionDescuento)

    def mutate(self, info, id_promocion_descuento, nombre_promocion=None, porcentaje=None, fecha_inicio=None, fecha_fin=None, imagen=None):
        promocion_descuento = PromocionDescuentoModel.query.get(id_promocion_descuento)
        if promocion_descuento:
            if nombre_promocion:
                promocion_descuento.nombre_promocion = nombre_promocion
            if porcentaje is not None:
                promocion_descuento.porcentaje = porcentaje
            if fecha_inicio:
                promocion_descuento.fecha_inicio = fecha_inicio
            if fecha_fin:
                promocion_descuento.fecha_fin = fecha_fin
            if imagen:
                promocion_descuento.imagen = imagen

            db.session.add(promocion_descuento)
            db.session.commit()

        return updatePromocionDescuento(promocion_descuento=promocion_descuento)

class deletePromocionDescuento(Mutation):
    class Arguments:
        id_promocion_descuento = Int(required=True)

    promocion_descuento = Field(lambda: PromocionDescuento)

    def mutate(self, info, id_promocion_descuento):
        promocion_descuento = PromocionDescuentoModel.query.get(id_promocion_descuento)
        if promocion_descuento:
            db.session.delete(promocion_descuento)
            db.session.commit()

        return deletePromocionDescuento(promocion_descuento=promocion_descuento)

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

class updateResenia(Mutation):
    class Arguments:
        id_usuario = String(required=True)
        id_libro = Int(required=True)
        texto = String()
        valoracion = Int()

    resenia = Field(lambda: Resenia)

    def mutate(self, info, id_usuario, id_libro, texto=None, valoracion=None):
        resenia = ReseniaModel.query.filter_by(id_usuario=id_usuario, id_libro=id_libro).first()
        if resenia:
            if texto:
                resenia.texto = texto
            if valoracion is not None:
                resenia.valoracion = valoracion
            db.session.add(resenia)
            db.session.commit()

        return updateResenia(resenia=resenia)

class deleteResenia(Mutation):
    class Arguments:
        id_usuario = String(required=True)
        id_libro = Int(required=True)

    resenia = Field(lambda: Resenia)

    def mutate(self, info, id_usuario, id_libro):
        resenia = ReseniaModel.query.filter_by(id_usuario=id_usuario, id_libro=id_libro).first()
        if resenia:
            db.session.delete(resenia)
            db.session.commit()

        return deleteResenia(resenia=resenia)

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

class createTipoEnvio(Mutation):
    class Arguments:
        descripcion = String(required=True)
    
    tipo_envio = Field(lambda: TipoEnvio)

    def mutate(self, info, descripcion):
        tipo_envio = TipoEnvioModel(descripcion=descripcion)

        db.session.add(tipo_envio)
        db.session.commit()
        
        return createTipoEnvio(tipo_envio=tipo_envio)

class updateTipoEnvio(Mutation):
    class Arguments:
        id_tipo_envio = Int(required=True)
        descripcion = String()

    tipo_envio = Field(lambda: TipoEnvio)

    def mutate(self, info, id_tipo_envio, descripcion=None):
        tipo_envio = TipoEnvioModel.query.get(id_tipo_envio)
        if tipo_envio:
            if descripcion:
                tipo_envio.descripcion = descripcion
            db.session.add(tipo_envio)
            db.session.commit()

        return updateTipoEnvio(tipo_envio=tipo_envio)

class deleteTipoEnvio(Mutation):
    class Arguments:
        id_tipo_envio = Int(required=True)

    tipo_envio = Field(lambda: TipoEnvio)

    def mutate(self, info, id_tipo_envio):
        tipo_envio = TipoEnvioModel.query.get(id_tipo_envio)
        if tipo_envio:
            db.session.delete(tipo_envio)
            db.session.commit()

        return deleteTipoEnvio(tipo_envio=tipo_envio)

class createUsuario(Mutation):
    class Arguments:
        id_usuario = String(required=True)
        nombre = String(required=True)
        apellido = String(required=True)
        email = String(required=True)
        imagen = String(required=False)
        rol = Int(required=False)
    
    usuario = Field(lambda: Usuario)

    def mutate(self, info, id_usuario, nombre, apellido, email, imagen=None, rol=None):
        usuario = UsuarioModel(id_usuario=id_usuario, nombre=nombre, apellido=apellido, email=email, imagen=imagen, rol=rol, fecha_creacion=datetime.now())

        db.session.add(usuario)
        db.session.commit()
        
        return createUsuario(usuario=usuario)

class updateUsuario(Mutation):
    class Arguments:
        id_usuario = String(required=True)
        nombre = String()
        apellido = String()
        email = String()
        imagen = String()
        rol = Int()

    usuario = Field(lambda: Usuario)

    def mutate(self, info, id_usuario, nombre=None, apellido=None, email=None, imagen=None, rol=None):
        usuario = UsuarioModel.query.get(id_usuario)
        if usuario:
            if nombre:
                usuario.nombre = nombre
            if apellido:
                usuario.apellido = apellido
            if email:
                usuario.email = email
            if imagen:
                usuario.imagen = imagen
            if rol:
                usuario.rol = rol
            db.session.add(usuario)
            db.session.commit()

        return updateUsuario(usuario=usuario)

class deleteUsuario(Mutation):
    class Arguments:
        id_usuario = String(required=True)

    usuario = Field(lambda: Usuario)

    def mutate(self, info, id_usuario):
        usuario = UsuarioModel.query.get(id_usuario)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()

        return deleteUsuario(usuario=usuario)

class createEjemplar(Mutation):
    class Arguments:
        isbn = Int(required=True)
        precio = Float(required=True)
        stock = Int(required=True)
        dimensiones = String(required=True)
        paginas = Int(required=True)
        id_libro = Int(required=True)
        id_editorial = Int(required=True)
        id_encuadernado = Int(required=True)
    
    ejemplar = Field(lambda: Ejemplar)

    def mutate(self, info, isbn, precio, stock, dimensiones, paginas, id_libro, id_editorial, id_encuadernado):
        ejemplar = EjemplarModel(isbn=isbn, precio=precio, stock=stock, dimensiones=dimensiones, paginas=paginas, id_libro=id_libro, id_editorial=id_editorial, id_encuadernado=id_encuadernado)

        db.session.add(ejemplar)
        db.session.commit()
        
        return createEjemplar(ejemplar=ejemplar)

class updateEjemplar(Mutation):
    class Arguments:
        isbn = Int(required=True)
        precio = Float()
        stock = Int()
        dimensiones = String()
        paginas = Int()
        id_libro = Int()
        id_editorial = Int()
        id_encuadernado = Int()

    ejemplar = Field(lambda: Ejemplar)

    def mutate(self, info, isbn, precio=None, stock=None, dimensiones=None, paginas=None, id_libro=None, id_editorial=None, id_encuadernado=None):
        ejemplar = EjemplarModel.query.get(isbn)
        if ejemplar:
            if precio:
                ejemplar.precio = precio
            if stock:
                ejemplar.stock = stock
            if dimensiones:
                ejemplar.dimensiones = dimensiones
            if paginas:
                ejemplar.paginas = paginas
            if id_libro:
                ejemplar.id_libro = id_libro
            if id_editorial:
                ejemplar.id_editorial = id_editorial
            if id_encuadernado:
                ejemplar.id_encuadernado = id_encuadernado
            db.session.add(ejemplar)
            db.session.commit()

        return updateEjemplar(ejemplar=ejemplar)

class Mutation(ObjectType):
    create_ejemplar = createEjemplar.Field()
    update_ejemplar = updateEjemplar.Field()
    create_autor = createAutor.Field()
    update_autor = updateAutor.Field()
    delete_autor = deleteAutor.Field()
    create_ciudad = createCiudad.Field()
    update_ciudad = updateCiudad.Field()
    delete_ciudad = deleteCiudad.Field()
    create_deseo_libro = createDeseoLibro.Field()
    delete_deseo_libro = deleteDeseoLibro.Field()
    create_direccion = createDireccion.Field()
    update_direccion = updateDireccion.Field()
    delete_direccion = deleteDireccion.Field()
    create_editorial = createEditorial.Field()
    update_editorial = updateEditorial.Field()
    delete_editorial = deleteEditorial.Field()
    create_encuadernado = createEncuadernado.Field()
    update_encuadernado = updateEncuadernado.Field()
    delete_encuadernado = deleteEncuadernado.Field()
    create_favorito_libro = createFavoritoLibro.Field()
    delete_favorito_libro = deleteFavoritoLibro.Field()
    create_genero = createGenero.Field()
    update_genero = updateGenero.Field()
    delete_genero = deleteGenero.Field()
    create_libro_autor = createLibroAutor.Field()
    delete_libro_autor = deleteLibroAutor.Field()
    create_libro_genero = createLibroGenero.Field()
    delete_libro_genero = deleteLibroGenero.Field()
    create_ejemplar_promocion = createEjemplarPromocion.Field()
    delete_ejemplar_promocion = deleteEjemplarPromocion.Field()
    create_libro = createLibro.Field()
    update_libro = updateLibro.Field()
    delete_libro = deleteLibro.Field()
    create_linea_carrito = createLineaCarrito.Field()
    update_linea_carrito = updateLineaCarrito.Field()
    delete_linea_carrito = deleteLineaCarrito.Field()
    create_linea_pedido = createLineaPedido.Field()
    update_linea_pedido = updateLineaPedido.Field()
    delete_linea_pedido = deleteLineaPedido.Field()
    create_pedido = createPedido.Field()
    update_pedido = updatePedido.Field()
    delete_pedido = deletePedido.Field()
    create_promocion_descuento = createPromocionDescuento.Field()
    update_promocion_descuento = updatePromocionDescuento.Field()
    delete_promocion_descuento = deletePromocionDescuento.Field()
    create_resenia = createResenia.Field()
    update_resenia = updateResenia.Field()
    delete_resenia = deleteResenia.Field()
    create_sesion = createSesion.Field()
    delete_sesion = deleteSesion.Field()
    create_tipo_envio = createTipoEnvio.Field()
    update_tipo_envio = updateTipoEnvio.Field()
    delete_tipo_envio = deleteTipoEnvio.Field()
    create_usuario = createUsuario.Field()
    update_usuario = updateUsuario.Field()
    delete_usuario = deleteUsuario.Field()