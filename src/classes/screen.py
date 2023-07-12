from tupy import *

class Screen(BaseImage):
    def __init__(self) -> None:
        super().__init__(file='start.png', x=450, y=250)