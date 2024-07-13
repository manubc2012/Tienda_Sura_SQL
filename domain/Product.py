from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI

Base = declarative_base()

class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(length=50))
    precio = Column(Integer)

# Crear el engine
engine = create_engine(DATABASE_URI, echo=True)

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear todas las tablas definidas en los modelos
Base.metadata.create_all(engine)