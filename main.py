"""Ponto de entrada e demonstração do AgendaFácil."""

from agenda_facil import Agenda


def executar_demonstracao() -> None:
    """Executa a demonstração exigida no enunciado.

    Args:
        None.

    Returns:
        None.
    """
    agenda = Agenda()

    agenda.marcar_consulta("Ana", "Dr. Silva", "2026-10-05", 9, 30)
    agenda.marcar_consulta("Bruno", "Dr. Silva", "2026-10-05", 9, 30)
    agenda.marcar_consulta("Carla", "Dra. Souza", "2026-10-05", 14, 60)
    agenda.remarcar_consulta("Ana", "2026-10-05", 9, "2026-10-06", 10)
    agenda.listar_consultas_por_data("2026-10-05")


if __name__ == "__main__":
    executar_demonstracao()
