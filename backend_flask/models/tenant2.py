#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from .base_model2 import Base, basemodel
from .espacio2 import espacio

class tenant(basemodel, Base):
    __tablename__ = 'tenant2'
    name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(60), nullable=False)
    phone = Column(Integer, nullable=False)
    espacio_numero = Column(Integer, ForeignKey('espacio2.id'), nullable=False)

    espacio = relationship("espacio", backref="tenants")
