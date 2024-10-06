from sqlalchemy import Column, Integer, ForeignKey, DateTime
from src.models import session, Base


class Factura(Base):
    __tablename__ = 'Factura'
    id_factura = Column(Integer, primary_key = True)
    fecha_factura= Column(DateTime, unique=True, nullable=False)
    numero_factura= Column(Integer, unique=True, nullable=False)
    id_cliente= Column(Integer, ForeignKey('id_cliente'), nullable=False)
    id_usuario= Column(Integer, ForeignKey('id_usuario'), nullable=False)


    
    def __init__(self, fecha_factura, numero_factura, id_cliente, id_usuario):
       self.fecha_factura = fecha_factura
       self.numero_factura= numero_factura
       self.id_cliente = id_cliente
       self.id_usuario = id_usuario