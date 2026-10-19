# AgendaFácil

Sistema em memória para marcar, remarcar e listar atendimentos de uma clínica. Projeto da Unidade 1 de DIM0501 — Boas Práticas de Programação.

## Membro

Augusto César da Silva Carvalho | 20250058768

## Requisitos

- Python 3.10 ou superior.
- O programa e os testes usam apenas a biblioteca padrão; não é necessário instalar dependências.

## Estrutura

- `agenda_facil/models.py`: tipo `Atendimento`, com campos nomeados.
- `agenda_facil/validators.py`: validações e constantes de negócio.
- `agenda_facil/service.py`: regras e operações da agenda, sem impressão no terminal.
- `main.py`: demonstração e apresentação das mensagens.
- `docs/`: documentação de API.

## Executar

Na pasta raiz do projeto:

```bash
python main.py
```

Saída esperada:

```text
Atendimento marcado para Ana
Horario ocupado
Atendimento marcado para Carla
Remarcado
14 Carla Dra. Souza MARCADO
```

## Gerar documentação

A implementação não depende de ferramentas externas. Para gerar documentação HTML com a ferramenta padrão `pydoc`, execute na raiz:

```bash
python -m pydoc -w agenda_facil.models agenda_facil.validators agenda_facil.service
```

Os arquivos HTML são gerados na pasta atual; mova-os para `docs/` se desejar manter a documentação gerada junto ao projeto. Os arquivos `docs/API.md` e `docs/README.md` fornecem uma referência textual versionada. O enunciado menciona pdoc ou sphinx-apidoc; essas ferramentas são externas, portanto não foram adicionadas como dependências do projeto para respeitar a restrição de biblioteca padrão.

