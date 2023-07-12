from tupy import *

class User(Image):
    """
    Classe responsável por armazenar os dados do jogador.

    Atributos:
    - highscore: pontuação máxima do jogador
    - name: nome do jogador
    - file: imagem do jogador

    Métodos:
    - hit_note(): é chamado quando uma nota é acertada pelo jogador
    """
    def __init__(self, name: str, file: str) -> None:        
        self.__highscore = 0
        self.__score = 0
        self.__name = name
        self.__file = file
        self._hide()

    # Getter methods

    def get_highscore(self) -> int:
        return self.__highscore

    def get_score(self) -> int:
        return self.__score

    def get_name(self) -> str:
        return self.__name

    def get_file(self) -> str:
        return self.__file

    # Setter methods

    def set_highscore(self, value: int) -> None:
        self.__highscore = value

    def set_score(self, value: int) -> None:
        self.__score = value

    def set_name(self, value: str) -> None:
        self.__name = value

    def set_file(self, value: str) -> None:
        self.__file = value

    def hit_note(self, value: int) -> None:
        """
        Método chamado quando uma nota é acertada pelo jogador.
        Atualiza a pontuação do jogador.
        """
        pass
