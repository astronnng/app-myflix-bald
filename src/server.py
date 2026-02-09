
from fastapi import FastAPI, Depends
from src.infra.sqlalchemy.repositorios.series import RepositorioSeries
from src.infra.sqlalchemy.config.database import Session, create_db_and_tables, get_db
from src.schemas import schemas
from sqlalchemy.orm import Session

#criar as tabelas no banco de dados
create_db_and_tables()


app = FastAPI()


@app.post("/series/")
def criar_serie(serie: schemas.Serie, db: Session = Depends(get_db)):
    serie_criada = RepositorioSeries(db).criar(serie)
    return serie_criada


@app.get("/series/")
def listar_series(db: Session = Depends(get_db)):
    series_listadas = RepositorioSeries(db).listar(schemas.Serie)
    return series_listadas


@app.get("/series/{serie_id}")
def obter_serie(serie: schemas.Serie, db: Session = Depends(get_db)):
    serie_obtida = RepositorioSeries(db).obter(serie)
    return serie_obtida


@app.delete("/series/")
def remover_serie(serie: schemas.Serie, db: Session = Depends(get_db)):
    resultado_remocao = RepositorioSeries(db).remover_serie(serie)
    if resultado_remocao:
        return {"message": "Série removida com sucesso"}
    else:
        return {"message": "Série não encontrada"}
    


