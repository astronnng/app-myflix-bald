# myflix

Pequeno projeto FastAPI para gerenciamento de séries.

Execução em ambiente de desenvolvimento (recomendado):

PowerShell:

```powershell
# Ative a virtualenv (se estiver usando a criada no repositório)
.\Scripts\Activate.ps1

# Inicie o servidor (execute na raiz do projeto)
python -m uvicorn src.server:app --reload --host 127.0.0.1 --port 8000
```

Alternativa (quando preferir executar apontando o package root):

```powershell
$env:PYTHONPATH = '.'
python -m uvicorn server:app --reload --host 127.0.0.1 --port 8000
```

Observações:
- O módulo ASGI é `src.server:app` porque o código usa imports `src.*`.
- Mantivemos `orm_mode` nos schemas por compatibilidade com Pydantic v1.
