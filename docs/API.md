# Documentação de API — AgendaFácil

## `agenda_facil.models.Atendimento`

Dataclass que representa um atendimento. Campos: `paciente`, `profissional`, `data`, `hora`, `duracao` e `status`.

## `agenda_facil.validators`

- `validar_texto(valor, campo)`: exige texto não vazio.
- `validar_data(data_texto)`: exige data existente no formato `AAAA-MM-DD`.
- `validar_horario(hora, duracao)`: valida expediente, duração e horário de término.

As funções de validação lançam `ValueError` com mensagens explicativas quando os dados são inválidos.

## `agenda_facil.service.Agenda`

- `marcar(...)`: agenda e retorna `True`; retorna `False` se houver conflito.
- `remarcar(...)`: remarca e retorna `True`; retorna `False` se o atendimento não existir ou houver conflito.
- `listar_por_data(data)`: retorna os atendimentos da data.
- `existe_conflito(...)`: centraliza a regra de conflito.
- `atendimentos()`: retorna uma tupla dos atendimentos cadastrados.

As operações de serviço não imprimem mensagens; a camada de apresentação decide o que exibir.
