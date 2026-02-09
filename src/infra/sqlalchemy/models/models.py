from src.infra.sqlalchemy.config.database import Base
from sqlalchemy import Column, Integer, String


class Serie(Base):
    __tablename__ = "series" # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    ano = Column(Integer)
    genero = Column(String)
    qtd_temporadas = Column(Integer)


