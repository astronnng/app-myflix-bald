from src.infra.sqlalchemy.models import models
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models.models import Serie
from src.schemas import schemas



class RepositorioSeries:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, serie: schemas.Serie):
        db_serie = Serie(titulo=serie.titulo, ano=serie.ano, genero=serie.genero, qtd_temporadas=serie.qtd_temporadas)
        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)
        return db_serie


    def listar(self, serie: schemas.Serie):
        db_lista = self.db.query(models.Serie).all()
        return db_lista

    def obter(self, serie: schemas.Serie):
        db_serie_obter = self.db.query(models.Serie).filter(models.Serie.id == serie.id).first()
        return db_serie_obter
        

    def remover_serie(self, serie: schemas.Serie):
        db_serie_remover = self.db.query(models.Serie).filter(models.Serie.id == serie.id).first()
        if db_serie_remover:
            self.db.delete(db_serie_remover)
            self.db.commit()
            return True
        return False
    