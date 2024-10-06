from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Producto(Base):
    __tablename__ = 'Producto'
    id_producto = Column(Integer, primary_key = True)
    descripcion = Column(String(250), unique=True, nullable=False)
    valor_unitario= Column(Float(10,8), nullable=False)
    unidad_de_medida= Column(String(3), nullable=False)
    cantidad_stock= Column(Integer, nullable=False)
    id_categoria= Column(Integer, ForeignKey('id_categoria'), nullable=False)
    id_factura_producto= Column(Integer, ForeignKey('id_factura_producto'), nullable=False)



    def __init__(self, descripcion, valor_unitario, unidad_de_medida, cantidad_stock, id_categoria, id_factura_producto):
       self.descripcion = descripcion
       self.valor_unitario = valor_unitario
       self.unidad_de_medida = unidad_de_medida
       self.cantidad_stock = cantidad_stock
       self.id_categoria = id_categoria
       self.id_factura_producto = id_factura_producto