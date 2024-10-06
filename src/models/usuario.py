from sqlalchemy import Column, Integer, String, Boolean, Date
from src.models import session, Base

class Usuario(Base):
    __tablename__ = 'Usuario'
    id_usuario = Column(Integer, primary_key = True)
    cuenta_activa = Column(Boolean, nullable=False)
    fecha_nacimiento= Column(Date, nullable=False)
    contraseña= Column(String(45), nullable=False)
    nombre_completo= Column(String(90), nullable=False)
    email= Column(String(90), nullable=False, unique=True)


    def __init__(self, cuenta_activa, fecha_nacimiento, contraseña, nombre_completo, email):
       self.cuenta_activa = cuenta_activa
       self.fecha_nacimiento = fecha_nacimiento
       self.contraseña = contraseña
       self.nombre_completo = nombre_completo
       self.email = email