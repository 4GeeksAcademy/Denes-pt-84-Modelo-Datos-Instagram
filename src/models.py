import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False) #nullable=false, al estar falso quiere decir que no puede quedar vacio
    last_name = Column(String(250))
    email = Column(String(50), nullable=False, unique=True)# unique=True quiere decir que es unico y no se puede repetir en la tabla
    comentario = relationship('Coments', back_populates='person')
    publicacion = relationship('Post', back_populates = 'Person')

class Coments(Base):
    __tablename__ = 'comentario'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    text = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    person = relationship('Person', back_populates ='comentario')
    publicacion = relationship('Post', back_populates = 'comentario')

class Post(Base): 
    __tablename__= 'publicacion'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comentario = relationship('Coments', back_populates = 'publicacion')
    person = relationship('Person', back_populates ='publicacion')
    multimedia= relationship('Media', back_populates = 'publicacion')
    
class Media(Base): 
    __tablename__= 'multimedia'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('publicacion.id'))
    publicacion = relationship('Post', back_populates = 'multimedia')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
