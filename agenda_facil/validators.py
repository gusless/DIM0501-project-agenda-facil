"""Validações de entrada e regras de negócio."""

from datetime import date

HORA_INICIO_MINIMA = 8
HORA_INICIO_MAXIMA = 17
HORA_FIM_MAXIMA = 18
DURACAO_MINIMA = 15
DURACAO_MAXIMA = 120
INTERVALO_DURACAO = 15


def validar_texto(valor: str, campo: str) -> None:
    """Valida um campo textual obrigatório.

    Args:
        valor: Texto informado.
        campo: Nome do campo para a mensagem de erro.

    Returns:
        None.

    Raises:
        ValueError: Se o valor não for texto não vazio.
    """
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} deve ser um texto não vazio; recebido: {valor!r}.")


def validar_data(data_texto: str) -> None:
    """Valida uma data no formato AAAA-MM-DD.

    Args:
        data_texto: Data a validar.

    Returns:
        None.

    Raises:
        ValueError: Se a data não existir ou não seguir o formato exigido.
    """
    if not isinstance(data_texto, str):
        raise ValueError(f"A data deve estar no formato AAAA-MM-DD; recebido: {data_texto!r}.")
    
    try:
        data_convertida = date.fromisoformat(data_texto)
    except ValueError as exc:
        raise ValueError(
            f"Data inválida {data_texto!r}; informe uma data existente no formato AAAA-MM-DD."
        ) from exc
    if data_convertida.isoformat() != data_texto:
        raise ValueError(
            f"Data inválida {data_texto!r}; informe uma data no formato AAAA-MM-DD."
        )


def validar_horario(hora: int, duracao: int) -> None:
    """Valida o horário de início e a duração de um atendimento.

    Args:
        hora: Hora de início, entre 8 e 17.
        duracao: Duração em minutos.

    Returns:
        None.

    Raises:
        ValueError: Se horário ou duração violarem as regras de negócio.
    """
    if isinstance(hora, bool) or not isinstance(hora, int):
        raise ValueError(f"A hora deve ser um inteiro entre 8 e 17; recebido: {hora!r}.")
    
    if not HORA_INICIO_MINIMA <= hora <= HORA_INICIO_MAXIMA:
        raise ValueError(
            f"Hora de início inválida {hora!r}; o expediente permite início entre "
            f"{HORA_INICIO_MINIMA}h e {HORA_INICIO_MAXIMA}h."
        )
    
    if isinstance(duracao, bool) or not isinstance(duracao, int):
        raise ValueError(f"A duração deve ser um inteiro em minutos; recebido: {duracao!r}.")
    
    if not DURACAO_MINIMA <= duracao <= DURACAO_MAXIMA or duracao % INTERVALO_DURACAO:
        raise ValueError(
            f"Duração inválida {duracao!r}; use de {DURACAO_MINIMA} a "
            f"{DURACAO_MAXIMA} minutos, em múltiplos de {INTERVALO_DURACAO}."
        )
    
    if hora * 60 + duracao > HORA_FIM_MAXIMA * 60:
        raise ValueError(
            f"O atendimento das {hora}h com duração de {duracao} minutos termina após "
            f"{HORA_FIM_MAXIMA}h."
        )
