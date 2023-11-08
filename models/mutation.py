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
    Usuario
)

from .libro import Libro as LibroModel
from .carrito import Carrito as CarritoModel
from .linea_carrito import LineaCarrito as LineaCarritoModel
from .usuario import Usuario as UsuarioModel
from .sesion import Sesion as SesionModel

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
        id_session = String(required=True)
        id_usuario = String(required=True)

    
    sesion = Field(lambda: Sesion)

    def mutate(self, info, id_session, id_usuario):
        sesion = SesionModel(id_session=id_session, id_usuario=id_usuario)

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

class Mutation(ObjectType):
    create_linea_carrito = createLineaCarrito.Field()
    update_linea_carrito = updateLineaCarrito.Field()
    delete_linea_carrito = deleteLineaCarrito.Field()
    create_usuario = createUsuario.Field()
    create_sesion = createSesion.Field()
    delete_sesion = deleteSesion.Field()
