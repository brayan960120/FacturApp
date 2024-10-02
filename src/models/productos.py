from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Producto():
    __tablename__ = 'Producto'
    id_producto = Column(Integer, primary_key = True)
    descripcion = Column(String(250), unique=True, nullable=False)
    valor_unitario= Column(Float(10,8), nullable=False)
    unidad_de_medida= Column(String(3), nullable=False)
    cantidad_stock= Column(Integer, nullable=False)
    id_categoria= Column(Integer, ForeignKey('id_categoria'), nullable=False)
    id_factura_producto= Column(Integer, ForeignKey('id_factura_producto'), nullable=False)