from sqlalchemy import Column, Integer, ForeignKey, DateTime

class Factura():
    __tablename__ = 'Factura'
    id_factura = Column(Integer, primary_key = True)
    fecha_factura= Column(DateTime, unique=True, nullable=False)
    numero_factura= Column(Integer, unique=True, nullable=False)
    id_cliente= Column(Integer, ForeignKey('id_cliente'), nullable=False)
    id_usuario= Column(Integer, ForeignKey('id_usuario'), nullable=False)