"""Serviços de negócio para a agenda de atendimentos."""

from .models import Atendimento
from .validators import validar_data, validar_horario, validar_texto


class Agenda:
    """Mantém os atendimentos em memória e aplica as regras da agenda."""

    def __init__(self) -> None:
        """Cria uma agenda vazia.

        Args:
            None.

        Returns:
            None.
        """
        self._atendimentos: list[Atendimento] = []


    def atendimentos(self) -> tuple[Atendimento, ...]:
        """Retorna uma visão imutável dos atendimentos cadastrados.

        Args:
            None.

        Returns:
            Tupla com os atendimentos cadastrados.
        """
        return tuple(self._atendimentos)


    def existe_conflito(
        self, profissional: str, 
        data: str, 
        hora: int, 
        ignorar: Atendimento | None = None
    ) -> bool:
        """Verifica se um profissional já possui atendimento no mesmo dia e hora.

        Args:
            profissional: Nome do profissional.
            data: Data do atendimento.
            hora: Hora de início.
            ignorar: Atendimento a excluir da verificação, como numa remarcação.

        Returns:
            True se existir conflito; caso contrário, False.

        Raises:
            ValueError: Se profissional, data ou hora forem inválidos.
        """
        validar_texto(profissional, "Profissional")
        validar_data(data)

        if isinstance(hora, bool) or not isinstance(hora, int) or not 0 <= hora <= 23:
            raise ValueError(f"A hora deve ser um inteiro entre 0 e 23; recebido: {hora!r}.")
        
        return any(
            atendimento is not ignorar
            and atendimento.profissional == profissional
            and atendimento.data == data
            and atendimento.hora == hora
            for atendimento in self._atendimentos
        )


    def marcar_consulta(
        self, paciente: str, 
        profissional: str, 
        data: str, 
        hora: int, 
        duracao: int, 
        verbose: bool = True
    ) -> bool:
        """Agenda um atendimento, sem imprimir mensagens.

        Args:
            paciente: Nome do paciente.
            profissional: Nome do profissional.
            data: Data no formato AAAA-MM-DD.
            hora: Hora de início.
            duracao: Duração em minutos.

        Returns:
            True se o atendimento foi marcado; False se o horário estiver ocupado.

        Raises:
            ValueError: Se qualquer dado violar as regras de negócio.
        """
        validar_texto(paciente, "Paciente")
        validar_texto(profissional, "Profissional")
        validar_data(data)
        validar_horario(hora, duracao)

        if self.existe_conflito(profissional, data, hora):
            if verbose: print("Horario ocupado")
            return False
        
        self._atendimentos.append(
            Atendimento(paciente, profissional, data, hora, duracao)
        )

        if verbose: print(f"Atendimento marcado para {paciente}")
        return True


    def remarcar_consulta(
        self, paciente: str, 
        data_atual: str, 
        hora_atual: int, 
        nova_data: str, 
        nova_hora: int,
        verbose: bool = True
    ) -> bool:
        """Remarca o atendimento de um paciente.

        Args:
            paciente: Nome do paciente.
            data_atual: Data atual no formato AAAA-MM-DD.
            hora_atual: Hora atual.
            nova_data: Nova data no formato AAAA-MM-DD.
            nova_hora: Nova hora de início.

        Returns:
            True se foi remarcado; False se o atendimento não existir ou o novo
            horário estiver ocupado.

        Raises:
            ValueError: Se os dados informados forem inválidos.
        """
        validar_texto(paciente, "Paciente")
        validar_data(data_atual)
        validar_data(nova_data)

        if isinstance(hora_atual, bool) or not isinstance(hora_atual, int) or not 0 <= hora_atual <= 23:
            raise ValueError(f"A hora atual deve ser um inteiro entre 0 e 23; recebido: {hora_atual!r}.")
        
        if isinstance(nova_hora, bool) or not isinstance(nova_hora, int) or not 0 <= nova_hora <= 23:
            raise ValueError(f"A nova hora deve ser um inteiro entre 0 e 23; recebido: {nova_hora!r}.")
        
        atendimento = next(
            (
                item for item in self._atendimentos
                if item.paciente == paciente and item.data == data_atual and item.hora == hora_atual
            ),
            None,
        )

        # no código original não tem nenhuma mensagem para caso não ache o atendimento para remarcar,
        # por isso, caso não ache o horário, ele irá fazer o print padrão
        if atendimento is None:
            if verbose: print("Horario ocupado")
            return False
        
        validar_horario(nova_hora, atendimento.duracao)

        if self.existe_conflito(atendimento.profissional, nova_data, nova_hora, ignorar=atendimento):
            if verbose: print("Horario ocupado")
            return False
        
        atendimento.data = nova_data
        atendimento.hora = nova_hora

        if verbose: print("Remarcado")
        return True


    def listar_consultas_por_data(self, data: str, verbose: bool = True) -> list[Atendimento]:
        """Lista os atendimentos de uma data, preservando a ordem de cadastro.

        Args:
            data: Data no formato AAAA-MM-DD.

        Returns:
            Lista dos atendimentos da data informada.

        Raises:
            ValueError: Se a data for inválida.
        """
        validar_data(data)

        atendimentos = [item for item in self._atendimentos if item.data == data]

        if verbose:
            self.printar_atendimentos(atendimentos)

        return atendimentos


    def printar_atendimentos(self, atendimentos: list[Atendimento]) -> None:
        for atendimento in atendimentos:
            print(
                atendimento.hora,
                atendimento.paciente,
                atendimento.profissional,
                atendimento.status,
            )
