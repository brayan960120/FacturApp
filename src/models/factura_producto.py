from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Factura_producto(Base):
    __tablename__ = 'Factura_producto'
    id_factura_producto = Column(Integer, primary_key = True)
    cantidad = Column(Integer, nullable=False)
    nombre_producto= Column(String(45), nullable=False)
    precio_unitario= Column(Float(10,8), nullable=False)
    id_factura= Column(Integer, ForeignKey('id_factura'), unique=True, nullable=False)
    id_cliente= Column(Integer, ForeignKey('id_cliente'), unique=True, nullable=False)

    def __init__(self, cantidad, nombre_producto, precio_unitario, id_factura, id_cliente):
       self.cantidad = cantidad
       self.nombre_producto = nombre_producto
       self.precio_unitario = precio_unitario
       self.id_factura = id_factura
       self.id_cliente = id_cliente