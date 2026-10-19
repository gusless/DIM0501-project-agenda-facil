# Documentação

A referência da API está em `API.md`. Para gerar páginas HTML a partir das docstrings usando a biblioteca padrão:

```bash
python -m pydoc -w agenda_facil.models agenda_facil.validators agenda_facil.service
```

O comando gera arquivos HTML no diretório corrente. Como o enunciado cita especificamente `pdoc` ou `sphinx-apidoc`, confirme com o professor se `pydoc` (biblioteca padrão) é aceito, pois as duas ferramentas citadas são externas.
