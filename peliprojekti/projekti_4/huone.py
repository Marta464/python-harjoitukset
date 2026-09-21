from typing import Optional 
from esine import Esine

class Huone:
    def __init__(self, nimi: str, esine: Optional[Esine] = None):
        self.nimi: str = nimi
        self.esine: Optional[Esine] = esine