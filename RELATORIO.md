# Relatório — Projeto da Unidade 1: AgendaFácil

**Disciplina:** DIM0501 — Boas Práticas de Programação  
**Linguagem:** Python 3.10+  
**Integrante e matrículas:** Augusto César da Silva Carvalho | 20250058768 
**Repositório/arquivo:** [DIM0501 - Projeto Agenda Fácil](https://github.com/gusless/DIM0501-project-agenda-facil)

## 1. Diagnóstico do código-base

| # | Categoria | Anomalia e localização | Por que é um problema |
|---:|---|---|---|
| 1 | Adequação e lógica | `add`: valida apenas `h >= 8`, `h < 18` e `dur > 0`. | Aceita durações fora da regra e atendimentos que terminam depois das 18h. |
| 2 | Adequação e lógica | `rem`: não valida a nova data nem o horário de remarcação. | Um atendimento pode ser movido para uma data ou horário inválido. |
| 3 | Manutenibilidade | `ag` é uma lista global compartilhada. | Qualquer função pode alterar os dados e testes diferentes podem interferir uns nos outros. |
| 4 | Manutenibilidade | Atendimentos são listas e acessados por índices (`a[2]`, `a[3]`, `a[5]`). | A intenção dos campos fica implícita e trocar a ordem dos valores causa erros difíceis de detectar. |
| 5 | Organização e estética | Funções chamadas `add`, `rem` e `lst`. | Os nomes não comunicam claramente a responsabilidade e tornam o código menos legível. |
| 6 | Organização e estética | `add` valida, procura conflito, armazena e imprime. | Mudanças na regra ou na interface exigem editar a mesma função. |
| 7 | Programação defensiva e segurança | `except: pass` em `add`. | Erros de programação e entradas inválidas são ocultados; o usuário não sabe por que a operação falhou. |
| 8 | Programação defensiva e segurança | Entradas não são verificadas quanto a tipo, data e duração. | Valores inesperados podem entrar na agenda e gerar resultados incoerentes. |
| 9 | Desempenho e recursos | `add` percorre todos os atendimentos para procurar conflito, mesmo após encontrá-lo. | Faz verificações desnecessárias à medida que a agenda cresce. |
| 10 | Desempenho e recursos | `rem` faz uma busca pelo atendimento e outra busca completa por conflito. | A operação repete percursos pela lista e mistura localização com validação. |
| 11 | Adequação e lógica | A condição de conflito compara apenas profissional, data e hora de início. | A implementação não considera sobreposição parcial entre intervalos; essa limitação não está resolvida pela regra explícita do enunciado, que define conflito por mesmo dia e horário. |
| 12 | Manutenibilidade | Valores como `8`, `18`, `0` e `"MARCADO"` aparecem diretamente nas operações. | Alterar uma regra exige localizar números e textos espalhados pelo código. |

## 2. O que foi resolvido e o que ficou como dívida

| # | Situação | Como foi resolvida, ou por que ficou |
|---:|---|---|
| 1 | Resolvida | Validação centralizada da duração e do horário final. |
| 2 | Resolvida | Remarcação valida datas e novo horário antes de alterar o registro. |
| 3 | Resolvida | Os dados pertencem a uma instância de `Agenda`. |
| 4 | Resolvida | `Atendimento` é uma dataclass com campos nomeados. |
| 5 | Resolvida | Foram adotados nomes descritivos em `snake_case`. |
| 6 | Resolvida | O serviço aplica regras e retorna resultados; `main.py` imprime as mensagens. |
| 7 | Resolvida | Removido o `except` genérico silencioso; dados inválidos geram `ValueError`. |
| 8 | Resolvida | Validações de texto, data, hora e duração são feitas antes da operação. |
| 9 | Resolvida | A busca de conflito usa `any`, que encerra a verificação ao encontrar conflito. |
| 10 | Resolvida | A verificação de conflito está centralizada em `existe_conflito`. |
| 11 | Dívida assumida | A regra fornecida define conflito apenas para o mesmo profissional, data e hora de início. Não foi ampliada para intervalos sobrepostos para evitar introduzir uma regra de negócio não especificada. |
| 12 | Resolvida | Os limites de expediente e duração foram nomeados como constantes. |

## 3. Decisões de projeto

| Decisão tomada | Alternativa descartada | Por que decidimos assim |
|---|---|---|
| Representar cada registro com `dataclass Atendimento`. | Lista de seis posições. | Campos nomeados deixam o código mais legível e reduzem erros por índice. |
| Separar modelos, validação, serviço e demonstração. | Manter tudo em um único arquivo e função. | Cada módulo tem uma responsabilidade e pode ser testado isoladamente. |
| Retornar `bool` para conflito/resultado e imprimir em `main.py`. | Imprimir dentro da regra de negócio. | A lógica pode ser reutilizada por outras interfaces sem alterar o serviço. |
| Lançar `ValueError` para dados inválidos. | Ignorar entradas ou retornar um valor padrão. | A falha fica explícita e a mensagem informa o campo e o valor problemático. |

## 4. Mudanças de comportamento

| Entrada ou situação | O que acontecia antes | O que acontece agora |
|---|---|---|
| Marcar atendimento às 20h | A função falhava silenciosamente. | Lança `ValueError` com a faixa de expediente válida. |
| Duração negativa, menor que 15, maior que 120 ou não múltipla de 15 | Algumas durações eram aceitas ou ignoradas sem explicação. | Lança `ValueError`. |
| Atendimento que termina após 18h | Não havia validação do horário final. | Lança `ValueError`. |
| Data inexistente ou fora de `AAAA-MM-DD` | Não havia validação. | Lança `ValueError`. |
| Paciente/profissional vazio ou tipo inesperado | Podia ser armazenado ou causar erro silencioso. | Lança `ValueError`. |

## 5. Como executar e gerar a documentação

| Item | Resposta |
|---|---|
| Comando para executar | `python main.py` |
| Comando para documentação HTML | `python -m pydoc -w agenda_facil.models agenda_facil.validators agenda_facil.service` |
| Onde fica a documentação | `docs/API.md`; o comando `pydoc` gera HTML no diretório corrente. |
| Saída do programa de demonstração | `Atendimento marcado para Ana` / `Horario ocupado` / `Atendimento marcado para Carla` / `Remarcado` / `14 Carla Dra. Souza MARCADO` |


## 6. Uso de ferramentas de IA

**Foram usadas ferramentas de IA neste trabalho?** Sim.

**Em quais etapas, e para quê?** Foi utilizada para modelar o readme e o relatório, convertendo de docx  para markdown. Além de ajudar na formatação da documentação e modelação das classes, métodos e funções, para facilitar no que importa de verdade: que é consertar o programa.
