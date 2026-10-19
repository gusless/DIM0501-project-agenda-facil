"""Modelos de dados do AgendaFácil."""

from dataclasses import dataclass


@dataclass
class Atendimento:
    """Representa um atendimento agendado.

    Args:
        paciente: Nome do paciente.
        profissional: Nome do profissional responsável.
        data: Data no formato AAAA-MM-DD.
        hora: Hora de início, em formato de 24 horas.
        duracao: Duração em minutos.
        status: Situação do atendimento.
    """

    paciente: str
    profissional: str
    data: str
    hora: int
    duracao: int
    status: str = "MARCADO"
