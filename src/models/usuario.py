from sqlalchemy import Column, Integer, String, Boolean, Date

class Usuario():
    __tablename__ = 'Usuario'
    id_usuario = Column(Integer, primary_key = True)
    cuenta_activa = Column(Boolean, nullable=False)
    fecha_nacimiento= Column(Date, nullable=False)
    contraseña= Column(String(45), nullable=False)
    nombre_completo= Column(String(90), nullable=False)
    email= Column(String(90), nullable=False, unique=True)