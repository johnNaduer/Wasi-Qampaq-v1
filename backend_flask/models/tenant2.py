#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from .base_model2 import Base, basemodel
from .espacio2 import espacio
from .propiedad2 import propiedad

class tenant(basemodel, Base):
    __tablename__ = 'tenant2'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)
    first_last_name = Column(String(120), nullable=False)
    second_last_name = Column(String(60), nullable=False)
    dni = Column(Integer, nullable=False)
    phone = Column(Integer, nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    start_date = Column(String(20), nullable=False)
    end_date = Column(String(20), nullable=False) 
    espacio_numero = Column(Integer, ForeignKey('espacio2.id'), nullable=False)
    id_propiedad = Column(Integer, ForeignKey('propiedad2.id'), nullable=False)

    espacio = relationship("espacio", backref="tenants")
    propiedad = relationship("propiedad", backref="tenants")
