from sqlalchemy import Column, Integer, String

class Cliente():
    __tablename__ = 'Cliente'
    id_cliente = Column(Integer, primary_key = True)
    nombre_completo = Column(String(90), nullable=False)
    telefono= Column(Integer, nullable=True)
    identificacion= Column(String(45),unique=True, nullable=True)
    direccion= Column(String(90), nullable=True)
    email= Column(String(90), nullable=True)
    