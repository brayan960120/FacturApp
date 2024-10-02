from sqlalchemy import Column, Integer, String, ForeignKey

class Categoria():
    __tablename__ = 'Categoria'
    id_categoria = Column(Integer, primary_key = True)
    nombre_categoria = Column(String(45), unique=True, nullable=False)
    id_usuario= Column(Integer, ForeignKey('id_usuario'), nullable=False)