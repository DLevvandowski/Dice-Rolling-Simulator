from random import randint

class Die():
    """Klasa przedstawiająca pojedynczą kość do gry."""

    def __init__(self, num_sides=6):
        """Przyjęcie założenia, że kość do gry ma postać sześcianu."""
        self.num_sides = num_sides

    def roll(self):
        """Zwraca losowy wynik rzutu kością."""
        return randint(1, self.num_sides)