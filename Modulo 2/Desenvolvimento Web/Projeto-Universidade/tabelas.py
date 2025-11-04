import datetime
from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True )
    nome= Column(String(225),nullabe=False)
    email= Column(String(225),nullable=False)
    senha_hash= Column(String(225),nullable=False)
    criado_em=  Column(DateTime(timezone=True), default=datetime.datetime.now)

    notas = relationship("Nota", back_populates="autor")
    usuario_enderecos = relationship("Enderecos",
        secondary= usuario_endereco_associacao,
        back_populates="moradores"
    )

class Nota(Base):
    __tablename__ = "notas"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_usuario = Column (Integer, ForeignKey("usuarios.id"), nullable=False)
    titulo = Column (String(255), nullable=False)
    conteudo = Column(Text)
    criado_em = Column (DateTime(timezone=True), default=datetime.datetime.now)
    modificado_em = Column (DateTime(timezone=True), default=datetime.datetime.now)
    autor = relationship("Usuario", back_populates="notas")