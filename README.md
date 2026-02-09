## 🚀 myflix — API simples de séries

Aplicação minimalista em FastAPI para criar, listar, obter e remover séries. Ideal para testes e aprendizado sobre FastAPI + SQLAlchemy.

Principais pontos:
- Endpoints REST para `series` (criar, listar, obter, remover) ✅
- Banco SQLite local (arquivo `myflix.db`) 🗄️
- Modelos com SQLAlchemy e schemas Pydantic (usando `orm_mode` para compatibilidade) 🧩

Execução (na raiz do projeto)

PowerShell:

```powershell
# (opcional) ative a virtualenv do projeto
.\myflix\Scripts\Activate.ps1

# inicie o servidor (use o módulo do package `src`)
python -m uvicorn src.server:app --reload --host 127.0.0.1 --port 8000
```

Observações rápidas:
- Use `src.server:app` porque o projeto usa a package root `src/`.
- Se preferir, exporte `PYTHONPATH` e rode `python -m uvicorn server:app` a partir de `src/`.
- Arquivo do banco: `myflix.db` (adicionado ao `.gitignore` para evitar commits de dados locais).

Quer que eu adicione exemplos de requisições (curl) ou um OpenAPI/Swagger rápido? 😄

### 📬 Exemplos de requisições (curl)

- Criar uma série (POST):

```bash
curl -X POST "http://127.0.0.1:8000/series/" \
	-H "Content-Type: application/json" \
	-d '{"id": 1, "titulo": "Minha Série", "ano": 2023, "genero": "Drama", "qtd_temporadas": 2}'
```

- Listar séries (GET):

```bash
curl "http://127.0.0.1:8000/series/"
```

- Obter série por ID (GET) — exemplo usando o path param:

```bash
curl "http://127.0.0.1:8000/series/1"
```

- Remover série (DELETE):

```bash
curl -X DELETE "http://127.0.0.1:8000/series/" \
	-H "Content-Type: application/json" \
	-d '{"id": 1, "titulo": "Minha Série", "ano": 2023, "genero": "Drama", "qtd_temporadas": 2}'
```

> Dica: abra `http://127.0.0.1:8000/docs` no navegador para a documentação interativa (Swagger UI). ✨
