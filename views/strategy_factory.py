from models.tipo_usuario import TipoUsuario
from views.permissao_strategy import PermissaoAdmin, PermissaoComum

class StrategyFactory:
    @staticmethod
    def obter_estrategia(tipo_usuario):
        estrategias = {
            TipoUsuario.ADMINISTRADOR: PermissaoAdmin(),
            TipoUsuario.COMUM: PermissaoComum()
        }
        return estrategias.get(tipo_usuario, PermissaoComum())