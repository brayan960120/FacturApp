from sqlalchemy import Column, Integer, String
from src.models import session, Base

class Cliente(Base):
    __tablename__ = 'Cliente'
    id_cliente = Column(Integer, primary_key = True)
    nombre_completo = Column(String(90), nullable=False)
    telefono= Column(Integer, nullable=True)
    identificacion= Column(String(45),unique=True, nullable=True)
    direccion= Column(String(90), nullable=True)
    email= Column(String(90), nullable=True)
    

    def __init__(self, nombre_completo, telefono, identificacion, direccion, email):
       self.nombre_completo = nombre_completo
       self.telefono = telefono
       self.identificacion = identificacion
       self.direccion = direccion
       self.email = email