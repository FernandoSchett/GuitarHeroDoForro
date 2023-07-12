from tupy import *

class Score(Label):
    def __init__(self) -> None:
        super().__init__('Pontuação: 0', 500, 9, font='Helvetica 30', color='white')
        self.__score = 0
        self.__highscore = 0

    # Getter methods
    
    def get_score(self):
        return self.__score
    
    def get_highscore(self):
        return self.__highscore
    
    # Setter methods
    
    def set_score(self, value):
        self.__score = value
    
    def set_highscore(self, value):
        self.__highscore = value
    
    def increment(self, value: int) -> None:
        """
        Método chamado quando uma nota é acertada pelo jogador.
        Atualiza a pontuação do jogador.
        """
        self.__score += value
        self.text = f'Pontuação: {self.__score}'

        if self.__score >= self.__highscore:
            self.__highscore = self.__score
        else:
            self.__highscore = self.__highscore
    
    def decrement(self, value: int) -> None:
        """
        Atualiza a pontuação do jogador.
        """
        self.__score -= value
        self.text = f'Pontuação: {self.__score}'
