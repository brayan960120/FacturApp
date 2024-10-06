from sqlalchemy import Column, Integer, String, ForeignKey
from src.models import session, Base

class Categoria(Base):
    __tablename__ = 'Categoria'
    id_categoria = Column(Integer, primary_key = True)
    nombre_categoria = Column(String(45), unique=True, nullable=False)
    id_usuario= Column(Integer, ForeignKey('id_usuario'), nullable=False)


    def __init__(self, nombre_categoria, id_usuario):
       self.nombre_categoria = nombre_categoria
       self.id_usuario = id_usuario