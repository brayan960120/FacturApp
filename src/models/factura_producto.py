from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Factura_producto():
    __tablename__ = 'Factura_producto'
    id_factura_producto = Column(Integer, primary_key = True)
    cantidad = Column(Integer, nullable=False)
    nombre_producto= Column(String(45), nullable=False)
    precio_unitario= Column(Float(10,8), nullable=False)
    id_factura= Column(Integer, ForeignKey('id_factura'), unique=True, nullable=False)
    id_cliente= Column(Integer, ForeignKey('id_cliente'), unique=True, nullable=False)