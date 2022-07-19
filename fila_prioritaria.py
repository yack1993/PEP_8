#Usando Pip8
#mypy, verica os erros no código de todos os aquivos que foram importados na class
#pip install mypy ex: mypy main.py

#flake8, verifica os erros na classe
#pip install flake8 ex: flake8 main.py

from typing import Dict, List, Union

from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada

classes = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self)-> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: str)-> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return ('Cliente atual:{}, dirija-se ao caixa: {}'.format(cliente_atual, caixa))

    def estatisticas(self, retorna_estatistica: classes) -> dict:

        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)
