class Esine:
    def __init__(self, nimi: str, paino: float):
        self.nimi: str = nimi
        self.paino: float = paino

    def __str__(self) -> str:
        return f"Olio: {self.nimi}, Paino: {self.paino} kg"